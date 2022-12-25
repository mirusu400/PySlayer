

class Maps:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("maps :: __new__ is called")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_maps"):
            print("maps :: __init__ is called")
            self._maps = {}

    def add_tcp_conntion_to_maps(self, connection, map_id = None):
        if map_id is None:
            map_id = connection.player.current_map
        print(f"[+] {connection} is added to map {map_id}")
        
        if map_id not in self._maps.keys():
            self._maps[map_id] = [connection]
        else:
            self._maps[map_id].append(connection)

    def get_tcp_connections_in_map(self, map_id):
        return self._maps[map_id]

    def change_map(self, connection, before_map_id, after_map_id):
        self._maps[before_map_id].remove(connection)
        if after_map_id not in self._maps.keys():
            self._maps[after_map_id] = [connection]
        else:
            self._maps[after_map_id].append(connection)