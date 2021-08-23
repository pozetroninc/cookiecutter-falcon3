# -*- coding: utf-8 -*-
"""
Just a websocket example
"""
# System imports
import json
# Third-party imports
from falcon.asgi import Request, Response, WebSocket
from falcon import WebSocketDisconnected


class SampleWebsocket:

    async def on_get(self, req: Request, example_param: str):
        pass

    async def on_websocket(self, req: Request, ws: WebSocket, example_param: str):
        try:
            await ws.accept()
        except WebSocketDisconnected:
            return
        while True:
            try:
                payload_str = await ws.receive_text()
                await ws.send_text(f'{example_param} says GOOD')
            except WebSocketDisconnected:
                # Do any necessary cleanup, then bail out
                return
            except TypeError:
                # The received message payload was not of the expected
                #   type (e.g., got BINARY when TEXT was expected).
                pass
            except json.JSONDecodeError:
                # The default media deserializer uses the json standard
                #   library, so you might see this error raised as well.
                pass
