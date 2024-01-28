# Credit Spending Habits Visualization 🚀 🥇 <br> Credit Spending in India using Tableau and Streamlit


## Project/Goals 🎈
***
In this project, we will combine and practice implementing what we have learned throughout this course, including:

* SQL queries using pgadmin
* Cleaning data using python
* Creating an interactive dashboard with tableau
  
  
* Apply your bootcamp learnings into a single end-to-end project: Data retrieval, EDA / cleaning, Statistical modeling (optional), Tableau

* Main deliverable: Tableau dashboard(s) and presentation, Jupyter notebooks if used

  
***

## Project Structure

```
├── data                      <- Data Folder 
│   ├── cleaned_data_india_credit.csv <- Cleaned data source
│   ├── credit_card_india.csv <- Oringinal data source
│   
├── output                    <- Images Used in the Project and output files
│   ├── Credit Dash.png       <- dashboard snapshot
│   ├── sql_output.md         <- output of sql queries
│ 
├── src/modules               <- Source Code 
│   ├── cleaning_data.ipynb   <- code for data cleaning 
│   ├── SQL_Credit_card.ipynb <- code for sql queries
│   └── EDA.ipynb             <- EDA file
│   └── Credit_viz.twbx       <- tableau file with dashboard
      ├── streamlit           <- Folder For All The Streamlit App Code  
│         ├── app.py          <- viz app for different plots
│         ├── eda_app.py      <- pandas profiling
│         ├── requirements.txt<- list of all dependencies 
│
├── __init__.py              <- Package Initializer          
└── README.md                <- Project Documentation
```

***


## Files Used 📁
***

* Dataset - https://www.kaggle.com/datasets/thedevastator/analyzing-credit-card-spending-habits-in-india
* <img width="405" alt="image" src="https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/99081a6c-18eb-4727-939c-0d089a6dac5c">
* <img width="495" alt="image" src="https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/71d120b9-9a2c-4c82-8acf-5b94d7264864">

***
## Process ⏩
* Step 1: Aquire dataset and import into jupyter notebook, clean dataset and export file

* Step 2: Use cleaned file and import into tableau and SQL

* Step 3: Run sql queries to answer questions like top 5: Cities with fraud, which gender has most fraud, what credit card had most fraud

* Step 4: Make an interactive dashboard based on city and date on tableau
***

## Visualization 📊
![image](https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/0c06e9a8-b6d5-4c08-8344-89135030a721)
![image](https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/e347307b-d33e-45a6-8b81-4d3ce784f214)
![image](https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/c0649cb1-2074-47af-9b6c-da4b3c3e6f51)
![image](https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/13a46c83-00db-43e5-bc48-ab8be9dab5ba)
![image](https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/f88e9989-62a4-4cb5-b6d4-a36480229159)
***
## SQL Queries 📉
* Please refer to the following:
* [SQL Queries MD File](https://github.com/gu12934/LHL_Final_Capstone_Project/blob/main/ouput/sql_output.md)
* [ERD Diagram](https://github.com/gu12934/LHL_Final_Capstone_Project/blob/main/ouput/ERD_diagram.png)

***
## Word Cloud ☁️
![image](https://github.com/gu12934/LHL_Final_Capstone_Project/assets/36687057/fb29fc6b-3172-4695-861d-0aa55b706699)
***

## Streamlit 🧑‍🚀

* This gif showcases the pandas profiling module deployed on the streamlit that allows you to do EDA by uploading a dataset

![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjYzdWdrbTcycng0eHJtMWpjMnh3cjAwMjh6NTVydTF0M21rMXQzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tZCu365fLHh7lwbGJe/giphy.gif)

* This allows you to do EDA with any dataset uploaded, it will create various plots for you to conduct analysis, also deployed on streamlit
  
![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnBnM3QxeDkxeW15aHo0cWJ0em80M2VlYnN4OHltMzl0Nmt0dHpyMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LVEWCP6bR7EJhnpWRI/giphy.gif)

*Test out the app here: 
![Alt Text](https://lhlfinalcapstoneproject-eda.streamlit.app/)

## The Streamlit App 
To run the Streamlit App, run the following command: 

```python
streamlit run app.py


```
* Note for the above, you need to be in the correct folder
***
## Presentation 🌠
https://docs.google.com/presentation/d/1zzXzLE6kJSKPbSglUbs9xWFQATFGJms0aH-3kAz8Uek/edit#slide=id.p

[https://public.tableau.com/app/profile/gurmol.sohi/vizzes](https://public.tableau.com/app/profile/gurmol.sohi/viz/Credit_viz/Dashboard1)https://public.tableau.com/app/profile/gurmol.sohi/viz/Credit_viz/Dashboard1

* If you click on the city, it will adjust all the other graphs, you can also select specific months to gain insight
***
## Results 🔍
* Mumbai and Bengaluru had greatest spending, 
* Most spending was on bills, food, fuel
* Highest percentage of gold type was in Zira
* Lowest gold card type was in Achalpur
* The highest spend month was in August with a Platinum card
* Greater Mumbai had the highest expense type with Bills and lowest with entertainment
* Greater Mumbai had 14% of the total spending of the whole dataset
* 01/2015 had the highest amount of spending

## Challenges 🎱
***
* It was a challenge to create interactivty on tableau
* had lots of issues creating a db with sql-lite to begin with and running queries
* importing the file from a different folder into cleaning ipynb caused some issues
* streamlit was not working at first, issues with pandas profiling library
* adding a state column in excel online to make the tableau dashboard better

***
## Future Goals 🥅
* develop a ML model and make predictions on credit fraud
* compare to other datasets and other spending habits in different countries
* customer segmentation, credit risk, credit fraud detection (anomalies), credit approval projects coming soon
