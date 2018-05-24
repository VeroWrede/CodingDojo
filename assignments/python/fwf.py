from random import randint

# def odd_even(num):
# 	for n in range(1,num + 1):
# 		if n % 2 == 0:
# 			oddity = 'even'
# 		else:
# 			oddity = 'odd'
# 		print('num: ', n, ' -> ', oddity )

# odd_even(5)

def multiply(lst, num):
	idx = 0
	while idx < len(lst):
		temp = lst[idx] * num
		lst[idx] = temp
		idx += 1
	return lst

myArr = multiply([1,2,3], 5)

print(myArr)


def layered_multiples(arr):
	result =[0] * len(arr)
	for num in range(len(arr)):
		result[num] = [1] * arr[num]
	return result

print(layered_multiples(myArr))

print(randint(5,15))