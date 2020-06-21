## P2P Chat Program
---------------
#### Program 설명
>Napster 스타일 p2p 1:1 채팅 프로그램입니다.
>클라이언트들은 서버에 연결 가능한 채팅방 목록을
>요청하고 원하는 채팅방에 입장하여 상대방과 자유
>롭게 채팅을 진행합니다.

#### Program 실행 설명
---------------
-서버 파일 실행
``` C
$ python3 echo-server.py
```
-클라이언트 파일 실행
``` C
$ python3 echo-client [자신이 개설할 채팅방 번호]
```
#### Program 기능 설명
---------------
1. help
  ``` C
  /help
  ```
  - 명령어 목록을 출력해주는 기능
2. register

  - 서버에 IP와 채팅방 번호(PORT)를 등록하는 기능
  - 클라이언트는 서버에 채팅방을 등록하고 나와서 
    자신의 채팅방을 열어 상대방을 기다린다
  - 상대방이 입장하면 채팅을 시작한다
  - /quit 을 입력하면 채팅을 종료한다
  
3. request Chat Room List
 
  - 서버에 현재 입장 가능한 채팅방의 목록을 요청한다
  
4. close
  
  - 채팅이 끝나고 채팅방 방장은 서버에게
    자신의 채팅방 번호를 목록에서 지울것을 요청한다
    
5. connect to Chat Room
  ``` C
  connect [ip] [Chat Room Number]
  ```
  - 채팅방에 입장하여 채팅을 시작한다
  - /quit 을 입력하면 채팅을 종료한다
  
6. quit
  
  - 프로그램을 종료한다
