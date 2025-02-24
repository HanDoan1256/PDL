	
baseNumbers = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C'
}

def convertToBase13(num):
  if num == 0:
    return "0"
  cvnum = ""
  a=abs(num)
  if a < 13:
    return baseNumbers[a]
  if a >= 13:
    while a>= 13:
      cvnum = baseNumbers[a%13] + cvnum
      a//=13
      
    cvnum = baseNumbers[a] + cvnum
    return cvnum if (num>0) else ("-" + cvnum)
    
