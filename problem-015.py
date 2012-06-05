import math

rows = 20
columns = 20
  
routes = math.factorial(rows + columns)/(math.factorial(rows)*math.factorial(columns))
	 
print routes
