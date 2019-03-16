


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

final_array = []
for i,j in zip(A, B):
    final_array.append((i * j, i,j))

final_array.sort(reverse = True)
lower = 0
upper = final_array[0][0]
final_answer = upper

while lower <= upper:
