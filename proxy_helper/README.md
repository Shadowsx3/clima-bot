## README: Interceptor Manager

### Overview
This tool allows you to intercept HTTP requests and modify responses using **mitmproxy**. You can control interceptors via a simple **CLI** interface, where you can dynamically enable or disable interceptors without restarting the proxy. It's designed to be flexible and interactive, providing real-time interception for testing and debugging.

### Installation & Setup

#### Prerequisites:
- **Python 3.8+**: Make sure Python is installed on your system.
- **mitmproxy**: Used to intercept and modify HTTP traffic.

#### 1. Setup Virtual Environment (Optional but recommended)
To ensure you don't pollute your global Python environment, create a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 2. Install Dependencies
Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

**Note:** It is necessary to install `mitmproxy`:
```bash
brew install mitmproxy # I have a mac
```

#### 3. Run the Application
To run the proxy with CLI control, use the `main.py` script and specify the port to listen on (e.g., `8080`):
```bash
python main.py
```

---

### Connecting to mitmproxy

1**Set Up Proxy on Your .env file**:
   - **Proxy IP**: Enter your computer's IP address.
   - **Port**: Enter the port of mitmproxy (e.g., `8081`).

Once connected, all HTTP traffic from your phone will be routed through mitmproxy, and you can intercept and modify responses.

---

### CLI Usage for Managing Interceptors

When you start the application, the **CLI interface** allows you to manage the interceptors. 
Here's an example of what the interface looks like:

```text
Interceptor Status:
[X] Send message Mock (ID: 0)
[ ] Firmware Error (ID: 1)
```

Each interceptor can be toggled on or off by using its **ID**. The `X` indicates that an interceptor is enabled, and `[ ]` indicates that it is disabled.

#### Available Commands:

- **Toggle Interceptor**: Toggle an interceptor on or off using its ID.
  ```bash
  > toggle 0
  ```
  This will enable/disable the **Firmware Update** interceptor.

- **Exit**: Exit the CLI interface.
  ```bash
  > exit
  ```

---

### Interceptor Setup

You can define custom interceptors inside the `interceptor_manager.py` file. Each interceptor has the following structure:

```python
{
    "name": "Interceptor Name",        # Name of the interceptor
    "response": True,                  # Whether it modifies the response or the request
    "enabled": True,                   # Whether the interceptor is initially enabled
    "match": {"url": "/some/path"},    # URL pattern to match
    "call": mock_function              # Function to call when the interceptor is triggered
}
```

### Adding New Interceptors

To add a new interceptor:

1. Create a mock function that handles the interception:
   ```python
   def mock_new_response(flow: http.HTTPFlow):
       flow.response = http.Response.make(
           200,
           b'{"message": "New Interceptor!"}',
           {"Content-Type": "application/json"}
       )
   ```

2. Add the new interceptor to the `interceptors` list:
   ```python
   interceptors.append({
       "name": "New Interceptor",
       "response": True,
       "enabled": False,
       "match": {"url": "/new-endpoint"},
       "call": mock_new_response,
   })
   ```

3. Start or restart the application to apply the changes.

### Toggling Interceptors
Once your proxy is running and interceptors are defined, you can toggle them on and off using the CLI while the proxy is actively intercepting traffic. For instance:

- **To enable an interceptor** (toggle ID 1):
  ```bash
  > toggle 1
  ```

- **To disable an interceptor** (toggle ID 0):
  ```bash
  > toggle 0
  ```

These changes will immediately affect how mitmproxy handles the traffic. If the interceptor is enabled and matches a request, the response will be modified accordingly.

---

### Debugging and Logs

All requests and responses are logged to the web interface.