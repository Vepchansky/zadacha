n = int(input())
g = [] 
order = []
answer = False

def search_parent(parent, child):
    global answer
    answer = False
    if parent != ":" and child != ":":
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
    order.append(child)
    n -= 1

for i in range(len(order)):
    for j in range(len(order)):
        if j > i:
            search_parent(order[i], order[j])
            if answer: 
                print(order[j])
