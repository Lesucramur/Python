List_1 = []
A = 0
B = 1
List_1.append(A)
List_1.append(B)

for i in range (50):
    C = B + A
    List_1.append(C)
    A = B
    B = C

print(List_1)

