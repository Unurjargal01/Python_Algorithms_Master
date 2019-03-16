from collections import deque, OrderedDict

def maximum(Alpha):
    if len (Alpha) == 2 and Alpha[-1][2] == (N - 1) and Alpha[0][0] == 0:
        return 1, 0, 0
    elif Alpha[-1][2] == (N - 1) and Alpha[0][0] == 0:
        K = [Alpha[-1][0], Alpha[-1][1] + Alpha[0][1], Alpha[0][2]] 
        T = Alpha
        T.pop()
        T.popleft()
        T = list(T)
        T.append(K)
        T.sort(key = lambda x: x[1])
        maxi1, maxi2 = T[-1], T[-2]
        if K == maxi1:
            return 2, maxi1, maxi2
        else:                       # k is maxi2 ?
            return 3, maxi1, maxi2
    else:
        A = list(Alpha)
        A.sort(key = lambda x: x[1])
        maxi1, maxi2 = A[-1], A[-2] 
        return 3, maxi1, maxi2

def check(Alpha, counter, type_, maxi1, maxi2):
    if type_ == 1:
        length = Alpha[0][1] + Alpha[1][1]
        #if counter in range(Alpha[1][0], Alpha[1][2] + 1):
        if 0 <= counter <= Alpha[0][2]:
            t = Alpha[0][2] - counter + 1
            return max(t , length - t)
        elif Alpha[1][0] <= counter <= Alpha[1][2]:
            t = counter - Alpha[1][0] + 1
            return max(t, length - t) 
        else:
            return length


    elif type_ == 2:
        if  N - 1 >= counter >= maxi1[0]:
            t = counter - maxi1[0] + 1
            return max(maxi1[1] - t, t, maxi2[1])
        elif counter <= maxi1[2]:
            t = maxi1[2] - counter + 1
            return max(maxi1[1] - t, t, maxi2[1])
        else:
            return maxi1[1]


    elif type_ == 3:
        if not( maxi1[0] <= counter <= maxi1[2]):
            return maxi1[1] 
        else:
            return max(counter - maxi1[0] + 1, maxi1[2] - counter + 1, maxi2[1])

N, Q, K = map(int, input().split())
A = list(map(int, input().split()))
Task = input()

Alpha = deque() 
length = 0
starting_point = 0
for i in range(len(A)):
    if A[i] == 1:
        length += 1
    else:
        if length != 0:
            Alpha.append([starting_point, length, i - 1])
            #print(i)
        starting_point = i + 1
        length = 0
    if A[i] == 1 and i == len(A) - 1:
        Alpha.append([starting_point, length, i])

type_, maxi1, maxi2 = maximum(Alpha)


counter = N - 1
for i in Task:
    if i == '!':
        if counter == 0:
            counter = N
        counter = (counter - 1)    
    else:
        maxi = check(Alpha, counter, type_, maxi1, maxi2)
        if maxi >= K:
            print(K)
        else:
            print(maxi)