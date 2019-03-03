numberOfBooks = 5000; 
numberPoints = 0;

if(numberOfBooks <= 100):

	print("You cannot sell books yet sorry");

	if(numberPoints == 0):

		print("Sorry you will not make any money because you can't sell any books on a site" ); 


elif(numberOfBooks >= 100 and numberOfBooks <= 1000):
	# amazon 
	print("You have 100 books you can start selling them now on Amazon.com"); 

	if(numberPoints == 100): 

		print("you get 100 dollars for every book you  sell" ); 

	
elif(numberOfBooks >= 1000 and  numberOfBooks <= 10000):

	# Ebay
	print("You have 100 books you can start selling them now on Ebay.com"); 

	if(numberPoints == 500): 

		print("you get 500 dollars for every book you  sell" ); 
else: 

	print("you have too many books to sell"); 


''''
if(numberOfBooks == 1000):
	# Ebay
	print("You have 100 books you can start selling them now on Ebay.com"); 

'''