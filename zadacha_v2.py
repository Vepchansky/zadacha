n = int(input())
namespace = {}
variables = {}

def create(namesp1, namesp2):
    global namespace
    if namesp2 not in namespace.keys():
        namespace[namesp2] = None
    namespace[namesp1] = namesp2

def add(namesp, var):
    global variables
    try:
        if bool(variables[namesp]): variables[namesp].add(var)
    except KeyError:
        variables[namesp] = set()
        variables[namesp].add(var)

def get(namesp, var):
    global namespace, variables
    try:
        if var in variables[namesp]:
            return namesp
        elif namespace[namesp]:
            namesp = get(namespace[namesp], var)
        else: namesp = None
    except KeyError:
        if namespace[namesp]:
            namesp = get(namespace[namesp], var)
        else: namesp = None
    return namesp

for i in range(n):
    cmd, namesp, var = input().split()
    if cmd == 'create': create(namesp, var)
    elif cmd == 'add': add(namesp, var)
    elif cmd == 'get': 
        namesp = get(namesp, var)
        print(namesp)    
