
# import ngrok python sdk
import http.server
import socketserver
import threading
import time
import ngrok
import time
import creds

# start server
PORT = 9000
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)
httpd_thread = threading.Thread(target=httpd.serve_forever)
httpd_thread.start()


# Establish connectivity
listener = ngrok.forward(9000, authtoken=creds.NGROK_TOKEN)

# Output ngrok url to console
print(f"Ingress established at {listener.url()}")

# Keep the listener alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing listener")
