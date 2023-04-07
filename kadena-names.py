import requests

from constants import NAMES_URL, ADDRESS_URL


class KadenaNames:
    def __init__(self) -> None:
        pass

    def getAddress(self, name: str = None) -> str:
        name = f"{name}.kda" if not name.endswith(".kda") else name
        url = f"{NAMES_URL}{name}"
        return self.get(url)["address"]

    def getName(self, address: str = None) -> str:
        address = f"k:{address}" if not address.startswith("k:") else address
        url = f"{ADDRESS_URL}{address}"
        return self.get(url)["name"]

    def get(self, url: str = None) -> dict:
        resp = requests.get(url)
        return resp.json()


# mic check mic check testing testing
if __name__ == "__main__":
    KN = KadenaNames()
    addr = KN.getAddress("tanner")
    name = KN.getName(addr)
    print(name, addr)
