import sys
filename = 'L1n4.txt'

def fiboGen(n):
    a, b = 1, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1

def main(n = int(open(filename, 'r').read())):
    for x in fiboGen(n):
        print(x)

if __name__ == '__main__':
    try:
        if '-f' in sys.argv:
            filename = sys.argv[sys.argv.index('-f') + 1]
    except:
        filename = 'L1n4.txt'
    main()
        
with open(filename, 'r') as f:
	    n = int(f.read())
