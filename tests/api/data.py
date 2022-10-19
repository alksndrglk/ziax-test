from http import HTTPStatus


success_data = {
    "status": "ok",
    "num_words": 2,
    "last_norm_form": ["строка"],
    "first_declined_word": [
        "тестовых",
        "тестового",
        "тестовые",
        "тестовом",
        "тестовому",
        "тестовый",
        "тестовой",
        "тестовая",
        "тестовою",
        "тестовое",
        "тестовую",
        "тестовыми",
        "тестовым",
    ],
}

testdata = [
    (
        HTTPStatus.UNAUTHORIZED.value,
        {
            "sentence": "TEST",
        },
        {},
        {
            "error": {
                "code": "unauthorized",
                "message": "401: Invalid authorization token: None",
            }
        },
    ),
    (
        HTTPStatus.BAD_REQUEST.value,
        {},
        {
            "content-type": "application/json",
            "key": "ziax",
        },
        {
            "error": {
                "code": "bad_request",
                "message": "Request validation has failed",
                "fields": {"sentence": ["Missing data for required field."]},
            }
        },
    ),
    (
        HTTPStatus.BAD_REQUEST.value,
        {
            "sentence": "english words тестовая строка",
        },
        {
            "content-type": "application/json",
            "key": "ziax",
        },
        {
            "error": {
                "code": "bad_request",
                "message": "Request validation has failed",
                "fields": {"sentence": ["Sentence can contain only cyrillic symbols"]},
            }
        },
    ),
    (
        HTTPStatus.BAD_REQUEST.value,
        {
            "sentence": " ",
        },
        {
            "content-type": "application/json",
            "key": "ziax",
        },
        {
            "error": {
                "code": "bad_request",
                "message": "Request validation has failed",
                "fields": {"sentence": ["Sentence cannot be empty"]},
            }
        },
    ),
]
