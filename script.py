#!/usr/bin/python3
import sys

class PRNG:
    def __init__(self):
        self.state = 0x12345

    def next(self):
        self.state = (self.state * 0xdeadbeef + 0xbaad) & 0xffffffff
        return self.state % 0xff

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
    else:
        with open(sys.argv[1], "rb") as f:
            data = f.read()

        a = PRNG()
        b = bytes([x ^ a.next() for x in data])

        for x, y in [((z & 0xf), ((z >> 4) & 0xf)) for z in b]:
            print(x, y, end=' ')
        
if __name__ == '__main__':
    main()