import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    hotels=pd.read_csv('zomato.csv')
    return hotels

def remove_unwanted_columns():
    #DO NOT REMOVE FOLLOWING LINE
    #call read_data_from_csv() function to get dataframe
   read_data_from_csv()
   hotels=pd.read_csv('zomato.csv')
   hotels.drop(['address','phone'], axis=1, inplace=True)
   return hotels

def rename_columns():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    #task2: rename columns  only these columns are allowed in the dataset
    # 1.	Id
    # 2.	Name
    # 3.	online_order
    # 4.	book_table
    # 5.	rating
    # 6.	votes
    # 7.	location
    # 8.	rest_type
    # 9.	dish_liked
    # 10.	cuisines
    # 11.	approx_cost
    # 12.	type
    read_data_from_csv()
    hotels=remove_unwanted_columns()
    hotels.rename(columns={'name': 'name', 'rate': 'rating', 'approx_cost(for two people)': 'approx_cost', 'listed_in(type)': 'type'}, inplace=True)
    return hotels

#task3: handle  null values of each column
def null_value_check():
    #DO NOT REMOVE FOLLOWING LINE
    #call rename_columns() function to get dataframe
    hotels=rename_columns()
    read_data_from_csv()
    hotels=rename_columns()
    hotels=hotels.dropna(subset=['name'], inplace=True)
    hotels['online_order'].fillna('NA', inplace=True)
    hotels['book_table'].fillna('NA', inplace=True)
    hotels['rating'].fillna(0, inplace=True)
    hotels['votes'].fillna(0, inplace=True)
    hotels['location'].fillna('NA', inplace=True)
    hotels['rest_type'].fillna('NA', inplace=True)
    hotels['dish_liked'].fillna('NA', inplace=True)
    hotels['cuisines'].fillna('NA', inplace=True)
    hotels['approx_cost'].fillna(0, inplace=True)
    hotels['type'].fillna('NA', inplace=True)
    #deleting null values of name column
    
    #handling null values of online_order
    
    #handling null values of book_table
    
    #handling null values of rating
    
    #handling null values of votes
    
    #handling null values of location
    
    #handling null values of rest_type
    
    #handling null values of dishliked
    
    #handling null values of cuisines
    
    #handling null values of approxcost
    
    #handling null values of type
    
    return hotels

#task4 #find duplicates in the dataset
def find_duplicates():
    #DO NOT REMOVE FOLLOWING LINE
    #call null_value_check() function to get dataframe
    hotels=null_value_check()
    read_data_from_csv()
    hotels=null_value_check()
    hotels=hotels.drop_duplicates()
    return hotels
    #droping the duplicates value keeping the first

#task5 removing irrelevant text from all the columns
def removing_irrelevant_text():
    #DO NOT REMOVE FOLLOWING LINE
    #call find_duplicates() function to get dataframe
    hotels= find_duplicates()
    hotels = hotels[hotels['name'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['online_order'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['book_table'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['rating'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['votes'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['location'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['rest_type'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['dish_liked'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['cuisines'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['approx_cost'].str.contains('RATED|Rated') == False]
    hotels = hotels[hotels['type'].str.contains('RATED|Rated') == False]
    
    return hotels

#task6: check for unique values in each column and handle the irrelevant values
def check_for_unique_values():
    #DO NOT REMOVE FOLLOWING LINE
    #call removing_irrelevant_text() function to get dataframe
    hotels=removing_irrelevant_text()
    hotels = hotels.loc[hotels['online_order'].isin(['Yes', 'No'])]
    hotels["rating"]=hotels["rating"].apply(lambda x : str(x).split("/")[0])
    hotels["rating"]=hotels["rating"].replace(["NEW","-"],0)
    
    return hotels

#task7: remove the unknown character from the dataset and export it to "zomatocleaned.csv"
def remove_the_unknown_character():
    #DO NOT REMOVE FOLLOWING LINE
    #call check_for_unique_values() function to get dataframe
    dataframe=check_for_unique_values()
    hotels=check_for_unique_values()
    hotels["name"]=hotels["name"].str.replace(r'[Ãx][^A-Za-z]+','', regex=True)
    hotels.to_csv('zomatocleaned.csv')
    return dataframe


    #remove unknown character from dataset
    
    #export cleaned Dataset to newcsv file named "zomatocleaned.csv"

    dataframe.to_csv('zomatocleaned.csv')
    return dataframe

#check if mysql table is created using "zomatocleaned.csv"
#Use this final dataset and upload it on the provided database for performing analysis in  MySQL
#To Run this task first Run the appliation for Terminal to create table named 'Zomato' and then run test.
def start():
    remove_the_unknown_character()
    return 

def task_runner():
    start()
