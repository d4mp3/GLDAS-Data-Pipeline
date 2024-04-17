import io
import pandas as pd
import requests
from datetime import datetime
from urllib.parse import urlencode, quote

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    base_url = "https://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/access/timeseries.cgi"
    query_parameters = {
        "variable": kwargs['gldas_param'],
        "type": "asc2",
        "location": f"GEOM:POINT({kwargs['long']}, {kwargs['lat']})",
        "startDate": kwargs['start_date'],
        "endDate": datetime.now().strftime("%Y-%m-%dT%H"),
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


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
