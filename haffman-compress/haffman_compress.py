import struct

CODE_KEY = {}
FILL = 0


def compress(content):
    ret = ''
    for i in content:
        ret += CODE_KEY[i]
    return ret

def decompress(content):
    ret = ''
    temp = ''
    for i in content:
        temp += i
        if temp in CODE_KEY.values():
            ret += list(CODE_KEY.keys())[list(CODE_KEY.values()).index(temp)]
            temp = ''
    return ret


def code(content):
    resoult = {}
    for i in content:
        resoult[i] = content.count(i)
    # print(sorted(resoult.items(), key=lambda item: item[1], reverse=True))
    if resoult != '':
        while True:
            if len(resoult) == 1:
                break
            two_min = sorted(resoult.items(), key=lambda item: item[1])[:2]
            #two_min is a list
            resoult[two_min[0][0]+two_min[1][0]] = two_min[0][1]+two_min[1][1]
            for i in two_min[0][0]:
                if i in CODE_KEY:
                    CODE_KEY[i] = '0' + CODE_KEY[i]
                else:
                    CODE_KEY[i] = '0'
            for i in two_min[1][0]:
                if i in CODE_KEY:
                    CODE_KEY[i] = '1' + CODE_KEY[i]
                else:
                    CODE_KEY[i] = '1'
            del resoult[two_min[0][0]]
            del resoult[two_min[1][0]]

        print(CODE_KEY)

def main():
    global FILL, CODE_KEY
    with open("samples/my-father.txt", 'r') as file:
        txt = file.read()
        if txt != '':
            code(txt)
        comtext = compress(txt)
        byte_temp = ''
        for i in range(0, len(comtext), 8):
            if len(comtext) - i < 8:
                FILL = 8 - (len(comtext) - i)
                comtext += '0' * FILL
            # byte_temp += str(hex('%02d' % int(comtext[i:i+8], 2)))[2:]
            byte_temp += '%02x' % int(comtext[i:i+8], 2)
        # print(comtext)
        # print(byte_temp)
        print(len(comtext))
        print(len(byte_temp))
        byte_str = bytes.fromhex(byte_temp)
        with open("samples/my-father.txt.com", "wb") as file_compress:
            byte_str = bytes(str(FILL) + '\n' + str(CODE_KEY) + '\n', encoding='ascii') + byte_str
            file_compress.write(byte_str)

        with open("samples/my-father.txt.com", "rb") as file_decompress:
            FILL = int(str(file_decompress.readline(), encoding='ascii'))
            CODE_KEY = eval(str(file_decompress.readline(), encoding='ascii'))
            print(FILL)
            print(CODE_KEY)
            byte_str = file_decompress.read()
            byte_str = ''.join(['%02x' % b for b in byte_str])
            if FILL == 0:
                comtext = str(bin(int(byte_str, 16))[2:])
            else:
                comtext = str(bin(int(byte_str, 16))[2:-FILL])
            txt = decompress(comtext)
            with open("samples/my-father.txt.org", "w") as file_origin:
                file_origin.write(txt)


if __name__ == "__main__":
    main()
