n = int(input())
g = [] 

while n > 0:
    klass = list(map(str,input().split()))    
    g.append(klass) 
    n -= 1

print(g)
n = int(input())

while n > 0:
    parent, child = map(str, input().split())
    answer = 'No'
    if parent == child: answer = 'Yes'
    else:
        for row in g:
            if row[0] == child:
                for count in row:
                    if count == parent: answer = 'Yes'
            elif row[0] != child:
                for i in range(len(row)):
                    if i !=0 and i != 1:
                        for row2 in g:
                            if row2[0] == row[i]:
                                for count in row2:
                                    if count == parent: answer = 'Yes'
    print(answer)


    n -= 1

