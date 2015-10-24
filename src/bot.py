import communicator


def commands(nick, chan, msg):
    if chan[0] != '#':
        return
    if msg[0] != '!':
        return

    command = msg.split(' ')[0][1:]
    if command == "hai":
        communicator.sendmsg(chan, "oh hai")


while 1:
    data = communicator.getfeed()
    print(data)

    if data.find("PING :") != -1:
        communicator.ping()

    if data.find(' PRIVMSG '):
        nick = data.split('!')[0][1:]
        channel = data.split(' PRIVMSG ')[-1].split(' :')[0]
        msgstart = data[1:].find(':')
        if msgstart != -1:
            msg = data[msgstart+2:]
            commands(nick, channel, msg)
