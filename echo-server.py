import socket

IP = '127.0.0.1'  # 로컬 호스트넘버
S_PORT = 7777  # 임의의 포트넘버

client_queue = []

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP타입 소켓객체 생성
serverSocket.bind((IP, S_PORT))  # 소켓을호스트와 포트넘버에 연결
serverSocket.listen(1)  # 클라이언트의 접속 허용

## queue에서 정보를 삭제하는 메소드
def removeClient(ip, chatRoom_Num):

    for i, client in enumerate(client_queue):
        if client[0] == ip and client[1] == chatRoom_Num:
            client_queue.pop(i)
            print("\n유저 정보가 삭제되었습니다.\n".format(i))
            return True

    print("No such client!! {}::{}".format(ip, chatRoom_Num))

    return False

## 클라이언트로부터 받은 요청을 수행하는 메소드
def handleCommand(command, clinet_socket, client_ip, chatRoom_Num):

    if command == '1':

        client_queue.append([client_ip, chatRoom_Num])
        print("채팅방 목록에 {}::{} 가 추가되었습니다.\n".format(client_ip, chatRoom_Num))

    elif command == '2':

        clinet_socket.sendall(str(client_queue).encode())
        print("\n채팅방 목록을 보냈습니다\n")

    elif command == '3':

        print("삭제 전 : {} \n".format(client_queue))
        removeClient(client_ip, chatRoom_Num)
        print("삭제 후 : {} \n".format(client_queue))

    else:

        print("\n[CommandNotFoundError]\n")
        clinet_socket.sendall("메뉴 다시 선택해라.".encode())


while True:

    print("[Server] waiting for client...")

    clientSocket, address = serverSocket.accept()  # 클라이언트 접속

    client_ip, chatRoom_Num = address[0], clientSocket.recv(4).decode() # 클라이언트로부터 채팅방 번호 받기
    command = clientSocket.recv(1).decode() # 클라이언트로부터 command 받기

    handleCommand(command, clientSocket, client_ip, chatRoom_Num)

    clientSocket.close()


serverSocket.close()
