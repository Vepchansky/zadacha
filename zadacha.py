n = int(input())
g = []

def create(child, parent, namesp):
    if not bool(namesp):
        namesp.append({parent:[{child:[]}]})
    else:
        for sp in namesp:
            if type(sp) == type({}):
                for key in sp:
                    if key == parent: sp[key].append({child:[]})
                    else: create(child, parent, sp[key])            

def addvar(parent, vari, namesp):
    if not bool(namesp):
        namesp.append({parent:[vari]})
    else:
        for sp in namesp:
            if type(sp) == type({}):
                for key in sp:
                    if key == parent: sp[key].append(vari)
                    else: addvar(parent, vari, sp[key]) 

def getvar(parent, vari, namesp, papa = None):
    if not bool(namesp): return papa
    else:
        for sp in namesp:
            if type(sp) == type({}):
                for key in sp:
                    if key == parent:
                        for var in sp[key]:
                            if var == vari:
                                papa = key
                        return papa
                    else:
                        papr = getvar(parent, vari, sp[key], key)
                        if papr != None:
                            papa = papr
                        return papa
        for sp in namesp:
            if sp == vari and papa == None: 
                return papa
            else:
                papa = None
              

for i in range(n):
    papa = None
    cmd, namesp, variab = input().split()
    if cmd == 'create': create(namesp, variab, g)
    elif cmd == 'add': addvar(namesp, variab, g)
    elif cmd == 'get': 
        papa = getvar(namesp, variab, g, papa)
        print(papa)
    else: print('Недопустимый ввод')