import macro


class CommandParser():


    def __init__(self):
        print("CommandParser initialized!!")

    def parse(self, command):

        if "connect" in command:
            ip, port = command.split()[1:3]
            print("connect command!: {}:{}".format(ip, port))
            return [macro.CONNECT_COMMAND, ip, port]
        elif "talk" in command:
            message = command.split()[-1]
            print("talk {}".format(message))
            return [macro.TALK_COMMAND, message]
        else:
            print("something else")
            return [macro.OTHERS_COMMAND]



