GradesList = [60,70,80,90,100,100,5,28, 30,100,100,100,9];
 # index      0   1  2  3  4   5  6  7   8 

def averageGrade(Gradelist):

	average = 0; 

	for x in range(0,len(Gradelist)):

		average += Gradelist[x];

	
	average = average/len(Gradelist); 


	return average; 

print(averageGrade(GradesList)); 



