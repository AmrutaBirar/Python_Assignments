sum = 0

i = 0
j = 31
while (i<=30 and j>=1):
	#print (i,j)
	sum = sum + (i/j)
	
	i = i + 1 
	j = j - 1
	
print(format(sum,'.2f'))		
