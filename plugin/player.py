from server_packets import opcode_02, opcode_03, opcode_07, opcode_08, opcode_18
from server_packets import opcode_28, opcode_44, opcode_2E, opcode_14, opcode_3B
from server_packets import opcode_25, opcode_1A
from client_packets import parse_7E
import json
class Player():
    def __init__(self, cinfo, apparences, equips):
        self.level = cinfo["level"]
        self.uid = cinfo["index"]
        self.charactername = cinfo["charactername"]
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
        self.apparences = apparences[1:]
        self.equips = equips[1:]
        self.skills_list = [
            # Default skillsets
            80, 82, 86, 88, 90, 94, 194, 
            2175, 2186, 2188
        ]
        self.mob_pos_list = []
        self.mob_idx = 0x000F0000

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
        print("Stats:", self.str, self.dex, self.int, self.tol)
        return payload

    def get_set_maxhp_and_maxmp_packets(self):
        return opcode_25(500)

    def get_usebuffskill_packet(self, skillid, time):
        return opcode_3B(skillid, self.uid, time)

    def get_respawn_packet(self):
        # Send opcode 04
        return opcode_2E(self.charactername, self.job1, self.job2, self.str, self.dex, self.int, self.tol, self.level,
            self.hp, self.mp, self.equips, self.apparences, self.xpos, self.ypos)

    def get_username(self):
        return self.charactername

        
    def get_welcome_packet(self):
        # Send opcode 02
        return opcode_02(self.uid, self.charactername, self.apparences)

    def get_ingame_packet(self):
        # Send opcode 03
        return opcode_03(self.current_map)
    
    def get_spawn_packet(self):
        # Send opcode 07
        self.mob_pos_list = []
        p1 = opcode_07(self.uid, self.charactername, self.job1, self.job2, self.str, self.dex, self.int, self.tol, self.level,
            self.hp, self.mp, self.equips, self.apparences, self.xpos, self.ypos)
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
        self.hp += hp
        p1 = opcode_28(self.hp)
        return p1
    
    def set_delta_mp(self, mp):
        self.mp += mp
        p1 = opcode_44(self.mp)
        return p1

    def get_apparence(self):
        return self.apparences

    def get_equips(self):
        return self.equips

