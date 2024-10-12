import os

from httpx import Client, Timeout, Limits
from openai import OpenAI

DEFAULT_TIMEOUT = Timeout(timeout=100, connect=100, pool=100)
DEFAULT_LIMITS = Limits(max_connections=2, max_keepalive_connections=2)


def get_httpx_client():
    proxy = os.getenv("PROXY_URL")
    if proxy:
        httpx_proxy = f"http://{proxy}"
        client = Client(proxies=httpx_proxy, verify=False, timeout=DEFAULT_TIMEOUT, limits=DEFAULT_LIMITS)
    else:
        client = Client(timeout=DEFAULT_TIMEOUT, limits=DEFAULT_LIMITS)
    return client

def get_openai_client():
    return OpenAI(http_client=get_httpx_client(), api_key=os.getenv("OPENAI_API_KEY"))