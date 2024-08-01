import sqlite3


class DBHelper:
    def __init__(self):
        self.def_db_conn = sqlite3.connect("gamedef.sqlite3", check_same_thread=False)
        self.user_db_conn = sqlite3.connect("db.sqlite3", check_same_thread=False)
        self.def_db_conn.row_factory = sqlite3.Row
        self.user_db_conn.row_factory = sqlite3.Row
        self.def_db_cur = self.def_db_conn.cursor()
        self.user_db_cur = self.user_db_conn.cursor()

    def get_characters(self, idx) -> dict:
        idx = str(idx)
        self.user_db_cur.execute(f'SELECT * FROM characters WHERE "index"={idx}')
        return dict(self.user_db_cur.fetchone())

    def get_equips(self, idx):
        idx = str(idx)
        self.user_db_cur.execute(f'SELECT * FROM chracterequip WHERE "index"={idx}')
        return tuple(self.user_db_cur.fetchone())

    def get_apparence(self, idx):
        idx = str(idx)
        self.user_db_cur.execute(f'SELECT * FROM chracterapparence WHERE "index"={idx}')
        return tuple(self.user_db_cur.fetchone())

    def get_item_info(self, idx):
        idx = str(idx)
        self.def_db_cur.execute(f"SELECT * FROM items WHERE idx = {idx}")
        return dict(self.def_db_cur.fetchone())

    def get_map(self, portal_code, cur_map):
        portal_code = str(portal_code)
        cur_map = str(cur_map)
        self.def_db_cur.execute(
            f"SELECT next_map_id, xpos, ypos, map_name FROM maps WHERE portal_code = {portal_code} AND current_map_id = {cur_map}"
        )
        result = self.def_db_cur.fetchone()
        if result == None:
            return None
        else:
            return dict(result)
