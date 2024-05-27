from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("admin", "senha@123", r"C:\Projetos\ftpServer_python\DIretorioFTP", "elradrmw")

handler = FTPHandler
handler.authorizer = authorizer

with FTPServer(("192.168.1.235", 21), handler) as server:
    server.max_cons = 5
    server.max_cons_per_ip = 2 
    server.serve_forever()