
fib1 = 1
fib2 = 2

sum = 2

def next_fib():
  global fib1
  global fib2
  
  next_num = fib1  + fib2
  
  fib1 = fib2
  fib2 = next_num
  
  return next_num
  
while fib2 < 4000000:
  value = next_fib()

  if value % 2 == 0:
    sum += value

print(sum)

input("Press any key...")