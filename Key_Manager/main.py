from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import os
from db import initialize_db, add_password, get_passwords
from crypto import encrypt_password, decrypt_password

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/listar':
            contrasenas = get_passwords()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Listar Contraseñas</title></head><body>", "utf-8"))
            self.wfile.write(bytes("<h1>Listado de Contraseñas</h1><table border='1'>", "utf-8"))
            self.wfile.write(bytes("<tr><th>Servicio</th><th>Usuario</th><th>Contraseña</th></tr>", "utf-8"))
            for servicio, usuario, contrasena_cifrada in contrasenas:
                contrasena = decrypt_password(contrasena_cifrada)
                self.wfile.write(bytes(f"<tr><td>{servicio}</td><td>{usuario}</td><td>{contrasena}</td></tr>", "utf-8"))
            self.wfile.write(bytes("</table><br><a href='/'>Volver a inicio</a></body></html>", "utf-8"))
            return
        elif self.path == '/agregar.html':
            self.path = '/agregar.html'
        else:
            self.path = '/404.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/agregar':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            fields = urllib.parse.parse_qs(post_data.decode('utf-8'))
            servicio = fields.get('servicio', [''])[0]
            usuario = fields.get('usuario', [''])[0]
            contrasena = fields.get('contrasena', [''])[0]
            contrasena_cifrada = encrypt_password(contrasena)
            add_password(servicio, usuario, contrasena_cifrada)
            self.send_response(301)
            self.send_header('Location', '/listar')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><head><title>Error 404</title></head>', 'utf-8'))
            self.wfile.write(bytes('<body><h1>Error 404: Recurso no encontrado</h1>', 'utf-8'))
            self.wfile.write(bytes('<p>El recurso solicitado no se pudo encontrar.</p></body></html>', 'utf-8'))

if __name__ == "__main__":
    os.chdir('templates')
    initialize_db()
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Running server...")
    httpd.serve_forever()
