import netifaces as ni
from mitmproxy import ctx
from mitmproxy.options import Options
from mitmproxy.tools import web

from proxy.proxy_handler import ConnectionInspector


async def start_proxy(
    interface: str = ni.ifaddresses("en0")[ni.AF_INET][0]["addr"],
    port: int = 8081,
):
    options = Options(
        listen_host=interface,
        listen_port=port,
        ignore_hosts=[],
    )
    master = web.master.WebMaster(options)
    ctx.options.web_columns = ["tls", "method", "path", "status", "timestamp"]
    master.addons.add(ConnectionInspector())

    try:
        print(f"Starting mitmproxy on {interface}:{port}")
        print(f"Connect and navigate to http://mitm.it")
        await master.run()
    except KeyboardInterrupt:
        print("Stopping mitmproxy...")
        master.shutdown()
