def readFile(file):
    htmlFileToServer = open(file, "r")
    return htmlFileToServer.read()

import socket as s

htmlFileToServer = open("index.html", "r")
htmlFile = htmlFileToServer.read()

HOST, PORT = '', 8888

listen_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
listen_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)
print('Serve HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    file_request = request.split()[1]
    file_request_as_string = file_request.decode("utf-8") 
    
    if file_request_as_string == "/":
        fileRequest = 'index.html'

    if file_request_as_string == "/script.js":
        fileRequest = 'script.js'

    file = readFile(fileRequest)

    http_response="""\
    HTTP 1.1 200 OK
    \n
    """ + file

    http_response_as_bytecode = http_response.encode()

    client_connection.sendall(http_response_as_bytecode)
    client_connection.close()
