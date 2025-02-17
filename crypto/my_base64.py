class Base64:
    def __init__(self):
        self.table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    def encode(self, text) -> str:
        bins = str()
        for i in text:
            bins += str(bin(ord(i)))[2:].zfill(8)

        if len(bins) % 6 != 0:
            bins += "0" * (6 - len(bins) % 6)

        bins = [bins[i:i + 6] for i in range(0, len(bins), 6)]
        bins = [int(i, 2) for i in bins]

        len(text) % 3 == 1 and bins.extend([64, 64])
        len(text) % 3 == 2 and bins.append(64)

        return "".join([self.table[i] for i in bins])


    def decode(self, data):
        bins = str()
        for i in data:
            if i == "=":
                continue
            bins += str(bin(self.table.index(i)))[2:].zfill(6)

        bins = bins[:len(bins) - len(bins) % 8]

        bins = [bins[i:i + 8] for i in range(0, len(bins), 8)]

        return "".join([chr(int(i, 2)) for i in bins])

# print(Base64().encode("1234"))
print(Base64().decode("MTIzNA=="))