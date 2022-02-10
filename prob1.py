s = int(input())
matrix=[]
# For user input
for i in range(s):          # A for loop for row entries
    a =[]
    for j in range(s):      # A for loop for column entries
        a.append((input().split(",")))
    matrix.append(a)
for i in range(s):
    for j in range(s):
        print(matrix[i][j], end = " ")
    print()
