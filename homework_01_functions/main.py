from datetime import datetime

def multiply(*args, multiple = 2):
  result = []
  for num in args:
    result.append(num ** multiple)
  return result

print(multiply(2, 10, 11, 50))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def determine_numbers(numbers, type):
  result = []
  for num in numbers:
    if type == 'even':
      if num % 2 == 0:
        result.append(num)
    elif type == 'odd':
      if num % 2 != 0:
        result.append(num)
    elif type == 'simple':
      if is_prime(num):
        result.append(num)
  return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(determine_numbers(numbers, 'even'))
print(determine_numbers(numbers, 'odd'))
print(determine_numbers(numbers, 'simple'))

def time_check(func):
  def wrapper(*args):
    start_time = datetime.now()
    result = func(*args)
    print(datetime.now() - start_time)
    return result
  return wrapper
  
@time_check
def useless(range_number):
  result = []
  for n in range(range_number):
    result.append(n)

print(useless(1000))