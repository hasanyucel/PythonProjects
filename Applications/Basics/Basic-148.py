# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.


def findMin(lst):
    minimum = lst[0]
    for num in lst:
        if(num < minimum):
            minimum = num
    
    return minimum

def findMax(lst):
    maximum = 0
    for num in lst:
        if(num > maximum):
            maximum = num
    
    return maximum

lst = [1,5,7,1,2,9,4,0,1]

print("Max",findMax(lst))
print("Min",findMin(lst))

# w3sources answer

def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))