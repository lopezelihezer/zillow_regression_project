import pandas as pd
import numpy as np
import os
from env import host, user, password

###################### Acquire Zillow Data ######################

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    

def new_zillow_data():
    '''
    This function reads the zillow data from the Codeup db into a df.
    '''
    sql_query = """
                SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips, transactiondate
                FROM properties_2017
                JOIN predictions_2017 USING (parcelid)
                WHERE propertylandusetypeid IN ('261','260', '262', '263', '264', '265', '266', '268', '273', '276');
                """
    # Included single family residential, Residential general, rural residence, mobile home, townhouse, cluster home, condominium, row house, bungalow, patio home
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    return df

def get_zillow_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('zillow_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('zillow_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_zillow_data()
        
        # Cache data
        df.to_csv('zillow_df.csv')
        
    return df

###################### Remove Outliers ######################

def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

###################### Automated Clean DataFrame ####################

def wrangle_zillow():
    df = get_zillow_data()
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df['area'] = df.calculatedfinishedsquarefeet
    df = df.drop(columns='calculatedfinishedsquarefeet')
    df = df.dropna()
    df = remove_outliers(df, 1, df.columns)
    return df

