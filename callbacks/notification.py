if 'callback' not in globals():
    from mage_ai.data_preparation.decorators import callback

import requests

@callback('success')
def success_callback(parent_block_data, **kwargs):
    pass


def trigger_failed_notification(api_endpoint, message_payload, headers):
    return requests.post(api_endpoint, json=message_payload, headers=headers)

@callback('failure')
def alert_me(parent_block_data, **kwargs):
    # Define your API Endpoint, headers and message payload
    api_endpoint = "http://example.com/endpoint"
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    message_payload = {"message": "Pipeline failed"}

    # Send a POST request to the API
    response = trigger_failed_notification(
        'http://host.docker.internal:8000/guardar_mensaje?mensaje=holahola2', 
        {"mensaje": "Trigger failure"}, 
        {"Accept": "application/json", "Content-Type": "application/json"})
    # Here you can add your own error checking logic or logging
