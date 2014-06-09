#!/user/bin/pyton2.4 -tt

import sys

def Hello(name):
    if name == 'Alice' or name == 'Nick':
       name = name + '!!!'
       print 'Hello', name +'I know you!'
    else:
        print 'who are you'
    
    name = name + '???'
    print 'thanks..', name

def main():
    Hello(sys.argv[1])
    
if __name__ == "__main__":
    main()
