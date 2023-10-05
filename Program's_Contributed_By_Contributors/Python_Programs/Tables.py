'''
wapp to print the table of a no
'''

num=float(input("enter a number: "))
mul=int(input("enter last multiple: "))
for i in range(1,mul+1):
	print(i,"*",num," = ",(i*num))
