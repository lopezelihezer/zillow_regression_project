import pandas as pd
import numpy as np
import os
from env import host, user, password
from sklearn.model_selection import train_test_split

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
    df['bed'] = df.bedroomcnt
    df['bath'] = df.bathroomcnt
    df['taxvalue'] = df.taxvaluedollarcnt
    df = df.drop(columns=['calculatedfinishedsquarefeet','bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt'])
    df = df.dropna()
    col_list = ['bed', 'bath', 'area', 'taxvalue', 'taxamount']
    df = remove_outliers(df, 1, col_list)
    df = df.loc[
                 (df.transactiondate.str.contains('2017-05')) 
               | (df.transactiondate.str.contains('2017-06')) 
               | (df.transactiondate.str.contains('2017-07')) 
               | (df.transactiondate.str.contains('2017-08'))
                ]
    # Converting transactiondate into datetime

    df['transactiondate'] = pd.to_datetime(df['transactiondate'],\
                        format = '%Y-%m-%d', errors = 'coerce')

    # Creating columns for month, day, and week. We know they're all 2017
    # so we don't need year

    df['tdate_month'] = df['transactiondate'].dt.month
    df['tdate_day'] = df['transactiondate'].dt.day
    df['tdate_week'] = df['transactiondate'].dt.week

    # Dropping transactiondate

    df.drop(columns='transactiondate', inplace=True)
    county_dict = {
                6059: "Orange",
                6037: "Los Angeles",
                6111: "Ventura"
                }
    df['county'] = df.fips.replace(county_dict)
    df["taxrate"] = df.taxamount / df.taxvalue

    return df


###################### Split DataFrame ####################

def split(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123)
    return train, validate, test

###################### Make Variables ####################

def make_vars():
    
    target = "taxvalue"
    clist = ['area', 'bed', 'bath']

    # split train into X (dataframe, only col in list) & y (series, keep target only)
    X_train = train[clist]
    y_train = train[target]
    y_train = pd.DataFrame(y_train)
    
    # split validate into X (dataframe, only col in list) & y (series, keep target only)
    X_validate = validate[clist]
    y_validate = validate[target]
    y_validate = pd.DataFrame(y_validate)

    # split test into X (dataframe, only col in list) & y (series, keep target only)
    X_test = test[clist]
    y_test = test[target]
    y_test = pd.DataFrame(y_test)
    
    return target, X_train, y_train, X_validate, y_validate, X_test, y_test

###################### Split DataFrame ####################

###################### Split DataFrame ####################

###################### Split DataFrame ####################