def another_one(digits):
	a=''
	for i in digits:
	  a=a+str(i)
	b=int(a)
	b=b+1
	b=str(b)
	c=[]
	for i in range (0,len(b)):
	  c.append(int(b[i]))
	return c
