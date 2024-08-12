import json
import numpy as np
import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer, data_source
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@transformer
def transform(data, *args, **kwargs):
    df = json.loads(data["data"])
    df = df["jobs"]
    df = pd.json_normalize(df)
    df['annualSalaryMax'] = df['annualSalaryMax'].replace('null', np.nan)
    df = df.dropna(subset=['annualSalaryMax'])
    df['annualSalaryMax'] = pd.to_numeric(df['annualSalaryMax'])

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

