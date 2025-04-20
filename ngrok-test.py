import creds
import time
from ngrok import ngrok, Listener
from threading import Thread
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler

class Publisher():

    def __init__(self, port: int=9000) -> None:
        self.port: int = port
        self.listener: Listener | None = None
        self.url: str | None = ""
        httpd = TCPServer(("0.0.0.0", self.port), SimpleHTTPRequestHandler)
        httpd_thread = Thread(target=httpd.serve_forever, daemon=True)
        httpd_thread.start()


    def publish(self) -> str:
        self.listener = ngrok.forward(self.port, authtoken=creds.NGROK_TOKEN)
        self.url = self.listener.url()
        return self.url

    
    def stop(self) -> None:
        assert self.listener is not None, "Listener has not been initialized!"
        assert self.url is not None, "URL has not been set!"
        ngrok.disconnect(self.url)


