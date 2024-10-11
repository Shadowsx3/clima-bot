from interceptor.implementations.send_message_mock import mock_send_me_hi


interceptors = [
    dict(val, **{"id": str(i)})
    for i, val in enumerate(
        [
            {
                "name": "Send message Mock",
                "response": False,
                "enabled": True,
                "match": {"url": "/sendMessage"},
                "call": mock_send_me_hi,
            },
        ]
    )
]
