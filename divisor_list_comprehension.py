
#DIVISOR:
#The first check to be performed has to be that for number 0. If a user provided incorrect input, the program can be terminated,
#if the divisor is correct, we can iterate the range of integers and check, whether the remainder of each number divided by divisor is zero,
#if it is, then we want to collect this number into our result variable

start = int(input('Write your starting number: '))
stop = int(input('Write your stop number: '))
divisor = int(input('Write your divisor number: '))
result = []
if divisor:
	result = [num for num in range(start,stop+1) if num % divisor == 0]
	print('Numbers in range(' + str(start) +', ' + str(stop) + ') divisible by ' + str(divisor) + ':')
	print(result)
else:
	print('Can not divide by zero')




