a=120
b=12
def gcd(x,y):
	if y==0:
		return x
	else:
		return gcd(y,x%y)

print('The GCD is '+ str(gcd(a,b)))


"""
print(remainder)"""

"""while judge==0:
	igcd(a,b)
	if remainder:
		remainder=b%remainder"""