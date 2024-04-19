import pandas as pd
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    daily_sum = data.groupby(pd.Grouper(key='datetime', freq='1D')).sum() * 3 * 3600
    daily_sum = daily_sum.reset_index()

    daily_sum['year'] = np.nan
    daily_sum['month'] = np.nan

    for i in range(len(daily_sum)):
        daily_sum.loc[i, 'year'] = daily_sum['datetime'].iloc[i].year
        daily_sum.loc[i, 'month'] = daily_sum['datetime'].iloc[i].month

    daily_sum['year'] = daily_sum['year'].astype(int)
    daily_sum['month'] = daily_sum['month'].astype(int)

    return daily_sum


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
