from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from game_server import Game_Tcp_Handler
from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import sqlite3
import random


# Ingame Init packet
def opcode_05(tcp_connection: Game_Tcp_Handler) -> bytes:
    player = tcp_connection.player
    iptables = []
    if player.ip is None:
        iptables = [0, 0, 0, 0]
    else:
        try:
            iptables = list(map(int, player.ip.split(".")))
        except:
            print(f"[-] Iptable error!, {player.ip}")
            iptables = [127, 0, 0, 1]
    payload = b"\x05"  # opcode 5
    payload += pstr(player.character_name, 17)
    payload += p32u(player.uid)  # Must be 2
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
    # 4 == 도적 ( 2 == 트랩퍼)
    # 5 == 마법사
    # 6 == 사제
    payload += p8u(player.job1)  # 1차 전직
    payload += p8u(player.job2)  # 2차 전직
    # payload += p16u(12)
    payload += p8u(player.level)  # Level
    payload += p8u(20)  # 계급

    payload += p8u(0)  # Bool

    for i in player.apparences:  # 외형 (loop 17)
        payload += p16u(i)

    payload += p16u(player.str)  # 힘
    payload += p16u(player.dex)  # 민첩
    payload += p16u(player.int)  # 지혜
    payload += p16u(player.tol)  # 근성

    for i in player.equips:  # Equip (loop 15)
        payload += p16u(i)
        for j in range(0, 6):  # Equip enchant
            payload += p16u(0)
    # line 1874

    for i in range(0, 10):  # Cash Equip
        payload += p16(0)  # Item Id
        payload += p16(0)  # 속성부여아이템 ID
        payload += p16(0)  # 속성부여아이템 ID

    payload += p8u(0)
    # Buff things
    # for i in [88, 90, 94, 0x15B]:
    #     payload += p16u(1)
    # print(x, y)

    payload += p8u(0)  # For loop below
    # ??
    # for i in range(0, 10):
    # payload += p16(1)

    payload += pf64(player.xpos)
    payload += pf64(player.ypos)

    payload += p32u(0)  # Initial action
    payload += p8u(1)  # Bool
    payload += p8u(1)

    payload += p32u(1)
    payload += p32u(1)
    payload += p8u(1)
    payload += p32u(1)

    payload += p8u(iptables[3])
    payload += p8u(iptables[2])
    payload += p8u(iptables[1])
    payload += p8u(iptables[0])

    # Maybe about actions?
    payload += p8u(0)  # Bool

    # payload += p8u((not is_my_connection))  # If checked, all characters are invisible
    payload += p8u(0)  # Bool

    payload += p8u(0)  # Bool -> issmallattack?
    payload += p8u(0)  # Bool -> isleftmove?
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(1)  # Bool

    payload += p16u(player.hp)  # HP
    payload += p16u(player.mp)  # MP

    payload += p32u(700)
    payload += p8u(30)

    # these packets are send on else method..
    payload += p8u(0)  # bool
    return payload
