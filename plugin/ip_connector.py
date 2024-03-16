import json


class Ip_Connector:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("Ip_connetor :: __new__ is called")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_ip_connector"):
            print("Ip_connetor :: __init__ is called")
            with open("ip_info.json", "r", encoding="utf-8") as f:
                self._ip_connector = json.load(f)

    def get_index_from_ip(self, ip):
        if str(ip) in self._ip_connector.keys():
            return self._ip_connector[str(ip)]
        else:
            return "1"
