'''
Created on Jan 25, 2016

@author: LenovoM
'''
from Domain.Student import *
import copy
class Repository:
    _fName='student.txt'
    def __init__(self):
        self.__data=[]
        self.__loadFromFile()
        self.__undo=None
        self.__redo=None
    def __loadFromFile(self):
        try:
            f=open(self._fName,'r')
            t=f.readline().strip()
            while t!='':
                args=t.split(',')
                self.__data.append(Student(int(args[0]),args[1],int(args[2])))
                t=f.readline().strip()
            
            f.close()
        except IOError:
            return
    def store(self):
        self.__storeToFile()
    def __storeToFile(self):
        f=open(self._fName,'w')
        st=''
        for e in self.__data:
            
            st+=str(e.getId())
            st+=','
            st+=e.getName()
            st+=','
            st+=str(e.getGroup())
            st+='\n'
        f.write(st)
        f.close()
        
        
        
    def find(self,id):
        for e in self.__data:
            if e.getId()==id:
                return e
        return None
    def add(self,obj):
        self.__undo=copy.copy(self.__data)
        e=self.find(obj.getId())
        if e==None and obj.getName().strip()!='':
            self.__data.append(obj)
            self.__storeToFile()
        else:
            raise ValueError("Student already exists")
    def remove(self,obj):
        self.__undo=copy.copy(self.__data)
        e=self.find(obj)
        if e==None:
            raise ValueError("Student does not exist")
        else:
            self.__data.remove(e)
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