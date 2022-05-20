import json
from unittest import TestCase

import requests

"""
"""


class TestApiGateway(TestCase):
    # TODO put the endpoint in the environment
    api_endpoint: str = "http://127.0.0.1:3000/hello"

    def setUp(self) -> None:
        """
        Based on the provided env variable AWS_SAM_STACK_NAME,
        here we use cloudformation API to find out what the HelloWorldApi URL is
        """
        pass

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        with open('events/event.json') as f:
            data = json.load(f)
        response = requests.get(self.api_endpoint, json=data)
        self.assertDictEqual(response.json(), {"message": "event digested"})
