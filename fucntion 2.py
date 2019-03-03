GradesList = [60,70,80,90,100,100,5,28, 30];
 # index      0   1  2  3  4   5  6  7   8 

def averageGrade(value1, value2, value3, value4, value5, value6,value7,value8, value9,total_Amount_Of_Grades):
   #PEMDAS
   average = (value1+value2+value3+value4+value5+value6+value7+value8+value9)/total_Amount_Of_Grades; 


   #print(average)

   return average; 

print(averageGrade(GradesList[0], 
	               GradesList[1], 
	               GradesList[2],
	               GradesList[3],
	               GradesList[4],
	               GradesList[5], 
	               GradesList[6], 
	               GradesList[7],
	               GradesList[8],
	               len(GradesList)  	               
	               )); 



