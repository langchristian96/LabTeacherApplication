'''
Created on Jan 25, 2016

@author: LenovoM
'''
class Problem:
    def __init__(self,id,lab,problem,grade):
        self.__id=id
        self.__lab=lab
        self.__problem=problem
        self.__grade=grade
    
    def getId(self):
        return self.__id
    def getLab(self):
        return self.__lab
    def getProblem(self):
        return self.__problem
    def getGrade(self):
        return self.__grade
    def setGrade(self,grade):
        if self.__grade!=0:
            raise ValueError
        else:
            self.__grade=grade
    