class Response:
    def __init__(self, status_code: int, json=None):
        self.status_code = status_code
        self._json = json

    def json(self):
        return self._json

class MockTransport:
    def __init__(self, handler):
        self._handler = handler

    async def __call__(self, url, params=None):
        return await self._handler(url, params=params)

class AsyncClient:
    def __init__(self, transport=None):
        self._transport = transport

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def get(self, url, params=None):
        if self._transport is None:
            raise RuntimeError("Network access not available")
        return await self._transport(url, params=params)
