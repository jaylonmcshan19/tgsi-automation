def handler(event, context):
    print("Incoming request:", event)
    return {
        "statusCode": 200,
        "body": "Request received successfullly!"
    }
