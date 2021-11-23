#define _bool unsigned char // Even it's bool, it use 1 byte.
#define _8c unsigned char
#define _16c unsigned short
#define _16u unsigned short
#define _32u unsigned int
#define _32l unsigned long // I don't know whats difference between _32i and _32l
#define _32i int
#define _64i long long
#define _64u unsigned long long

struct _03_CHANGE_MAP_STRUCT
{
  _8c   opcode;
  _8c   must_be_one;
  _16u  map_code
  _32u  unk1;
  _64i  Gold;

  _32u  unk2; // Maybe cash
  _32u  fame; // 명성점수
  _32u  winnie; // 위니
  _32u  battle_win_count;
  _32u  battle_lose_count;
  _32u  battle_ko_count;
  _32u  battle_down_count;
  
  _bool unk3;

  _32u  pos_x; // 캐릭터 위치

  // Maybe this must be happen
  if pox_x {
    _str(17)  unk4;
    _8c       pos_y;
  }

  _8c  unk5;

  for (int i=0; i < 5; i++) {
    _16s  unk6;
  }
  for (int i=0; i < 5; i++) {
    _8s  unk7;
  }

  _8c  equipment_slot_count;
  _8c  consumable_slot_count;
  _8c  others_slot_count;
  _8c  unk8; // Maybe cash_slot_count

  // I don't know this loop count
  for (int i=0; i < v803; i++) {
    _16s  unk9;
    _8c   unk10;
  }

  // memset(unk11, 0, 0x5A);
  // memset(unk12, 0, 0x21C);

  _8c   equip_item_count;
  for (int i=0; i < equip_item_count; i++) {
    _16s  equip_item_id;
    _8c   equip_item_option_count;
    for (int j=0; j < equip_item_option_count; j++) {
      _16s  equip_item_option_id;
    }
    _16s  unk11;      // 아이템 개수?
  }

  // memset(unk11, 0, 0x5A);
  // memset(unk12, 0, 0x5A);

  _8c  consumable_item_count;
  for (int i=0; i < consumable_item_count; i++) {
    _16s  consumable_item_id;
    _16s  consumable_item_count;    // 아이템 개수
  }

  // memset(unk11, 0, 0x5A);
  // memset(unk12, 0, 0x2D);

  _8c  others_item_count;
  for (int i=0; i < others_item_count; i++) {
    _16s  others_item_id;
    _8s   others_item_count;   // 아이템 개수
  }

  _32u  event_play_time;   // Not much necessary


};