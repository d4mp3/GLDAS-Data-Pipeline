import io
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    param = kwargs['param']
    lines = data.split("\n")
    parameters = {}
    for line in lines[2:11]:
        key, value = line.split("=")
        parameters[key] = value

    if not param:
        param = "data"

    df = pd.read_table(io.StringIO(data), sep="\t",
                                     names=["datetime", param],
                                     header=10, parse_dates=["datetime"])
    
    print(df.dtypes)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
