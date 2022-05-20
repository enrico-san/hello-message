import json
import mysql_helper

def lambda_handler(event, context):
    """Message digesting Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        body = json.loads(event['body'])['body']
        customerId = body['customerId']
        messageType = body['type']
        amount = body['amount']
    except:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "invalid event"
        }),
    }

    try:
        mysql_helper.update(customerId, messageType, amount)
    except:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "database error"
        }),
    }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "event digested"
        }),
    }
