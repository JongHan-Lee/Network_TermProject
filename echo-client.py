import socket
from commandParser import CommandParser
import sys

IP = '127.0.0.1' #서버의 주소
S_PORT = 7777      #서버 포트넘버
CHAT_SERVER_PORT = eval(sys.argv[1]) #채팅방 번호
parser = CommandParser() #파서 객체 생성


print("\nChatRoom Num : {}\n".format(CHAT_SERVER_PORT))


## 채팅서버 열기
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, CHAT_SERVER_PORT))


while True:

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 레지서버에 접속할 소켓

    print("명령어 목록은 /help 를 입력하세요.")
    option = input(">>")
    print()


    if option == "1":

        clientSocket.connect((IP, S_PORT))  # 레지서버 접속
        print("레지 서버에 연결되었습니다.")

        clientSocket.sendall(str(CHAT_SERVER_PORT).encode()) # 채팅방번호 전송
        clientSocket.sendall(option.encode())
        print("레지 서버에 IP주소를 등록했습니다.")

        clientSocket.close()

        serverSocket.listen(1)
        print("\n챗모드 중... 다른 유저 기다림...\n")
        userSocket, address = serverSocket.accept() #채팅방 상대 받기

        print("상대방과 접속되었습니다. ")
        print("대화 종료를 원하시면 /quit 를 입력하세요.\n")

        ## 대화 시작
        while True:

            msg = input("[TO] : ")

            if msg == "/quit":

                userSocket.sendall("disconnected".encode())
                userSocket.close()
                break

            else:

                userSocket.sendall(msg.encode())
                response = userSocket.recv(1024).decode()
                print("[FROM] : {}".format(response))

                if response == "disconnected":
                    userSocket.close()
                    break


    elif option == "2":

        clientSocket.connect((IP, S_PORT))  # 서버 접속

        clientSocket.sendall(str(CHAT_SERVER_PORT).encode())
        clientSocket.sendall(option.encode())

        chatRoom_list = clientSocket.recv(1024).decode() # 채팅방 목록 받기

        print("채팅방 목록\n{}\n".format(chatRoom_list))

        clientSocket.close()

    elif option == "3":

        clientSocket.connect((IP, S_PORT))  # 서버 접속

        clientSocket.sendall(str(CHAT_SERVER_PORT).encode())
        clientSocket.sendall(option.encode())

        print("채팅방을 목록에서 삭제하였습니다.")

        clientSocket.close()

    elif option == '4':

        infos = input("명령어 : connect [ip] [port] : ")
        chat_Owner_IP, chat_Owner_PORT = parser.parse(infos)

        clientSocket.connect((chat_Owner_IP, int(chat_Owner_PORT))) #채팅방에 접속

        print("상대방과 접속되었습니다.")
        print("대화 종료를 원하시면 /quit 를 입력하세요.\n")

        ## 대화 시작
        while True:
            msg = input("[TO] : ")

            if msg == '/quit':

                clientSocket.sendall("disconnected".encode())
                clientSocket.close()
                break

            else:

                clientSocket.sendall(msg.encode())
                response = clientSocket.recv(1024).decode()
                print("[FROM]: {}".format(response))

                if response == 'disconnected':
                    clientSocket.close()
                    break

    elif option == '5' :
        clientSocket.close()
        break

    elif option == '/help' :

        print("\n(1) : 서버에 내 채팅방등록 & 채팅 방 열기")
        print("(2) : 현재 입장 가능한 채팅방 보기")
        print("(3) : 서버에서 내 채팅방 삭제")
        print("(4) : 채팅방 입장하기")
        print("(5) : 종료하기\n")
        clientSocket.close()

    else :

        clientSocket.connect((IP, S_PORT))
        clientSocket.sendall(option.encode())

        data = clientSocket.recv((1024))
        print(data.decode())
        clientSocket.close()