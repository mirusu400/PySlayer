from server_packets import opcode_02, opcode_03, opcode_07, opcode_08, opcode_18
from server_packets import opcode_28, opcode_44, opcode_2E, opcode_14, opcode_3B
from server_packets import opcode_25, opcode_99, opcode_61, opcode_91, opcode_0A, opcode_1A
from server_packets import opcode_custom
from client_packets import parse_7E
from external_proc import *
from plugin.player import Player
from plugin.maps import Maps

m = Maps()

class Custom_CMD:
    def __init__(self, player=None, connection=None):
        self.player: Player = player
        self.connection = connection
        return

    def set_player(self, player):
        self.player = player

    def get_chatting_cmd(self, chat) -> bytes:
        cmd = chat.split(" ")[0]
        if cmd == "item":
            try:
                item, count = map(int,chat[4:].split(" "))
                return opcode_18(item, count)
            except:
                return None
        elif cmd == "map":
            try:
                payload = []
                map_id = int(chat.split(" ")[1])
                
                m.change_map(self.connection, self.player.current_map, map_id)

                self.player.set_current_map(map_id, 500, 500)
            
                payload.append(self.player.get_changemap_packet())
                payload.append(self.player.get_spawn_packet(self.connection))
                return payload
            except:
                print("[-] Wrong Map Code")
                raise
                return None
        elif cmd == "pos":
            try:
                self.set_internal_pos(float(chat.split(" ")[1]), float(chat.split(" ")[2]))
                return None
            except:
                return None

        elif cmd == "getpos":
            return self.get_internal_pos(chat)

        elif cmd == "mob":
            try:
                npcidx = int(chat.split(" ")[1])
                payload = self.get_internal_pos("mob", npcidx)
                return payload
            except Exception as e:
                print(e)
                return None
        
        elif cmd == "dumpmob":
            self.player.dump_mob()
            return opcode_91("Dump done!")
        
        elif cmd == "loadmob":
            return self.player.load_mob()


        
            
    
    def get_custom_cmd_packet(self, cmd) -> bytes:
        """
        Getting cmds, return payload(packets)
        """
        cmd = cmd.strip()
        payload = None
        if cmd == "item":
            item = int(input("item code?"))
            count = int(input("count?"))
            payload = opcode_18(item, count)

        elif cmd == "map":
            payload = []
            map = int(input("map code?"))
            self.player.set_current_map(map, 500, 500)
            payload.append(self.player.get_changemap_packet())
            payload.append(self.player.get_spawn_packet(self.connection))

        elif cmd == "mp":
            mp = int(input("mp?"))
            payload = opcode_44(mp)

        elif cmd == "hp":
            hp = int(input("hp?"))
            payload = opcode_28(hp)

        elif cmd == "superman":
            payload = opcode_99(0x13)
        elif cmd == "supermode":
            payload = opcode_99(0x14)
        elif cmd == "chat":
            payload = opcode_61()
        elif cmd == "chat2":
            payload = opcode_91()
        elif cmd == "chat3":
            chat = input("chat?")
            username = input("username?")
            payload = opcode_0A(chat, username)
        elif cmd == "deathmob":
            item = int(input("mob code?"))
            return
        elif cmd == "mob" or cmd == "getpos":
            return self.get_internal_pos(cmd)
        
        elif cmd == "custom":
            try:
                opcode = int(input("opcode? (In hex)"), 16)
                datatype = input("datatype? (Space between)").split(" ")
                data = input("data? (Space between)\nIf you want to type str, specify [str(length)] format.").split(" ")
                try:
                    payload = opcode_custom(opcode, datatype, data)
                    print(payload)
                    print(len(payload))
                except:
                    print("[-] Wrong Data")
                    return None
            except Exception as e:
                print(f"[-] Wrong Data: {str(e)}")
                return None
        else:
            print("[-] Undefined Opcode")
            return None
        return payload
    
    def get_internal_pos(self, cmd, npcidx = 0) -> bytes:
        if not (cmd == "mob" or cmd == "getpos"):
            return None
        try:
            with ExtProcess.ctx_open("WindSlayer.exe") as Proc:
                
                Position = Proc.make_ptr(0x00572590, PtrType.Uint32)\
                            .go_ptr(0xFD0)\
                            .go_ptr(0x13E0)
                CharX = Proc.read.double(Position.get_address())
                CharY = Proc.read.double(Position.get_address() + 0x90)
                if cmd == "mob":
                    payload = self.player.add_mob(npcidx, CharX, CharY)
                elif cmd == "getpos":
                    payload = opcode_91("[Console Message] CharX : {X}, CharY : {Y}".format(X = CharX, Y = CharY))
                    print("[Console Message] CharX : {X}, CharY : {Y}".format(X = CharX, Y = CharY))
                return payload
        except Exception as e:
                print("[-] Except : ", type(e))
                print(e)
                return None

    def set_internal_pos(self, x, y):
        try:
            with ExtProcess.ctx_open("WindSlayer.exe") as Proc:
                
                Position = Proc.make_ptr(0x00572590, PtrType.Uint32)\
                            .go_ptr(0xFD0)\
                            .go_ptr(0x13E0)
                Proc.write.double(Position.get_address(), x)
                Proc.write.double(Position.get_address() + 0x90, y)
                return
        except Exception as e:
                print("[-] Except : ", type(e))
                return None