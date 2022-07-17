from server_packets import opcode_02, opcode_03, opcode_07, opcode_08, opcode_18
from server_packets import opcode_28, opcode_44, opcode_2E, opcode_14, opcode_3B
from server_packets import opcode_25, opcode_1A
from client_packets import parse_7E
from .maps import Maps
import json

m = Maps()

class Player():
    def __init__(self, cinfo, apparences, equips):
        self.ip = ""
        self.level = cinfo["level"]
        self.uid = cinfo["index"]
        self.character_name = cinfo["charactername"]
        self.current_map = cinfo["mapcode"]
        self.str = cinfo["str"]
        self.dex = cinfo["dex"]
        self.int = cinfo["int"]
        self.tol = cinfo["tol"]
        self.job1 = cinfo["job1"]
        self.job2 = cinfo["job2"]
        self.xpos = cinfo["xpos"]
        self.ypos = cinfo["ypos"]
        self.hp = cinfo["hp"]
        self.mp = cinfo["mp"]
        self.max_hp = 0
        self.max_mp = 0
        self.apparences = apparences[1:]
        self.equips = equips[1:]
        self.skills_list = [
            # Default skillsets
            80, 82, 86, 88, 90, 94, 194, 
            2175, 2186, 2188
        ]
        self.mob_pos_list = []
        self.mob_idx = 0x000F0000

        self.set_max_hp()
        self.set_max_mp()

    def set_max_hp(self):
        # hp offset, lev offset, tol offset 순서
        hp_list = []
        if self.job1 == 1: # 전사
            hp_list = [270, 6, 12]
        elif self.job1 == 2: # 무도가
            hp_list = [220, 5, 12]
        elif self.job1 == 3: # 궁수
            hp_list = [165, 4, 12]
        elif self.job1 == 4: # 도적
            hp_list = [165, 3, 13]
        elif self.job1 == 5: #마법사
            hp_list = [110, 6, 14]
        elif self.job1 == 6: # 사제
            hp_list = [110, 5, 14]
        else: #초보여행자
            hp_list = [110, 2, 10]
        hp_offset, hp_level_offset, hp_tol_offset = hp_list
        self.max_hp = (self.level * hp_level_offset) + hp_offset + (self.tol * hp_tol_offset)
        return

    def set_max_mp(self):
        # mp offset, lev offset, int offset 순서
        mp_list = []
        if self.job1 == 1: # 전사
            mp_list = [110, 1, 9.1]
        elif self.job1 == 2: # 무도가
            mp_list = [80, 1, 9.8]
        elif self.job1 == 3: # 궁수
            mp_list = [122, 1, 9.1]
        elif self.job1 == 4: # 도적
            mp_list = [120, 4, 8.4]
        elif self.job1 == 5: # 마법사
            mp_list = [200, 2, 7]
        elif self.job1 == 6: # 사제
            mp_list = [200, 2, 7]
        else: #초보여행자
            mp_list = [80, 2, 7]
        mp_offset, mp_level_offset, mp_int_offset = mp_list
        self.max_mp = (self.level * mp_level_offset) + mp_offset + (self.int * mp_int_offset)
        return

    def add_mob(self, mob_id, xpos, ypos):
        self.mob_pos_list.append({
            "mob_id": mob_id,
            "xpos": xpos,
            "ypos": ypos})
        self.mob_idx += 0x000F0000 + len(self.mob_pos_list)
        return opcode_1A(mob_id, self.mob_idx, xpos, ypos)
    
    def dump_mob(self):
        with open(f"./maps/{self.current_map}.json", "w", encoding="utf-8") as f:
            json.dump(self.mob_pos_list, f, ensure_ascii=False, indent=4)
        return
    
    def load_mob(self) -> bytes:
        ops = []
        self.mob_pos_list = []
        try:
            with open(f"./maps/{self.current_map}.json", "r", encoding="utf-8") as f:
                self.mob_pos_list = json.load(f)
        except FileNotFoundError:
            print("No mob file found")
            pass
        for idx, mob in enumerate(self.mob_pos_list):
            ops.append(opcode_1A(mob["mob_id"], (self.mob_idx + idx), mob["xpos"], mob["ypos"]))
        return ops

    def add_stats(self, stat_type):
        payload = b""
        if stat_type == 0:
            self.str += 1
            payload += opcode_14(self.uid, 0, self.str)
        elif stat_type == 1:
            self.dex += 1
            payload += opcode_14(self.uid, 1, self.dex)
        elif stat_type == 2:
            self.int += 1
            payload += opcode_14(self.uid, 2, self.int)
        elif stat_type == 3:
            self.tol += 1
            payload += opcode_14(self.uid, 3, self.tol)
        self.set_max_hp()
        self.set_max_mp()
        print("Stats:", self.str, self.dex, self.int, self.tol)
        return payload

    def get_set_maxhp_and_maxmp_packets(self):
        return opcode_25(500)

    def get_usebuffskill_packet(self, skillid, time):
        return opcode_3B(skillid, self.uid, time)

    def get_respawn_packet(self):
        # Send opcode 04
        return opcode_2E(self.character_name, self.job1, self.job2, self.str, self.dex, self.int, self.tol, self.level,
            self.hp, self.mp, self.equips, self.apparences, self.xpos, self.ypos)

    def get_username(self):
        return self.character_name

        
    def get_welcome_packet(self):
        # Send opcode 02
        return opcode_02(self.uid, self.character_name, self.apparences)

    def get_ingame_packet(self):
        # Send opcode 03
        return opcode_03(self)
    
    def get_spawn_packet(self, my_tcp_connection):
        # Send opcode 07
        self.mob_pos_list = []
        tcp_connections_list = m.get_tcp_connections_in_map(self.current_map)
        p1 = opcode_07(tcp_connections_list, my_tcp_connection)
        # p2 = opcode_25(300)
        p3 = self.get_spawn_skills()
        p4 = self.load_mob()

        return [p1, p3, p4]
    
    def get_spawn_skills(self) -> bytes:
        payload = []
        for i in self.skills_list:
            payload.append(opcode_18(i, 1))
        return payload

    def get_changemap_packet(self) -> bytes:
        # Send opcode 08
        return opcode_08(self.current_map, self.uid)

    def add_skill(self, skillid):
        self.skills_list.append(skillid)

    def set_current_map(self, map_code, xpos, ypos):
        self.current_map = map_code
        self.xpos = xpos
        self.ypos = ypos
    
    def set_delta_hp(self, hp):
        self.hp = min(self.hp + hp, self.max_hp)
        p1 = opcode_28(self.hp)
        return p1
    
    def set_delta_mp(self, mp):
        self.mp = min(self.mp + mp, self.max_mp)
        p1 = opcode_44(self.mp)
        return p1

    def get_apparence(self):
        return self.apparences

    def get_equips(self):
        return self.equips

