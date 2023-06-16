post_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"},
    },
    "required": ["id", "title", "body", "userId"]
}