import student2
import hashtable
import time
gAges = 0

def InsertName(studentname):
    timetotal = 0
    t1 = time.time()
    countage = 0.0
    countgood = 0.0
    countbad = 0.0
    totalage = 0.0

    #  Insert Names
    finstudent = open("../StudentTextFiles/InsertNames.txt", "r")
    for line in finstudent:
        words = line.split()
        s = student2.Student(words[0], words[1],
                            words[2], words[3], int(words[4]))
        
        if studentname.Insert(s) == False:
            countbad += 1.0
        else:
            countgood += 1.0
            countage += 1.0
            totalage = totalage + s.getmAge()
            
    average = totalage / countage
    finstudent.close()
       
    t2 = time.time()
    timetotal = t2 - t1
    print()
    print("Insert Names:")
    print("The number of Success is " '%8.2f' %  countgood,".")
    print("The number of Failures is" '%8.2f' % countbad,".")
    print("Student's'average age is "'%8.2f' % average,".")
    print("It took "'%8.2f' %timetotal," Seconds.")


def Traverse(studentname): 
    global gAges
    timetotal = 0
    t1 = time.time()

    studentname.Traverse(addAges)
    print(gAges)
    totalsize = studentname.size()
    average = gAges/totalsize
    
    t2 = time.time()
    timetotal = t2 - t1
    print("Traversing the student list took " + '%8.2f' %  timetotal + " Seconds" )

    print("Student's'average age is " + '%8.2f' % average,". It took" '%8.2f' %  timetotal + " Seconds" )

def addAges(student):
    global gAges
    gAges += int((student.getmAge()))

def deleteNames(studentname):

    timetotal = 0
    t1 = time.time()
    count = 0
    
    countgood = 0.0
    countbad = 0.0
    
    finstudent = open("../StudentTextFiles/DeleteNames.txt", "r")

    for line in finstudent:
        ssn = line.strip()
        dummys = student2.Student("","",ssn,"",0)
        good = studentname.Delete(dummys)

        if good == False:
            countbad += 1.0
        else:
            countgood += 1.0

    t2 = time.time()
    timetotal = t2 - t1

    print()
    print("Delete Names:")
    print("The number of Success is " '%8.2f' %  countgood,".")
    print("The number of Failures is" '%8.2f' % countbad,".")
    print("It took "+'%8.2f' %timetotal + " Seconds.")

def retrievename(studentname):

    timetotal = 0
    t1 = time.time()

    countgood = 0.0
    countbad = 0.0
    totalage = 0.0
    agecount = 0.0
    
    finstudent = open("../StudentTextFiles/RetrieveNames.txt", "r")
    for line in finstudent:
        ssn = line.strip()
        dummys = student2.Student("","",ssn,"",0)
        good = studentname.Retrieve(dummys)

        if good is None:
            countbad += 1.0

        else:
            countgood += 1.0
            totalage = totalage + good.getmAge()
        
        agecount += 1.0
           
    average = totalage/agecount

    t2 = time.time()
    timetotal = t2 - t1
    
 
    print()
    print("Retrieve Names")
    print("The number of Success is " '%8.2f' %  countgood,".")
    print("The number of Failures is" '%8.2f' % countbad,".")
    print("Student's'average age is " + '%8.2f' % average,".")
    print("It took "+'%8.2f' %timetotal + " Seconds.")


def main():

    studentname = hashtable.Hashtable(300000)

    InsertName(studentname)
    Traverse(studentname)
    deleteNames(studentname)
    retrievename(studentname)
    

main()
