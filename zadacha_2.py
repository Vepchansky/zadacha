n = int(input())
g = [] 
answer = 'No'

def search_parent(parent, child):
    global answer
    if parent == child: answer = 'Yes'
    else:
        for row in g:
            if row[0] == child:
                for count in row:
                    if count == parent: answer = 'Yes'
                    elif count != ":" and count != child:
                        search_parent(parent, count)


while n > 0:
    klass = list(map(str,input().split()))    
    g.append(klass) 
    n -= 1

print(g)
n = int(input())

while n > 0:
    parent, child = map(str, input().split())
    answer = 'No'
    search_parent(parent, child)
    n -= 1
    print(answer)

