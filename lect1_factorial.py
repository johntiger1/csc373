
# Computes a^x
def factorial(a,x):
	if (x==1):
		return a;
	return a*factorial(a,x-1)



#print(factorial(12,10))

def quick_pow(a,x):
	x = int(x)
	if (x == 1):
		return a;

	r = quick_pow(a,x/2); #note that  // explicitly refers to integer divison, so we could use that too
	r = r*r;
	if (x % 2 == 1):
		r = r*a
	return r;
	
print(quick_pow(12,10))