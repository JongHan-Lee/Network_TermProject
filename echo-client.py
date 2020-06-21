import socket
from commandParser import CommandParser
import sys

IP = '127.0.0.1' #서버의 주소
S_PORT = 7777      #서버 포트넘버

CHAT_SERVER_PORT = eval(sys.argv[1])
parser = CommandParser()

print("Chat port: {}".format(CHAT_SERVER_PORT))


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP타입 소켓객체 생성
serverSocket.bind((IP, CHAT_SERVER_PORT))  # 소켓을호스트와 포트넘버에 연결

# serverSocket.listen(1)  # 클라이언트의 접속 허용

while True:

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP타입 소켓 객체 생성

    option = input("선택하세요 >> (1) 로그인 & 챗 대기 모드, (2) user_infos, (3) logoff, (4) connect):")

    if option == "1":

        clientSocket.connect((IP, S_PORT))  # 서버 접속
        print("서버에 연결되었습니다.")
        clientSocket.sendall(option.encode())
        clientSocket.sendall(str(
            {
                "ip": IP,
                "port": CHAT_SERVER_PORT
            }
        ).encode())
        print("레지 서버에 로그인했다.")
        clientSocket.close()
        print("챗모드 중... 다른 유저 기다림...")
        serverSocket.listen(1)  # 클라이언트의 접속 허용
        userSocket, address = serverSocket.accept()
        print("다른 유저와 접속! {}:{}".format(address[0], address[1]))
        # while True:
        userSocket.sendall("hey man!".encode())
        response = userSocket.recv(1024).decode()
        print("[User{}:{}]: {}".format(address[0], address[1], response))

        while True:
            msg = input("[TO]")
            if msg == "/quit":
                userSocket.sendall("disconnected".encode())
                userSocket.close()
                break
            else:
                userSocket.sendall(msg.encode())
                response = userSocket.recv(1024).decode()
                print("[FROM]: {}".format(response))
                if response == "disconnected":
                    userSocket.close()
                    break


    elif option == "2":
        clientSocket.connect((IP, S_PORT))  # 서버 접속

        print("서버에 연결되었습니다")

        clientSocket.sendall(option.encode()) #String타입 메시지를 bytes타입으로 encode하여 서버로 send
        print("서버로 메시지를 전송하였습니다")

        data = clientSocket.recv(1024)
        print(repr(data.decode()))
        clientSocket.close()

    elif option == "3":

        clientSocket.connect((IP, S_PORT))  # 서버 접속
        print("서버에 연결되었습니다")
        clientSocket.sendall(option.encode())  # String타입 메시지를 bytes타입으로 encode하여 서버로 send

    elif option == '4':
        infos = input("write: connect [ip] [port]")
        _, user_ip, user_port = parser.parse(infos)

        clientSocket.connect((user_ip, int(user_port)))
        clientSocket.sendall("hello from other side".encode())
        response = clientSocket.recv(1024).decode()
        print("[FROM OTHER USRR:{}::{}]: {}".format(user_ip
                                                    , user_port, response
                                                    ))
        while True:
            msg = input("[TO:{}::{}:".format(user_ip, eval(user_port)))
            if msg == '/quit':
                clientSocket.sendall("disconnected".encode())
                clientSocket.close()
                break
            else:
                clientSocket.sendall(msg.encode())
                response = clientSocket.recv(1024).decode()
                print("[FROM OTHER USRR:{}::{}]: {}".format(user_ip
                                                            , user_port, response
                                                            ))
                if response == 'disconnected':
                    clientSocket.close()
                    break



    # else:
        #서버로부터 send back된 메시지를 String타입으로 decode하여 출력
        # data = clientSocket.recv(1024)
        # print(repr(data.decode()))


