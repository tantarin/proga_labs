from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs # распарсить параметры гет и пост-запросов


def load_templates():
    from jinja2 import Environment, PackageLoader, select_autoescape
    env = Environment(loader=PackageLoader('models', 'templates'),
                       autoescape=select_autoescape(['html', 'xml']))
    return env


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        import models

        user1 = models.zhukov.Zhukov()
        userTarinskaya = models.tarinskaya.Tarinskaya()

        result = bytes('Пользователи:', 'utf-8')
        result += bytes(user1.full_name, 'utf-8')
        result += bytes(userTarinskaya.full_name, 'utf-8')

        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        list_of_u = user1.full_name

        env = load_templates()
        template = env.get_template('layout.html')

        result2 = bytes(template.render(list_of_users=list_of_u), 'utf-8')

        self.wfile.write(result2)

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = parse_qs(str(body, 'utf-8'), keep_blank_values=True)
        
        data = {k: v[0] for k, v in data.items() }
        result = bytes(data['user'], 'utf-8') + bytes(":", 'utf-8') + bytes(data['pass'], 'utf-8')
        # result = bytes(data)
        self.wfile.write(result)


# Запуск локального сервера
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
