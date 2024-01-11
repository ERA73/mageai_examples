if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import requests

def trigger_failed_notification(api_endpoint, message_payload, headers):
    response = requests.post(api_endpoint, json=message_payload, headers=headers)

@data_loader
def load_data(*args, **kwargs):
    0/0
    
    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
