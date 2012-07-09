import sys

ones = {  1: 'one', 
	  2:'two', 
	  3:'three', 
	  4:'four', 
	  5:'five', 
	  6:'six', 
	  7:'seven', 
	  8:'eight', 
	  9:'nine'   }

teens = { 11:'eleven', 
	  12:'twelve', 
	  13:'thirteen', 
	  14:'fourteen', 
	  15:'fifteen', 
	  16:'sixteen', 
	  17:'seventeen', 
	  18:'eighteen', 
	  19:'nineteen'   }

tens = {  10:'ten', 
	  20:'twenty',
	  30:'thirty', 
	  40: 'forty', 
	  50: 'fifty', 
	  60: 'sixty', 
	  70: 'seventy', 
	  80: 'eighty', 
	  90: 'ninety'   }
sum = 0
for i in range (1, 1001):

  print i 
  if i in ones:
    sum += len(ones[i])
    print ones[i]
  elif i == 10:
    sum += len(tens[i])
    print tens[i]
  elif i in teens:
    sum += len(teens[i])
    print teens[i]
  
  if len(str(i)) == 2 and i > 19:
    if i in tens:
      sum += len(tens[i])
      print tens[i]
    else:
      temp_num = str(i)[:1]
      temp_num += '0'
      sum += len(tens[int(temp_num)])
      print tens[int(temp_num)], ones[int(str(i)[-1:])]
      sum += len(ones[int(str(i)[-1:])])

  if len(str(i)) == 3:
    sum += len(ones[int(str(i)[:1])])
    sum += len('hundred') 
    print ones[int(str(i)[:1])], 'hundred'
    
    if str(i)[1] == '0' and i % 100 != 0:
      sum += len('and')
      sum += len(ones[int(str(i)[2])]) 
      print 'and', ones[int(str(i)[2])]
    
    elif int(str(i)[-2:]) in tens:
      sum += len('and')
      sum += len(tens[int(str(i)[-2:])]) 
      print 'and', tens[int(str(i)[-2:])]
    elif int(str(i)[-2:]) in teens:
      sum += len('and')
      sum += len(teens[int(str(i)[-2:])])
      print 'and', teens[int(str(i)[-2:])] 
    elif i % 100 != 0:
      temp_num = str(i)[1]
      temp_num += '0'
      sum += len('and')
      sum += len(tens[int(temp_num)])
      print 'and', tens[int(temp_num)], ones[int(str(i)[-1:])]
      sum += len(ones[int(str(i)[-1:])])
     
if i == 1000:
  sum += len('onethousand')
  print 'one thousand'
print sum
