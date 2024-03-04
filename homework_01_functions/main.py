def multiply(*args, multiple = 2):
  result = []
  for num in args:
    result.append(num ** multiple)
  return result

print(square(2, 10, 11, 50))