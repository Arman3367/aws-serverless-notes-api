import json
import boto3
import uuid
from datetime import datetime, timezone
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("notes")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body, default=decimal_default)
    }


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


def lambda_handler(event, context):
    method = event["requestContext"]["http"]["method"]

    if method == "POST":
        body = json.loads(event.get("body", "{}"))
        content = body.get("content")

        if not content:
            return response(400, {"message": "content is required"})

        item = {
            "id": str(uuid.uuid4()),
            "content": content,
            "createdAt": datetime.now(timezone.utc).isoformat()
        }

        table.put_item(Item=item)
        return response(200, item)

    elif method == "GET":
        result = table.scan()
        return response(200, result.get("Items", []))

    elif method == "DELETE":
        path_params = event.get("pathParameters") or {}
        note_id = path_params.get("id")

        if not note_id:
            return response(400, {"message": "id is required"})

        table.delete_item(Key={"id": note_id})
        return response(200, {"message": "deleted", "id": note_id})

    return response(400, {"message": "unsupported method"})
