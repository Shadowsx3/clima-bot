from mitmproxy import http

from interceptor.interceptor_manager import InterceptorManager


class ConnectionInspector:
    @staticmethod
    def request(flow: http.HTTPFlow) -> None:
        if InterceptorManager.apply_intercept(flow, False):
            print("Request modification applied.")

    @staticmethod
    def response(flow: http.HTTPFlow) -> None:
        if InterceptorManager.apply_intercept(flow, True):
            print("Mocked response applied.")
