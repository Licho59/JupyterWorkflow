import os
import pandas as pd
from urllib.request import urlretrieve

# Address to Seattle webpage with data concerned to numbers of bicycles crossing the Fremont Bridge
FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

# new function to deal with downloading data according to the file access + refactored code
def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the Fremont data.
    
    Parameters
    ----------
    filename: string(optional)
       location to save the data
    url: string(optional)
       web location of the data
    force_download: bool(optional)
       if True, force redownload of data
       
    Returns
    -------
    data: pandas DataFrame
       the Fremont bridge data
    """
   
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ['East', 'West']
    data['Total'] = data['East'] + data['West']
    return data
