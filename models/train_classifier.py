import sys
import nltk
nltk.download(['punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pandas as pd
import numpy as np

from sqlalchemy import create_engine
import pickle

from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV



def load_data(database_filepath):
    engine = create_engine('sqlite:///'+database_filepath)
    df = pd.read_sql_table('messages', engine)
    X = df['message']
    y = df.drop(['id','message', 'original', 'genre'], axis=1)
    categories = y.columns
    
    return X, y, categories


def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

def build_model():
    
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize, ngram_range=(1, 2))),
    ('tfidf', TfidfTransformer(use_idf=True)),
    ('clf', MultiOutputClassifier(RandomForestClassifier(n_estimators= 200)))
    ])
    
    
    return pipeline
    


def evaluate_model(model, X_test, Y_test, category_names):
    
    y_pred = model.predict(X_test)
    print(classification_report(Y_test.iloc[:,1:].values, np.array([x[1:] for x in y_pred]), target_names=category_names))


    
def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()