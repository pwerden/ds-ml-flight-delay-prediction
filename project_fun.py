import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def outcome(time_delay):
    """
    Converts continuous target variable into binary.
    0 for being in time
    1 for being delayed
    """

    if time_delay > 0:
        return '1'
    elif time_delay == 0:
        return '0'
    else:
        return 'NaN'


def get_airport_info(data, data_air, location='ARRSTN', cols=['country']):
    """
    Adds information about the airport to the dataframe and returns it. 

    Args:
        data (df): the Train.csv dataframe. Defaults to df.
        data_air (df): the airports.csv dataframe. Defaults to df_air.
        location (str): Either the arrival or departure airport. Must be 'ARRSTN' or 'DEPSTN'. Defaults to 'ARRSTN'.
        cols (list): List of strings to specify which information to add. 
        Possible are:
        'icao'	'iata'	'name'	'city'	'subd'	'country'	'elevation'	'lat'	'lon'	'tz'
        Defaults to ['country']. Note, that elevation is provided in feet.

    Return:
        Dataframe with additional columns appended to input dataframe 
    """

    # get string s to add this to the new column names
    if location == 'ARRSTN':
        s = '_arr'
    elif location == 'DEPSTN':
        s  = '_dep'
    else:
        raise ValueError(f"location must either be 'ARRSTN' or 'DEPSTN' but got {location}. ")

    # loop through list of columns to add
    for col in cols:

        dict = {}
        # loop over rows
        for iata in data[location].unique():
            mask = data_air['iata'] == iata
            temp = data_air[col][mask]
            dict[iata] = temp.to_string(index=False)

        # add column
        data[col+s] = data[location]
        data[col+s] = data[col+s].replace(dict)

    # Remove rows where 'ARRSTN' or 'DEPSTN' is 'Series([], )'
    # (some iata from Train.csv are unknown to iata list in airports.csv)
    # these appear in each column of certain rows, so remove them based on last column added
    data = data.drop(data[(data[col+s] == 'Series([], )')].index)
    data.reset_index(drop=True, inplace=True)

    return data

# Calculate metric
def calculate_metrics(y_train, y_pred_train, y_test, y_pred_test):
    """Calculate and print out RMSE and R2 for train and test data

    Args:
        y_train (array): true values of y_train
        y_pred_train (array): predicted values of model for y_train
        y_test (array): true values of y_test
        y_pred_test (array): predicted values of model for y_test
    """

    print("Metrics on training data") 
    rmse = np.sqrt(mean_squared_error(y_train,y_pred_train))
    r2 = r2_score(y_train,y_pred_train)
    print("RMSE:", round(rmse, 3))
    print("R2:", round(r2, 3))
    print("---"*10)
    
    # Calculate metric
    print("Metrics on test data")  
    rmse = mean_squared_error(y_test, y_pred_test, squared=False)
    # you can get the same result with this line:
    # rmse = np.sqrt(mean_squared_error(y_test,y_pred_test))

    r2 = r2_score(y_test,y_pred_test)
    print("RMSE:", round(rmse, 3))
    print("R2:", round(r2, 3))
    print("---"*10)    


def error_analysis(y_test, y_pred_test):
    """Generated true vs. predicted values and residual scatter plot for models

    Args:
        y_test (array): true values for y_test
        y_pred_test (array): predicted values of model for y_test
    """     
    # Calculate residuals
    residuals = y_test - y_pred_test
    
    # Plot real vs. predicted values 
    fig, ax = plt.subplots(1,2, figsize=(15, 5))
    plt.subplots_adjust(right=1)
    plt.suptitle('Error Analysis')
    
    ax[0].scatter(y_pred_test, y_test, color="#FF5A36", alpha=0.7)
    ax[0].plot([-400, 350], [-400, 350], color="#193251")
    ax[0].set_title("True vs. predicted values", fontsize=16)
    ax[0].set_xlabel("predicted values")
    ax[0].set_ylabel("true values")
    ax[0].set_xlim((y_pred_test.min()-10), (y_pred_test.max()+10))
    ax[0].set_ylim((y_test.min()-40), (y_test.max()+40))
    
    ax[1].scatter(y_pred_test, residuals, color="#FF5A36", alpha=0.7)
    ax[1].plot([-400, 350], [0,0], color="#193251")
    ax[1].set_title("Residual Scatter Plot", fontsize=16)
    ax[1].set_xlabel("predicted values")
    ax[1].set_ylabel("residuals")
    ax[1].set_xlim((y_pred_test.min()-10), (y_pred_test.max()+10))
    ax[1].set_ylim((residuals.min()-10), (residuals.max()+10));


#MAIN function
#
if(__name__ == '__main__'):
    # import data
    df = pd.read_csv('data/Train.csv',parse_dates=['DATOP','STD'])
    df_air = pd.read_csv('data/airports.csv')

    # test get_airport_info
    # create test dataframe with additional columns
    df_test = get_airport_info(data=df, data_air=df_air, location='ARRSTN', cols=['country','elevation','lat','lon'])

    # test outcome
    df_test['outcome'] = df.target.apply(lambda x: outcome(x))

    print(df_test.head(6))