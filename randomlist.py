import random
#This is function counts a interances
def same_num():    
	for x in randnum:
		global count
		if  int(neednum) == x:
			count += 1		
			
run = True	
while run == True:
	#Here is just a variables
	count = 0
	randnum = []
	s = 20
	n = random.randrange(0, 20)
	neednum = input("What num u choose?")


	#Random auto-fill  list "randnum"
	for sn in range(0, n):
	  	a= random.randrange(0, s)
	  	randnum.append(a)


	#Calls func	  
	same_num()
	  
	#Writes a result	  
	print(randnum)
	print('In list of random number,',neednum,'repeating a',count,' times')
	print("Lenth of list is ", len(randnum))
