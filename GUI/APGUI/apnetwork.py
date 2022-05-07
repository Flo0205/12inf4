import json
import requests

class APNetwork(object):
    def __init__(self, ip: str, port: str) -> None:
        self.ip = ip
        self.port = port

    def getRoles(self) -> list:
        response = requests.get(f"http://{self.ip}:{self.port}/autoperms/roles")
        roles: list
        roles = json.loads(response.json())

        roles.remove("User")
        roles.append("None")

        return roles

    def updateUsers(self, payload) -> None:
        requests.post(f"http://{self.ip}:{self.port}/autoperms/users", json.dumps(payload))