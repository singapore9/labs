import sys
database = set()
command = ''    

def Continue():
    ans = (input('Continue? y/n\n')).lower()
    if ans == 'n':
        return False
    elif ans == 'y':
        return True
    else:
        print('Invalid answer.')
        return Continue()

def add(db, *args):
    for arg in args:
        db.add(arg)

def remove(db, arg):
    db.remove(arg)

def find(db, *args):
    for arg in args:
        if arg in db:
            print(arg, end = ' ')
    print()

def list(db):
    for arg in db:
        print(arg, end = ' ')
    print()

def grep(db, arg):
    import re
    for item in db:
        match = re.fullmatch(arg, item)
        if match:
            print(item, end = ' ')
    print()

def save(db):
    import shelve
    l = []
    for item in db: l.append(item)
    with shelve.open('infoDB.db') as f:
        f['db'] = l

def load(db):
    global database
    import shelve
    with shelve.open('infoDB.db') as f:
        db = f['db']
    database = set(db)

COMMANDS = {'add': add, 'remove': remove, 'find': find,\
		'list': list, 'grep': grep, 'save': save, 'load': load}
 
def main(commands):
    global database
    print('Hello')
    while commands:#Continue():
        #command = input('Enter command:\n')
        command, commands = commands[0], commands[1:]
        args = command.split()
        command = args[0]
        args = args[1:]
        if command in COMMANDS:
            try:
                print('command =', command,'; args =', args)
                if len(args):
                    COMMANDS[command](database, *args)
                else:
                    COMMANDS[command](database)
            except:
                print('Invalid inputdata')
            print('result=', database)
        else:
            print('Invalid command.\nUse', COMMANDS.keys())


if __name__ == '__main__':
    try:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', dest='filename', type=str, help='open F file')
        args = parser.parse_args()
        try:
            if args.filename:
                with open(args.filename,'r') as file:
                    commands = file.readlines()
            else:
                commands = open('L1n3.txt','r').readlines()
        except:
            commands = []
    except:
        commands = open('L1n3.txt','r').readlines()
    if commands:
        main(commands)
    else:
        print('invalid data')


	    
