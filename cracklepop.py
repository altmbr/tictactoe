dividesby3 = False
dividesby5 = False

i = 1
while i <=100:

	if int(i/3)==i/3.0:
	 dividesby3 = True

	if int(i/5)==i/5.0:
	 dividesby5 = True

	if (dividesby3 and dividesby5):
	 print "%d CracklePop" % i
	elif dividesby3:
	 print "%d Crackle" % i
	elif dividesby5:
	 print "%d Pop" % i

	dividesby3 = False
	dividesby5 = False

	i+=1
