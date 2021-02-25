class Student:
    def __init__(self,last,first,ssn,email,age): 

        self.mLast = last
        self.mFirst = first
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age
 
    def getmlast(self):
        return self.mLast


    def getmfirst(self):
        return self.mFirst

    def getmEmail(self):
        return self.mEmail()

    def getmSSN(self):
        return self.mSSN()

    def getmAge(self):
        return self.mAge

    def __ne__(self,rhs):
        return self.mSSN != rhs.mSSN

    def __eq__(self,rhs):
        return self.mSSN == rhs.mSSN

    def __lt__(self,rhs):
        return self.mSSN < rhs.mSSN

    def __le__(self,rhs):
        return self.mSSN <= rhs.mSSN

    def __gt__(self,rhs):
        return self.mSSN > rhs.mSSN

    def __ge__(self,rhs):
        return self.mSSN >= rhs.mSSN