
# Computes a^x
def factorial(a,x):
	if (x==1):
		return a;
	return a*factorial(a,x-1)

print(factorial(12,2))

