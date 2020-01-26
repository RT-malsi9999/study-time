#A TINY GAME BY RT-MALSI9999

import random
import sys



#says something at the end
def pr1nt():
	if att == 6:
		print("U was near death")
	elif att <= 3:
		print("GG")
	elif att > 3 and att < 6:
		print("Not bad")
	else:
		print("some shit B|")
#Function which give you tips.
def guess():
	if int(g_num) < Hidden_num:
		print("My num is bigger")
	elif int(g_num) > Hidden_num:
		print("My num is lower!")
	elif int(g_num) == Hidden_num:
		print("U did it, my number is ", g_num)
		print("guesses taken are", att, "times.")
		pr1nt()
		sys.exit()

#Random chooses a random number
Hidden_num = random.randint(0, 20)
print("I chose a num from 0 to 20, guess him!")
#A tries' player
for att in range(1,7):
	g_num = input("TRY: ")
	guess()
	if att == 6 and g_num != Hidden_num:
		print('You are lose!\nNumber was a', Hidden_num)





		
	
