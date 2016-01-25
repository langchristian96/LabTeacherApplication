'''
Created on Jan 25, 2016

@author: LenovoM
'''
from Domain.Problem import *
import copy
class ProblemRepository:
    _fName='problem.txt'
    def __init__(self):
        self.__data=[]
        self.__loadFromFile()
        self.__undo=None
        self.__redo=None
    def setData(self,list):
        self.__data=list
    def store(self):
        self.__storeToFile()
    def __loadFromFile(self):
        try:
            f=open(self._fName,'r')
            t=f.readline().strip()
            while t!='':
                args=t.split(',')
                self.__data.append(Problem(int(args[0]),int(args[1]),args[2],int(args[3])))
                t=f.readline().strip()
            
            f.close()
        except IOError:
            return
    def __storeToFile(self):
        f=open(self._fName,'w')
        st=''
        for e in self.__data:
            
            st+=str(e.getId())
            st+=','
            st+=str(e.getLab())
            st+=','
            st+=e.getProblem()
            st+=','
            st+=str(e.getGrade())
            st+='\n'
        f.write(st)
        f.close()
        
        
    def find(self,id,lab):
        for e in self.__data:
            if e.getId()==id and e.getLab()==lab:
                return e
        return None
    def add(self,obj):
        self.__undo=copy.copy(self.__data)
        e=self.find(obj.getId(),obj.getLab())
        if e==None:
            self.__data.append(obj)
            self.__storeToFile()
        else:
            raise ValueError("Student has an assignment for this lab or ID does not exist")
  
    def updateGrade(self,obj):
        self.__undo=copy.copy(self.__data)
        print(obj.getGrade())
        e=self.find(obj.getId(),obj.getLab())
        if e==None:
            raise ValueError("Object does not exist")
        elif e.getGrade()!=0:
            raise ValueError("Grade cannot be modified")
        else:
            idx=self.__data.index(e)
            
            obj2=Problem(obj.getId(),obj.getLab(),e.getProblem(),obj.getGrade())
            self.__data.remove(e)
            self.__data.insert(idx,obj2)
            print(str(obj2.getId()),str(obj2.getLab()),obj2.getProblem(),str(obj2.getGrade()))
            self.__storeToFile()
    def getAll(self):
        return self.__data
    def undo(self):
        self.__redo=copy.copy(self.__data)
        self.__data=copy.copy(self.__undo)
        self.__storeToFile()
    def redo(self):
        self.__undo=copy.copy(self.__data)
        self.__data=copy.copy(self.__redo)
        self.__storeToFile()