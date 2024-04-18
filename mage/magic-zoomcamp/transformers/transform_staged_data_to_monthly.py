import pandas as pd
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    monthly_mean = (data.groupby(pd.Grouper(key='datetime', freq='1D')).sum() * 3 * 3600).resample("M").mean()
    monthly_mean = monthly_mean.reset_index()
    monthly_mean['datetime'] = monthly_mean['datetime'].dt.strftime('%Y-%m')
    monthly_mean = monthly_mean.rename(columns={'datetime': 'date'})

    return monthly_mean


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
