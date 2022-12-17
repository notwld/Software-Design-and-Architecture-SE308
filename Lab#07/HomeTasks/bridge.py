class Encryption:
    def encrypt(self):
        pass 

class AES(Encryption):
    def encrypt(self):
        print('Encrypting with AES')

class Blowfish(Encryption):
    def encrypt(self):
        print('Encrypting with Blowfish')

class EncryptionBridge:
    def __init__(self, encryption):
        self.encryption = encryption
    def encrypt(self):
        self.encryption.encrypt()

if __name__ == '__main__':
    aes = AES()
    blowfish = Blowfish()
    aesBridge = EncryptionBridge(aes)
    blowfishBridge = EncryptionBridge(blowfish)
    aesBridge.encrypt()
    blowfishBridge.encrypt()

