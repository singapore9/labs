import sys
import L1n1
import L1n2
import L1n3
import L1n4

def main(n):    
    modules = {1:L1n1.main,2:L1n2.main,3:L1n3.main,4:L1n4.main}
    if (0<n<5): modules[n]()
    else: print('Invalid \'n\'')
        
    
if __name__=='__main__':
    try:
        if '-o' in sys.argv:
            n = int(sys.argv[sys.argv.index('-o') + 1])
        else:
            raise Exception
    except Exception:
        n = int(input('Enter \'n\'[1..4]:\n'))
    main(n)
        
