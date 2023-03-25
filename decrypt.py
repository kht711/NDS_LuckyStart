import struct

f = open("sc/hikage.sdt", "rb")
line = f.read()
f.close()

charList = [
    "こなた",
    "つかさ",
    "かがみ",
    "みゆき",
    "ゆたか",
    "みなみ",
    "ひかげ",
    "ひなた",
    "パティ",
    "ななこ",
    "ゆい"
]

index = 0
while index < len(line) - 1:
    readLen = line[index]
    cmd = line[index + 1]
    
    if cmd == 0x10:
        script = line[index + 4:index + readLen - 1]
        print(script.decode("shift-jis"))
    elif cmd == 0x03:
        number = struct.unpack("<h", line[index + 2:index + 4])[0]
        h2 = line[index + 4:index + readLen - 1].decode("shift-jis")
        print("【ラベル{0}】".format(number))
    elif cmd == 0x04:
        number = struct.unpack("<h", line[index + 2:index + 4])[0]
        print(" - 【ラベル{0}へ行く】\n".format(number))
    elif cmd == 0x05:
        h1 = struct.unpack("<h", line[index + 2:index + 4])[0]
        h2 = struct.unpack("<h", line[index + 4:index + 6])[0]
        print(" - 【ダメージ分岐】 {0}\n    【ラベル{1}へ行く】".format(h1, h2))
    # IF?
    elif cmd == 0x06:
        char = line[index + 2]
        if char >= len(charList):
            charName = "?"
        else:
            charName = charList[char]
        number = struct.unpack("<h", line[index + 3:index + 5])[0]
        print(" - 【キャラ分岐】 {0}\n    【ラベル{1}へ行く】".format(charName, number))
    # BATTLE IF?
    elif cmd == 0x09:
        num = line[index + 2]
        number = struct.unpack("<h", line[index + 3:index + 5])[0]
        print(" - 【バトル分岐】 {0}\n    【ラベル{1}へ行く】".format(num, number))
    # BATTLE?
    elif cmd == 0x25:
        char = line[index + 2]
        h1 = struct.unpack("<h", line[index + 3:index + 5])[0]
        print("【VS バトル】 {0}".format(charList[char]))
    index += readLen
