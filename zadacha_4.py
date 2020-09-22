n = int(input())
g = [] 
order = []
answer = False

def search_parent(parent, child):
    global answer
    if parent == child: answer = True
    else:
        for row in g:
            if row[0] == child:
                for count in row:
                    if count == parent: answer = True 
                    elif count != ":" and count != child:
                        search_parent(parent, count)


while n > 0:
    klass = list(map(str,input().split()))    
    g.append(klass) 
    n -= 1

n = int(input())

while n > 0:
    child = input()
    for error in order:
        search_parent(error, child)
    if answer:
        order.append(child)
    n -= 1

for error in order:
    print(error)

