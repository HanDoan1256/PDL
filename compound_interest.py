def compound_interest(principal, rate, contribution, years):
  i=0
  while i<years:
    sum = (principal * (100+rate)/100) + contribution
    principal=sum
    i=i+1
  return round(sum,2)
