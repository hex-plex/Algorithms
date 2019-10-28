def maximum(*a):
	ma=a[0]
	for i in a:
		if(i>ma):ma=i
	print("the maximum value is "+str(ma))
	
		
maximum(1,6,7,2,9)
maximum(4,0,8,2,9)
