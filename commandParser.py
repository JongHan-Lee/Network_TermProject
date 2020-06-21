

class CommandParser():

    def parse(self, command):

        if "connect" in command:
            ip, port = command.split()[1:3]
            return [ip, port]



