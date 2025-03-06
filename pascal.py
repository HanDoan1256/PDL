def generate(numRows):
	triangle =[]
	for num in range (0,numRows):
	  row = [1]*(num+1)
	  for j in range (1,num):
	    row[j]=triangle[num-1][j-1] + triangle[num-1][j]
	  triangle.append(row)
	return triangle
