from mitmproxy import http


def mock_send_me_hi(flow: http.HTTPFlow):
    raw_body = flow.request.get_content().decode('utf-8')
    new_text = "Hi!!!!!"
    params = raw_body.split('&')
    for i, param in enumerate(params):
        if param.startswith('text='):
            params[i] = f'text={new_text}'
    modified_body = '&'.join(params)
    flow.request.set_content(modified_body.encode('utf-8'))
