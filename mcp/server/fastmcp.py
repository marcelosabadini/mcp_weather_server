class FastMCP:
    def __init__(self, name: str):
        self.name = name

    def run(self):
        pass

    def tool(self):
        def decorator(func):
            return func
        return decorator

    @property
    def _mcp_server(self):
        return Server()

class Server:
    pass
