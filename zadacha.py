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

def getvar(parent, vari, namesp, papa):
    for sp in namesp:
        if type(sp) == type({}):
            for key in sp:
                if key != parent:
                    papr = getvar(parent, vari, sp[key], key)
                    if papr != None:
                        papa = papr
                else:
                    for i in sp[key]:
                        if i == vari:
                            papa = parent
                    return papa
        else:
            if sp == vari:
                pass
            else: papa = None
    return papa
              

for i in range(n):
    papa = None
    cmd, namesp, variab = input().split()
    if cmd == 'create': create(namesp, variab, g)
    elif cmd == 'add': addvar(namesp, variab, g)
    elif cmd == 'get': 
        papa = getvar(namesp, variab, g, papa)
        print(papa)
    else: print('Недопустимый ввод')
    print(g)
