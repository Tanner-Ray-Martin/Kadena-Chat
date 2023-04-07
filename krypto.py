from nacl.signing import SigningKey, VerifyKey
from nacl.hashlib import blake2b
from nacl.secret import SecretBox as SB
import json


class Krypto:
    def __init__(
        self,
        keyset: dict = None,
        public_key: str = None,
        private_key: str = None,
        name: str = None,
        password: str = None,
        save: bool = True,
    ) -> None:
        self.keyset = keyset
        self.public_key = public_key
        self.private_key = private_key
        self.name = name
        self.password = password
        self.save = save

    def hash(self, message):
        pass

    def sign(self, public_key, encrypted_message):
        pass

    def verify(self, public_key, encrypted_message):
        pass

    def loadKeysFromFile(self, name):
        with open("keys.json", "r") as fp:
            keys = json.load(fp)

        try:
            keyset = keys[name]
        except:
            raise KeyError

        public_key = keyset["public"]
        encrypted_private_key = keyset["private"]

        private_key = self.decryptMessage(encrypted_private_key)

        return {name: {"public": public_key, "private": private_key}}

    def saveKeysToFile(self, keyset: dict = None):
        with open("keys.json", "r") as fp:
            all_keys = json.load(fp)

        for name, keys in keyset.items():
            public_key = keys["public"]
            private_key = keys["private"]

            encrypted_private_key = self.encryptMessage(private_key)

            all_keys[name] = {"public": public_key, "private": encrypted_private_key}

        with open("keys.json", "w") as fp:
            json.dump(all_keys, fp, sort_keys=True, indent=4)

    def encryptMessage(self, message):
        pass

    def decryptMessage(self, encrypted_message):
        pass
