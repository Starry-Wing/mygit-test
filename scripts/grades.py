

def main():
   n=int(input('enter the number of students:'))
   alldata={}
   studentdata={}
   subjects=['math','english','chinese']
   for i in range(n):
       name=str(input('enter the name of the student:'))
       for subject in subjects:
           result=int(input('enter {} result of {}:'.format(subject,name)))
           studentdata[subject]=result
       alldata[name]=studentdata.copy()
   printall(alldata)
   printgrades(alldata)

def printstudent(alldata,name):
   print(alldata[name])

def printall(alldata):
   for i in alldata:
	   print('{}:{}'.format(i,alldata[i]))

def printgrades(students):
   sum=0
   for student in students:
       for subject in students[student]:
           sum+=students[student][subject]
           #print('{}'.format(students[student][subject]))
       print('{}:{}'.format(student,sum))
       sum=0

main()

