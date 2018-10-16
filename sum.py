div = 0
sum = 0

startnum = int(input("Start at: "))
endnum = int(input("End at: "))
divisor = int(input("Divisor: "))

for i in range(startnum, (endnum + 1)):
	if i % divisor == 0:
		sum += i
		div += 1
	
print("Sum: {}\n# of integers added: {}".format(sum, div))
