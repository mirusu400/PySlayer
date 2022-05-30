from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import sqlite3
import random

# Ingame Init packet


def opcode_07(tcp_connections_list, my_tcp_connections) -> bytes:
    
    payload = b"\x07"  # opcode 7
    tcp_connection_len = len(tcp_connections_list)
    payload += p8u(tcp_connection_len)  # Must be >= 1
    payload += get_packets_from_connections(my_tcp_connections)
    for tcp_connections in tcp_connections_list:
        if tcp_connections == my_tcp_connections:
            continue
        payload += get_packets_from_connections(tcp_connections)
    return payload


def get_packets_from_connections(tcp_connection):
    payload = b''
    player = tcp_connection.player
    iptables = []
    if player.ip is None:
        iptables = [0,0,0,0]
    else:
        try:
            iptables = list(map(int, player.ip.split('.')))
        except:
            print("[-] Iptable error!")
            iptables = [127,0,0,1]
    payload += pstr(player.character_name, 17)
    payload += p32u(player.uid)  # Unique Character opcode, must be >= 2
    payload += p32u(1)
    payload += p16u(0)  # If 1, send packet below:

    # payload += p8u(2)
    # payload += pstr("나혼자산다", 17)

    # If >1, send packet below{str 16 16}:
    # If ==1, Bool
    # Guild info
    payload += p16u(0)
    # payload += pstr("MyGuild", 17)
    # payload += p16u(0)
    # payload += p16u(0)

    

    # if >= 4, send packet below:
    # {
    #   16 str
    #   if 4:
    #     16 16 16
    #   if else:
    #     16 16 16
    #   16
    # }
    payload += p8u(0)
    # payload += p16u(1)
    # payload += pstr("내혼녀", 17)
    # payload += p16u(10)
    # payload += p16u(11)
    # payload += p16u(12)
    # payload += p16u(13)

    # payload += p16u(1)
    # payload += b"mirusu403012345\0" #partnername

    # payload += p16u(0)
    # payload += p16u(0)
    # payload += p16u(0)
    # payload += p16u(0)

    # === end if
    payload += p8u(player.job1) # 1차 전직
    payload += p8u(player.job2) # 2차 전직
    # payload += p16u(12)
    payload += p8u(player.level)  # Level
    payload += p8u(20) # 계급

    payload += p8u(0)  # Initial action (ex. 1 -> attack)

    for i in player.apparences:  # 외형 (loop 17)
        payload += p16u(i)

    payload += p16u(player.str)  # 힘
    payload += p16u(player.dex)  # 민첩
    payload += p16u(player.int)  # 지혜
    payload += p16u(player.tol)  # 근성

    for i in player.equips:  # Equip (loop 15)
        payload += p16u(i)
        for j in range(0, 6): # Equip enchant
            payload += p16u(0)
    # line 1874

    for i in range(0, 10): # Cash Equip
        payload += p16(0) # Item Id
        payload += p16(0)   # 속성부여아이템 ID
        payload += p16(0)   # 속성부여아이템 ID

    # line 1886
    payload += p8u(0)
    # Buff things
    # for i in [88, 90, 94, 0x15B]:
    #     payload += p16u(1)
    # print(x, y)

    payload += p8u(0)

    payload += pf64(player.xpos)
    payload += pf64(player.ypos)

    payload += p32u(32)
    payload += p8u(0)  # Bool
    payload += p8u(1)

    payload += p32u(501)
    payload += p32u(502)
    payload += p8u(100)
    payload += p32u(503)

    payload += p8u(iptables[3])
    payload += p8u(iptables[2])
    payload += p8u(iptables[1])
    payload += p8u(iptables[0])

    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool

    payload += p16u(player.hp)  # HP
    payload += p16u(player.mp) # MP

    payload += p32u(1)
    payload += p8u(1)

    # these packets are send on else method..
    # payload += p8u(1) # bool
    # payload += p8u(1)
    # payload += pstr("123456789", 13)  # 13 bytes
    # payload += p8u(1)
    # payload += p8u(1)
    # payload += p32u(800)
    # payload += p8u(1)
    # payload += p16u(101)
    # payload += p16u(101)

    # for i in range(0,8000):
    #     payload += p8u(i % 0xFF)
    return payload



