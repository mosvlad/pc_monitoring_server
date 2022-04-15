from http.server import BaseHTTPRequestHandler, HTTPServer

import psutil


class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        cpu = psutil.cpu_percent(interval=0.1)
        ram = psutil.virtual_memory().percent
        self._set_response()
        answer = "{'CPU':" + str(cpu) + ", 'RAM':" + str(ram) + "}"

        self.wfile.write(answer.encode(encoding='utf_8'))


def run_server(server_class=HTTPServer, handler_class=Handler, port=8080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print("STARTING SERVER")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('STOPPING SERVER')


def main():
    run_server()


if __name__ == '__main__':
    main()



