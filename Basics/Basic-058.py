# Write a python program to find the sum of the first n positive integers.

def find_sum_integers(numbers):
    temp = 0
    for num in numbers:
        if(num>0):
            temp = temp + num
        else:
            break
    return temp

print(find_sum_integers([2,3,4,5,-1,2,3,4,5]))
print(find_sum_integers([2,3,4,5,1,2,3,4,5]))

#w3source' answer
n = 8
sum_num = (n * (n + 1)) / 2
print(sum_num)