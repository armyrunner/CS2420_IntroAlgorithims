import student
import time


def InsertName():
    timetotal = 0
    t1 = time.time()

    studentname = []

    #  Insert Names
    finstudent = open("../StudentTextFiles/InsertNames.txt", "r")
    for line in finstudent:
        words = line.split()
        s = student.Student(words[0], words[1],
                            words[2], words[3], int(words[4]))
        duplicate = False
        for i in range(len(studentname)):

            if s.mSSN == studentname[i].mSSN:
                duplicate = True
        if duplicate:
            print(s.mLast, s.mFirst, "is a duplicate")
        else:
            studentname.append(s)

    finstudent.close()
       
    t2 = time.time()
    timetotal = t2 - t1
    print("Original Student List took " + '%8.2f' %  timetotal + " Seconds" )


    return studentname


def avgAge(studentname):

    timetotal = 0
    t1 = time.time()

    count = 0.0
    totalage = 0.0

    for studentage in studentname:
        totalage = totalage + studentage.getmAge()
        count +=1
    average = totalage/count

    t2 = time.time()
    timetotal = t2 - t1

    print("Student's'average age is " + '%8.2f' % average,". It took" '%8.2f' %  timetotal + " Seconds" )


# Delete Names by comparing a a file to a list and remove the name from that list

def deleteNames(studentname):
    timetotal = 0
    t1 = time.time()

    finstudent = open("../StudentTextFiles/DeleteNames.txt", "r")
    for line in finstudent:
        line = line.strip()
        NotFound = True
        for student in studentname:
            if line == student.mSSN:
                studentname.remove(student)
                NotFound = False
        if NotFound:
            print(line,"Not Found in List")

    t2 = time.time()
    timetotal = t2 - t1

    print("It took "+'%8.2f' %timetotal + " Seconds")

def retrievename(studentname):

    timetotal = 0
    t1 = time.time()

    count = 0.0
    totalage = 0.0
    
    finstudent = open("../StudentTextFiles/RetrieveNames.txt", "r")
    for line in finstudent:
        line = line.strip()
        NotFound = True
        for student in studentname:
            if line == student.mSSN:
                totalage = totalage + student.getmAge()             
                count +=1
                NotFound = False
        if NotFound:
            print(line,"Not Found in List")

    average = totalage/count

    t2 = time.time()
    timetotal = t2 - t1

    print("Student's'average age is " + '%8.2f' % average,". It took" '%8.4f' %  timetotal + " Seconds" )

    return studentname


def main():

    finstudent = InsertName()
    print()
    avgAge(finstudent)
    print()
    deleteNames(finstudent)
    print()
    retrievename(finstudent)


    
main()
