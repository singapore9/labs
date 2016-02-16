import sys

def fiboGen(n):
    a, b = 1, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1

def main(n):
    for x in fiboGen(n):
        print(x)

if __name__ == '__main__':
    try:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', dest='filename', type=str, help='open F file')
        args = parser.parse_args()
        try:
            if args.filename:
                with open(args.filename,'r') as file:
                    num = file.read()
            else:
                num = open('L1n4.txt','r').read()
        except:
            num = ''
    except:
        num = open('L1n4.txt','r').read()
    if num:
        main(int(num))
    else:
        print('invalid data')
        
