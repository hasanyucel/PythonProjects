# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

lst = [3,2,5,8,6,3]

lenght = len(lst)

while (lenght > 3):
    lst.pop(3)
    lenght = lenght - 1

for i in range(0, 3):
    lst.pop()

print(lst)

# w3sources answer
def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)