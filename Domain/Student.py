'''
Created on Jan 25, 2016

@author: LenovoM
'''
class Student:
    def __init__(self,id,name,group):
        self.__id=id
        self.__name=name
        self.__group=group
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getGroup(self):
        return self.__group


def testStudent():
    st=Student(1,'caca',900)
    assert st.getId()==1
    assert st.getName()=='caca'
    assert st.getGroup()==900
    
if __name__=='__main__':
    testStudent()