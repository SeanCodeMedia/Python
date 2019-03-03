#input("Hi Welcome to our grade average program hit enter to continue")

isRunning = True; 

GradesList = [10];


while isRunning :

	inputValue = "d"#str(input(" Please enter your first grade if done \n entering grades hit d to calculate grades >>>")); 

	if(inputValue.lower() == "d"):

		isRunning = False;

		print(averageGrade(GradesList)); 

	else: 

		GradesList.append(int(inputValue));
		

input("hit enter to done !");

#print(averageGrade(GradesList)); 



def averageGrade(Gradelist):

	average = 0; 

	for x in range(0,len(Gradelist)):

		average += Gradelist[x];

	
	average = average/len(Gradelist); 


	return average; 
