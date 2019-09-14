List_1 = []
def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n-1) + fib(n-2)


for i in range(20):
	List_1.append(fib(i))
	
	
print(List_1)