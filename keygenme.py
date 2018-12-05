import math
import random

def reverse(s):
    s = str(s)
    r = "" 
    for i in s: 
        r = i + r
    return r

def generate(input):
    s = 0
    out = ""

    input = str(input)
    for i in input:
        s = s + ord(i)
 
    s = int(s * math.pi / math.e) ^ 1337 ^ ord(input[1])
    out = reverse(s)
    return out

def main():
    r = (random.randrange(10000))   
    print(r)
    print(generate(r))

if __name__ == "__main__":
    main()