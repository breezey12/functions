def test_whether_even_or_odd(number):
	if number % 2 == 0:
		print("Even") 
	else:
		print ("Odd")

def test_whether_greater_than_ten(number):
	if number > 10:
		print("Yes")
	else:
		print("No")

def test_even_odd_greater_than_ten(number):
	even_or_odd = test_whether_even_or_odd(number)
	greater_than = test_whether_greater_than_ten(number)
	#if even_or_odd == "Odd" and greater_than == "Yes":
		#return True
	#else:
		#return False





