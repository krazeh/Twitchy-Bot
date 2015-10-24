import socket

owner = "Krazy6446"
server = "irc.swiftirc.net"
botnick = "ItchyBot"

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " :TwitchyBot by " + owner + "\n")
ircsock.send("NICK " + botnick + "\n")


def ping():
    ircsock.send("PONG :Pong\n")


def sendmsg(rec, msg):
    output = "PRIVMSG " + rec + " :" + msg + "\n"
    print output
    ircsock.send(output)


def join(chan):
    ircsock.send("JOIN #" + chan + "\n")


def getfeed():
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    return ircmsg

#simply joining a test chan
join("pitchbot")
