from nacl.signing import SigningKey, VerifyKey
from nacl.hash import blake2b
from nacl.secret import SecretBox as SB
from nacl.encoding import URLSafeBase64Encoder, RawEncoder, HexEncoder
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
        self.sign_key = SigningKey
        self.verify_key = VerifyKey

    def hash(self, message):
        """
        convert message to bytes
        make blake2b bytes object from encoded message
        convert to URLsafe string
        remove ending "=" if there is one after decoding bytes output then return
        """
        return (
            URLSafeBase64Encoder.encode(
                blake2b(
                    bytes(message, encoding="utf8"), digest_size=32, encoder=RawEncoder
                )
            )
            .decode()
            .rstrip("=")
        )

    def sign(self, encrypted_message):
        return self.sign_key.sign(
            blake2b(
                bytes(encrypted_message, encoding="utf8"),
                digest_size=32,
                encoder=RawEncoder,
            )
        ).signature.hex()

    def verify(self, verify_key, encrypted_message):
        try:
            verify_key.verify(encrypted_message, encoder=HexEncoder)
            return True
        except:
            return False

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
