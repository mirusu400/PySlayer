import sqlite3

class DBHelper():
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.db_conn.row_factory = sqlite3.Row
        self.db_cur = self.db_conn.cursor()

    
    def get_characters(self, idx) -> dict:
        idx = str(idx)
        self.db_cur.execute(f'SELECT * FROM characters WHERE "index"={idx}')

        return dict(self.db_cur.fetchone())

    def get_equips(self, idx):
        idx = str(idx)
        self.db_cur.execute(f'SELECT * FROM chracterequip WHERE "index"={idx}')
        return tuple(self.db_cur.fetchone())
    
    def get_apparence(self, idx):
        idx = str(idx)
        self.db_cur.execute(f'SELECT * FROM chracterapparence WHERE "index"={idx}')
        return tuple(self.db_cur.fetchone())

    def get_item_info(self, idx):
        idx = str(idx)
        self.db_cur.execute(f"SELECT * FROM items WHERE idx = {idx}")
        return dict(self.db_cur.fetchone())
    
    def get_map(self, portal_code, cur_map):
        portal_code = str(portal_code)
        cur_map = str(cur_map)
        self.db_cur.execute(f"SELECT next_map_id, xpos, ypos, map_name FROM maps WHERE portal_code = {portal_code} AND current_map_id = {cur_map}")
        result = self.db_cur.fetchone()
        if result == None:
            return None
        else:
            return dict(result)