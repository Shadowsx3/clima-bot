from mitmproxy import http


class InterceptorManager:
    interceptors = []

    @classmethod
    def add_interceptor(cls, options):
        cls.interceptors.append(options)

    @classmethod
    def toggle_interceptor(cls, intercept_id):
        for interceptor in cls.interceptors:
            if interceptor.get("id") == intercept_id:
                interceptor["enabled"] = not interceptor["enabled"]
                print(
                    f"Toggled interceptor {interceptor['id']}: {'enabled' if interceptor['enabled'] else 'disabled'}"
                )
                break

    @classmethod
    def apply_intercept(cls, flow: http.HTTPFlow, response: bool = True):
        for interceptor in cls.interceptors:
            if (
                    interceptor["enabled"]
                    and interceptor["response"] == response
                    and interceptor["match"]["url"] in flow.request.url
            ):
                interceptor["call"](flow)
                return True
        return False
