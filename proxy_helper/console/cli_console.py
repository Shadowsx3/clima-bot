import cmd

from interceptor.interceptor_manager import InterceptorManager
from interceptor.interceptors import interceptors


class CLIConsole(cmd.Cmd):
    prompt = ""

    def __init__(self):
        super().__init__()
        self.interceptors = interceptors
        self.load_interceptors()
        for interceptor in self.interceptors:
            InterceptorManager.add_interceptor(interceptor)

    def load_interceptors(self):
        print("Interceptor Status:")
        for interceptor in self.interceptors:
            status = "[X]" if interceptor["enabled"] else "[ ]"
            print(f"{status} {interceptor['name']} (ID: {interceptor['id']})")

    def do_toggle(self, line):
        """Toggle an interceptor on or off by ID."""
        interceptor_id = line.strip()
        InterceptorManager.toggle_interceptor(interceptor_id)
        self.load_interceptors()

    def do_exit(self, line):
        """Exit the CLI."""
        return True

    def default(self, line):
        print("Unknown command.")
