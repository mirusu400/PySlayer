#!/usr/bin/python
import os

if not os.path.isfile("./_key.py"):
    print("Please put _key.py in root folder!")
    print("If you don't know what you should do,")
    print("Please read README.md")
    input()
    exit(1)

import argparse
import socket
import json
import time
import sqlite3
from threading import Thread, Lock
from channel_server import Channel_Server
from game_server import Game_Server
from patch_server import Patch_Server


def main_loop():
    """
    Start udp tcp server threads
    """
    lock = Lock()
    channel_server = Channel_Server(lock)
    game_server = Game_Server(lock)
    # patch_server = Patch_Server(lock)

    channel_server.start()
    game_server.start()
    # patch_server.start()
    is_running = True
    print("Single WS1 Emulator Server.")
    print(f"YOUR LOCAL IP: {socket.gethostbyname(socket.gethostname())}")
    print("--------------------------------------")
    print("quit : quit server")
    print("reset: reset server")
    print("map: change map")
    print("mob: spawn mob or npc")
    print("item: get item")
    print("hp: set hp")
    print("mp: set mp")
    print("--------------------------------------")

    while is_running:
        cmd = ""
        try:
            cmd = input("cmd >")
        except KeyboardInterrupt:
            print("Shutting down  server...")
            channel_server.is_listening = False
            game_server.is_listening = False
            # patch_server.is_listening = False

            is_running = False
        if cmd == "quit" or cmd == "exit" or cmd == "q":
            print("Shutting down  server...")
            channel_server.is_listening = False
            game_server.is_listening = False
            # patch_server.is_listening = False

            is_running = False
        elif cmd == "reset":
            print("Resetting server...")
            game_server.is_listening = False
            while game_server.is_alive:
                time.sleep(0.1)
            game_server.start()
            print("Resetting server... Done!")
        else:
            game_server.send_custom_opcode(cmd)

    channel_server.join()
    game_server.join()


if __name__ == "__main__":
    """
    Start a game server
    """
    # parser = argparse.ArgumentParser(description='Simple game server')
    # parser.add_argument('--tcpport',
    #                     dest='tcp_port',
    #                     help='Listening tcp port',
    #                     default="1234")
    # parser.add_argument('--udpport',
    #                     dest='udp_port',
    #                     help='Listening udp port',
    #                     default="1234")
    # parser.add_argument('--capacity',
    #                     dest='room_capacity',
    #                     help='Max players per room',
    #                     default="3")

    # args = parser.parse_args()

    main_loop()
