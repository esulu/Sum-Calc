div = 0

startnum = int(input("Start at: "))
endnum = int(input("End at: "))
divisor = int(input("Divisor: "))

for i in range(startnum, (endnum + 1), divisor):
	div += 1
	
print(div)
