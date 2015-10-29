# -*- coding: utf-8 -*-
import communicator
import math
import pprint
import sys


def convtemperature(scale1, scale2, value):
    funcvalid = scale1 is not None and scale2 is not None and value is not None
    if not funcvalid:
        return "Not enough parameters. The command is !temp [scale1] [scale2] [value to convert]."

    try:
        value = float(value)
    except ValueError:
        return "Given value was invalid. Please try again."

    scale1 = str.upper(scale1)
    scale2 = str.upper(scale2)
    convvalue = value
    scale1valid = True
    scale2valid = True

    if scale1 == "C":
        if scale2 == "K":
            convvalue = value + 273.15
        elif scale2 == "F":
            convvalue = (value * 1.8) + 32
        else:
            scale2valid = False

    elif scale1 == "F":
        if scale2 == "K":
            convvalue = (value + 459.67) * 5/9
        elif scale2 == "C":
            convvalue = (value - 32) * 5/9
        else:
            scale2valid = False

    elif scale1 == "K":
        if scale2 == "C":
            convvalue = value - 273.15
        elif scale2 == "F":
            convvalue = (value * 1.8) - 459.67
        else:
            scale2valid = False

    else:
        scale1valid = False

    if scale2valid is False:
        return "Chosen scale was invalid."

    if scale1valid is False:
        return "Original scale was invalid."

    return "{0:0.2f}° {1} is {2:0.2f}° {3}.".format(value, scale1, convvalue, scale2)


def commands(nick, chan, msg):
    if chan[0] != '#':
        return
    if msg[0] != '!':
        return

    command = msg.split(' ')[0][1:]
    if command == "temp":
        args = msg.split(' ')[1:]
        if len(args) == 3:
            communicator.sendmsg(chan, convtemperature(args[0], args[1], args[2]))
        else:
            communicator.sendmsg(chan, "Try using !temp [scale1] [scale2] [value to convert]")

    elif command == "shutdown":
        if str.lower(nick) == "krazy6446" or str.lower(nick) == "krazeh":
            sys.exit(0)
        else:
            communicator.sendmsg(chan, "Nope.")


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
