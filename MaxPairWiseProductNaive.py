# number or items in array
n = int(input()) 
# array items seperated by a space
a = [int(x) for x in input().split()]

product = 0

for i in range(n): 
	for j in range(i + 1, n): 
		product = max(product, a[i] * a[j])
		
print(product)
