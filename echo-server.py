import socket
from commandParser import CommandParser
import macro


IP = '127.0.0.1'  # 로컬 호스트넘버
S_PORT = 7777  # 임의의 포트넘버

client_queue = []
command_parser = CommandParser()


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP타입 소켓객체 생성
serverSocket.bind((IP, S_PORT))  # 소켓을호스트와 포트넘버에 연결
serverSocket.listen(1)  # 클라이언트의 접속 허용


def removeClient(ip, port):

    for i, client in enumerate(client_queue):
        if client[0] == ip and client[1] == port:
            client_queue[i][2].close()
            client_queue.pop(i)
            print("{}th client removed!!".format(i))
            return True
    print("No such client!! {}::{}".format(ip, port))
    return False




def debugPrint(message):
    print("[SERVER_DEBUG]: {}".format(message))


def handleCommand(command, clinet_socket, client_ip, client_port):
    debugPrint("::handleCommand::")
    debugPrint(command)
    result = command_parser.parse(command)

    if result[0] == macro.CONNECT_COMMAND:
        """
        result[1] = ip
        result[2] = port
        """

    elif result[0] == macro.TALK_COMMAND:
        """
        result[1] = message
        """
        pass
    else:
        if command == 'help':
            debugPrint("help command")
            clinet_socket.sendall("help help".encode())
        elif command == 'online_users':
            debugPrint("online_users")
            clinet_socket.sendall(str(
                [element[3] for element in client_queue]).encode())
        elif command == 'logoff':
            debugPrint("logoff command")
            print(client_queue)
            removeClient(client_ip, client_port)
            print(client_queue)
            # clinet_socket.sendall("logoff".encode())

        else:
            debugPrint("[CommandNotFoundError]")
            clinet_socket.sendall(command.encode())


while True:
    print("[Server] waiting for client...")
    clientSocket, address = serverSocket.accept()  # 클라이언트 접속시 새로운 소켓 생성
    print(address, "가 접속하였습니다.")

    client_server_info = eval(clientSocket.recv(1024).decode())
    client_ip, client_port = address[0], address[1]
    client_queue.append([client_ip, client_port, clientSocket, client_server_info])

    message = clientSocket.recv(1024)  # 클라이언트로부터 메시지를 받아 message에 저장
    decodeed_message = message.decode()

    print("before handle command")
    handleCommand(decodeed_message, clientSocket, client_ip, client_port)
    print("after  handle command")
    clientSocket.close()
    if decodeed_message == 'logoff':
        print("[Server]: logging off...!!!!!")
        break
    # message는 현재 String타입이기때문에 다시
    # bytes타입으로 incode시킨 후에 client에게 send back
    print('메시지를 보냈습니다.')


serverSocket.close()
