'''
#if statements

x = 180
y = 150

if x == y:
	print('That\'s great')
	
elif x < y:
	print('Yeah, now it\'s correct')

else:
	print("What a pity")
	
	
#Now, for some for statements. Haha.
	
for i in range(1,11):
	print("We're still going!")
else:	
	print("Well, now it's over.")
	
	


#while isn't a bad thing either.

i = 10
while i != 1:
	print("Hey, you still have to wait")
	i -= 1
	
print("We're done!")
	

#let's dot some functions!
def example():
	print("This is a function")
	
def simple_addition(n1,n2):
	answer = n1 + n2
	print("the answer is",answer)
	
simple_addition(3,4)


#writing, appending, reading...

appendMe = "\nNew bit of Information"

appendFile = open("example.txt","a")
appendFile.write(appendMe)
appendFile.close()


readMe = open("example.txt","r").readlines()

print(readMe)



#now, classes.

class calculator:

	def addition(x,y):
		added = x + y
		print(added)
	
	def subtraction(x,y):
		sub = x - y
		print(sub)
	
	def multiplication(x,y):
		mult = x * y
		print(mult)
	
	def division(x,y):
		div = x / y
		print(div)
		
calculator.division(1435,65)


#Let's put something in an input, hoho.

x = input("'the fuck are you doing? ")
print(x,"is stupid")


#Statistics module.

import statistics

list = [2,4,35,2,23,1,2,1,1,898,23,2,1,6]

x = statistics.stdev(list)

print(x)



#Lists vs. Tuples

x = 4,3,2,1	#that's a tuple
y = [4,3,2,1] #and that's a list!

print(x[2])



x = [1,2,3,4]

x.append(5)
x.insert(0,0)
print(x[3])
print(x)



x = [[[5,6],[8,3]],[1,3]]

print(x[0][1][1])


# How to open CSV files

import csv

with open('avxs.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ",")
	
	dates = []
	prices = []
		
	for row in readCSV:
		date = row[0]
		price = row[4]
		
		dates.append(date)
		prices.append(price)
		
	whatDate = input('For what date do you want to know AVXS\'s stock price?')
	
	if whatDate in dates:
		dateIndex = dates.index(whatDate)
		requestedPrice = prices[dateIndex]
		print('The stock price on',whatDate,'was:',requestedPrice)
	else:
		print("ERROR: Either the date was spelled incorrectly, or this date is not in the dataset.")





#now, let's work with dictionaries.

exDict = {'Marcus':[23,'brown'], 'Eva':[21, 'Red'], 'Toni':[64, 'Brown']}

print(exDict['Eva'][1])

exDict['Tim'] = 12
print(exDict)

del exDict['Tim']

print(exDict)



#built in modules 

exNum1 = -5
exNum2 = 5

print(abs(exNum1))

if abs(exNum1) == abs(exNum2):
	print ("They are the same")

exList = [1,2,4,5,2,4]
print(min(exList))

x = 2.2124
print(round(x))

intMe = '44'
print(intMe)
intMe = float(intMe)
print(intMe)
'''

