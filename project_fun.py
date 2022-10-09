import pandas as pd
import numpy as np


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