def total_letters(N):
  word_count = {
        1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 
        7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 
        12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 
        17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 
        40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 
        90: 6,
    }
  total=0
  for i in range (1,N+1):
    if i in word_count:
      total+= word_count[i]
    elif i<100:
      total += word_count[(i // 10) * 10] + word_count[i % 10]
    else:
      total += word_count[i // 100] + 7
      if i % 100 != 0:
        total += 3
        if i % 100 in word_count:
          total += word_count[i % 100]
        else:
          total += word_count[(i % 100) // 10 * 10] + word_count[i % 10]
     
    i+=1
  return total
