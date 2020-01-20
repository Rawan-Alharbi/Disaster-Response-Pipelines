# Disaster Response Pipeline Project

### Installation: 
This project requires **Python 3.x** and the following Python libraries installed:
- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Jupyter-Notbook](https://jupyter.org/install.html)
- [NLTL](https://www.nltk.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask](https://www.palletsprojects.com/p/flask/)

### Project Introduction
This Project is part of data science nanodegree program by Udacity in collaboration with Figure Eight. The dataset contains pre-labelled tweet and messages from real-life disaster. In this project, messages are categorized so that you can send the messages to an appropriate disaster relief agency.    
This project is divided into three section:
1. ETL Pipeline: Extract data from source, transform the data to be used in alnalysis, then load the data to SQLite database.   
2. Machine learning pipeline: train a model to classifiy disaster messages.
3. Web app: that can be used by disaster relief agency to categorize messages.


### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database:   
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves:   
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


### Screenshots 
Screenshots of the app interface:   

![Interface](/Images/Interface.png)   
   

* Bar chart that shows distribution of message genres:   

![Message-Genres](/Images/MessageGenres.png)  

* Bar chart that shows distribution of message categories:    

![Messages-Categories](/Images/MessageCategories.png)


### License
This project is licensed under the MIT License - see the LICENSE file for details

