
all_opcode = []
for i in ["./Full_Packet.c", "Packet_handler_1.c", "Packet_handler_2.c", "Packet_handler_3.c", "Packet_handler_4.c"]:
    tx_list = []
    with open(i, "r", encoding="utf-8") as f:
        for line in f:
            if line[0:8] == "    case":
                a = (line.strip().replace("\\n","").split("u")[0].split(":")[0].replace("case ",""))
                if a[0:2] != "0x":
                    a = "0x" + a
                a = int(a, 16)
                tx_list.append(a)
                all_opcode.append(a)
    print()
    print(f"{i}: {len(tx_list)}")
    idx = 0
    for j in tx_list:
        print(hex(j), end=" ")
        idx += 1
        if idx == 8:
            print()
            idx = 0
all_opcode.sort()
print()
print(f"All_opcode: {len(all_opcode)}")
idx = 0
for j in all_opcode:
    print(hex(j), end=" ")
    idx += 1
    if idx == 8:
        print()
        idx = 0