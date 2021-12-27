from server_packets import opcode_02, opcode_03, opcode_07, opcode_08, opcode_18
from server_packets import opcode_28, opcode_44
from client_packets import parse_7E

class Player():
    def __init__(self, cinfo, apparences, equips):
        self.level = cinfo["level"]
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


        
    def get_welcome_packet(self):
        # Send opcode 02
        return opcode_02(self.charactername, self.apparences)

    def get_ingame_packet(self):
        # Send opcode 03
        return opcode_03(self.current_map)
    
    def get_spawn_packet(self):
        # Send opcode 07
        return opcode_07(self.charactername, self.job1, self.job2, self.str, self.dex, self.int, self.tol, self.level,
            self.hp, self.mp, self.equips, self.apparences, self.xpos, self.ypos)
    
    def get_spawn_skills(self):
        for i in self.skills_list:
            yield opcode_18(i, 1)

    def get_changemap_packet(self):
        # Send opcode 08
        return opcode_08(self.current_map)

    def add_skill(self, skillid):
        self.skills_list.append(skillid)

    def set_current_map(self, map_code, xpos, ypos):
        self.current_map = map_code
        self.xpos = xpos
        self.ypos = ypos
    
    def set_delta_hp(self, hp):
        self.hp += hp
        return opcode_28(self.hp)
    
    def set_delta_mp(self, mp):
        self.mp += mp
        return opcode_44(self.mp)

    def get_apparence(self):
        return self.apparences

    def get_equips(self):
        return self.equips

