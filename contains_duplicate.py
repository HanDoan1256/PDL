def contains_duplicate(input)-> bool:
  list = set(input)
  if len(list) != len(input):
    return True
  else: 
    return False

