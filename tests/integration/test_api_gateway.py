import os
from unittest import TestCase

import requests

"""
Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test. 
"""


class TestApiGateway(TestCase):
    api_endpoint: str = "http://127.0.0.1:3000/hello"

    @classmethod
    def get_stack_name(cls) -> str:
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")
        if not stack_name:
            raise Exception(
                "Cannot find env var AWS_SAM_STACK_NAME. \n"
                "Please setup this environment variable with the stack name where we are running integration tests."
            )

        return stack_name

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
        response = requests.get(self.api_endpoint)
        self.assertDictEqual(response.json(), {"message": "event digested"})
