class Base64:
    def __init__(self):
        self.table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def encode(self, text):
        bins = str()
        for i in text:
            bins += bin(ord(i))[2:].zfill(8)
        bins += "0" * (6 - len(bins) % 6)


    def decode(self, data):
        return base64.b64decode(data)