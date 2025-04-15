class Response:
    Create_Response = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "Short_Url": "https://example.com/short_url",
                        "Control_Token": "1234567890"
                    }
                }
            }
        }
    }

    Regenerate_Response = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "message": "EXAMPLE_SHORT_CODE"
                    }
                }
            }
        }
    }

    Delete_Response = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "message": "URL with Short-Code EXAMPLE_SHORT_CODE deleted"
                    }
                }
            }
        }
    }

    Health_Response = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "status": "ok"
                    }
                }
            }
        }
    }