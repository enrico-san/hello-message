import json
from unittest import TestCase
import requests

"""
Test the Lambda function running on SAM
"""

class TestApiGateway(TestCase):
    # TODO put the endpoint in the environment
    api_endpoint: str = "http://127.0.0.1:3000/hello"

    def setUp(self) -> None:
        self.message = {
            "body": {"customerId": 2,"type": "B","amount": "0.012","uuid": "a596b362-08be-419f-8070-9c3055566e7c"},
            "resource": "/hello",
            "path": "/hello",
            "httpMethod": "GET",
            "isBase64Encoded": False,
            "queryStringParameters": {
                "foo": "bar"
            },
            "pathParameters": {
                "proxy": "/path/to/resource"
            },
            "stageVariables": {
                "baz": "qux"
            },
            "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, sdch",
                "Accept-Language": "en-US,en;q=0.8",
                "Cache-Control": "max-age=0",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "US",
                "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Custom User Agent String",
                "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
                "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
                "X-Forwarded-Port": "443",
                "X-Forwarded-Proto": "https"
            },
            "requestContext": {
                "accountId": "123456789012",
                "resourceId": "123456",
                "stage": "prod",
                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
                "requestTime": "09/Apr/2015:12:34:56 +0000",
                "requestTimeEpoch": 1428582896000,
                "identity": {
                "cognitoIdentityPoolId": None,
                "accountId": None,
                "cognitoIdentityId": None,
                "caller": None,
                "accessKey": None,
                "sourceIp": "127.0.0.1",
                "cognitoAuthenticationType": None,
                "cognitoAuthenticationProvider": None,
                "userArn": None,
                "userAgent": "Custom User Agent String",
                "user": None
                },
                "path": "/prod/hello",
                "resourcePath": "/hello",
                "httpMethod": "POST",
                "apiId": "1234567890",
                "protocol": "HTTP/1.1"
            }
}


    def test_api_gateway(self):
        """
        Call the API Gateway endpoint with an event and check the response
        """
        response = requests.get(self.api_endpoint, json=self.message)
        self.assertDictEqual(response.json(), {"message": "event digested"})
