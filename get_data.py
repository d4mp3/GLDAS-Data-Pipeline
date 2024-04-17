import requests
import pandas as pd
import numpy as np
import io
import os
from datetime import datetime
from urllib.parse import urlencode, quote
from typing import Tuple, Dict, Any


START_DATE = "2013-01-01T00"
NOW = datetime.now()
COORDS = (52.23, 21.01)
GLDAS_PARAM = {
    "prcp": ("prcp", "GLDAS2:GLDAS_NOAH025_3H_v2.1:Rainf_f_tavg")
}
OUTPUT_DIR = "./data"


def get_time_series(start_date: str, end_date: str, latitude: float, longitude: float, variable: str) -> str:
    """
    Calls the data rods service to get a time series.

    Parameters:
        start_date (str): Start date for the time series in the format "YYYY-MM-DDTHH".
        end_date (str): End date for the time series in the format "YYYY-MM-DDTHH".
        latitude (float): Latitude coordinate for the location.
        longitude (float): Longitude coordinate for the location.
        variable (str): Variable for which the time series is requested. For example precipitation (prcp)

    Returns:
        str: Time series data in string format.
    """
    base_url = "https://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/access/timeseries.cgi"
    query_parameters = {
        "variable": variable,
        "type": "asc2",
        "location": f"GEOM:POINT({longitude}, {latitude})",
        "startDate": start_date,
        "endDate": end_date,
    }
    encoded_query_params = urlencode(query_parameters, quote_via=quote)
    full_url = f"{base_url}?{encoded_query_params}"
    print(full_url)
    max_attempts = 5
    done = False

    for attempt in range(max_attempts):
        try:
            r = requests.get(full_url)
            r.raise_for_status()
            done = True
            break
        except requests.exceptions.RequestException as e:
            if attempt < max_attempts - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
            else:
                raise Exception(f"Error: {e}")

    if not done:
        raise Exception(f"Failed after {max_attempts} attempts to fetch URL: {full_url}")
    
    return r.text


def parse_time_series(ts_str: str, param: str = None) -> Tuple[Dict[str, str], pd.DataFrame]:
    """
    Parses the response from data rods.

    Parameters:
        ts_str (str): Time series data in string format.
        param (str, optional): Name of the parameter to parse. Defaults to None.

    Returns:
        Tuple[Dict[str, str], pd.DataFrame]: A tuple containing parameters dictionary and parsed DataFrame.
    """
    lines = ts_str.split("\n")
    parameters = {}
    for line in lines[2:11]:
        key, value = line.split("=")
        parameters[key] = value

    if not param:
        param = "data"

    df = pd.read_table(io.StringIO(ts_str), sep="\t",
                                     names=["time", param],
                                     header=10, parse_dates=["time"])
    return parameters, df


def transform_timeseries(timeseries_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Transforms dataframe to specific dfs.

    Parameters:
        timeseries_df (pd.DataFrame): DataFrame containing the time series data.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: A tuple containing transformed DataFrames for daily sum and monthly mean.
    """
    daily_sum = timeseries_df.groupby(pd.Grouper(key='time', freq='1D')).sum() * 3 * 3600
    month_mean = (timeseries_df.groupby(pd.Grouper(key='time', freq='1D')).sum() * 3 * 3600).resample("ME").mean()

    daily_sum = daily_sum.reset_index()
    month_mean = month_mean.reset_index()

    daily_sum['year'] = np.nan
    daily_sum['month'] = np.nan

    for i in range(len(daily_sum)):
        daily_sum.loc[i, 'year'] = daily_sum['time'].iloc[i].year
        daily_sum.loc[i, 'month'] = daily_sum['time'].iloc[i].month

    daily_sum['year'] = daily_sum['year'].astype(int)
    daily_sum['month'] = daily_sum['month'].astype(int)
    daily_sum = daily_sum.rename(columns={'time': 'date'})

    month_mean['time'] = month_mean['time'].dt.strftime('%Y-%m')
    month_mean = month_mean.rename(columns={'time': 'date'})

    return daily_sum, month_mean


def create_directory_if_not_exists(directory_path: str) -> None:
    """
    Check if the directory exists, if not, create a new one.

    Parameters:
        directory_path (str): Path to the directory.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    else:
        print(f"Directory '{directory_path}' already exists.")


df_ts = parse_time_series(
    get_time_series(
        start_date=START_DATE,
        end_date=NOW.strftime("%Y-%m-%dT%H"),
        latitude=COORDS[0],
        longitude=COORDS[1],
        variable=GLDAS_PARAM["prcp"][1]
    ),
    param=GLDAS_PARAM["prcp"][0]
)


create_directory_if_not_exists(OUTPUT_DIR)

_, timeseries_df = df_ts
daily_sum, month_mean = transform_timeseries(timeseries_df)

timeseries_df.to_parquet('data/GLDAS_3H_interval.parquet')
print(f'The {timeseries_df} was saved successfully')
daily_sum.to_parquet('data/GLDAS_daily_sum.parquet')
print(f'The {daily_sum} was saved successfully')
month_mean.to_parquet('data/GLDAS_month_mean.parquet')
print(f'The {month_mean} was saved successfully')
