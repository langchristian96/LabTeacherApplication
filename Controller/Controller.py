'''
Created on Jan 25, 2016

@author: LenovoM
'''
from operator import itemgetter
from Domain.Problem import *
from Domain.Student import *
from Repository.PRepository import *
from Repository.Repository import *
import copy
class Controller:
    def __init__(self,repo,prepo):
        self.__prepop=None
        self.__prepod=None
        self.__repo=repo
        self.__prepo=prepo
        self.__undor=None
        self.__undop=None
        self.__redor=None
        self.__redop=None
    def addStudent(self,obj):
        self.__undor=1
        self.__redor=None
        self.__undop=None
        self.__redop=None
        self.__repo.add(obj)
    def removeStudent(self,id):
        for e in self.__prepo.getAll():
            if e.getId()==id:
                raise ValueError("Student cannot be removed")
        
        self.__undor=1
        self.__redor=None
        self.__undop=None
        self.__redop=None
        self.__repo.remove(id)
    def addProblem(self,obj):
        self.__undop=1
        self.__redop=None
        self.__undor=None
        self.__redor=None
        self.__prepo.add(obj)
        
    def assignLaboratory(self,lab,fName,group):
        list=[]
        f=open(fName,'r')
        t=f.readline().strip()
        while t!='':
            list.append(t)
            t=f.readline().strip()
        f.close()
        studs=self.__repo.getAll()
        i=0
        
        self.__undop=2
        self.__prepop=copy.copy(self.__prepo.getAll())
        self.__redop=None
        self.__undor=None
        self.__redor=None
        for e in studs:
            if e.getGroup()==group:
                try:
                    if i==len(list):
                        i=0
                    self.__prepo.add(Problem(e.getId(),lab,list[i],0))
                    i+=1
                except ValueError:
                    pass
            
    def gradeStudent(self,obj):
        self.__undop=1
        self.__redop=None
        self.__undor=None
        self.__redor=None
        self.__prepo.updateGrade(obj)
    def topStudent(self,group):
        list=[]
        studs=self.__repo.getAll()
        gs=[]
        ass=self.__prepo.getAll()
        for e in studs:
            if e.getGroup()==group:
                gs.append(e)
        for e in gs:
            average=0
            cont=0
            for i in ass:
                if i.getId()==e.getId():
                    average+=i.getGrade()
                    cont+=1
            if cont!=0:
                average=average/cont
            w={'id':e.getId(),'name':e.getName(),'group':group,'average':average}
            list.append(dict(w))
            list.sort(key=itemgetter('average'),reverse=True)
        return list
            
    def failClass(self):
        list=[]
        studs=self.__repo.getAll()
        ass=self.__prepo.getAll()
        for e in studs:
            average=0
            cont=0
            for i in ass:
                if i.getId()==e.getId():
                    average+=i.getGrade()
                    cont+=1
            if cont!=0:
                average=average/cont
            if average<5:
                w={'id':e.getId(),'name':e.getName(),'average':average}
                list.append(dict(w))
        return list
    
    def undo(self):
        if self.__undor!=None:
            self.__redor=1
            self.__undor=None
            self.__repo.undo()
        elif self.__undop!=None:
            if self.__undop==2:
                self.__undop=None
                self.__prepod=copy.copy(self.__prepo.getAll())
                self.__prepo.setData(copy.copy(self.__prepop))
                self.__prepo.store()
                self.__redop=2
            else:
                self.__redop=1
                self.__undop=None
                self.__prepo.undo()
        else:
            raise ValueError('Cannot undo')
    def redo(self):
        if self.__redor!=None:
            self.__undor=1
            self.__redor=None
            self.__repo.redo()
        elif self.__redop!=None:
            if self.__redop==2:
                self.__redop=None
                self.__prepop=copy.copy(self.__prepo.getAll())
                self.__prepo.setData(copy.copy(self.__prepod))
                self.__prepo.store()
                self.__undop=2
            else:
                
                self.__undop=1
                self.__redop=None
                self.__prepo.redo()
        else:
            raise ValueError("Cannot redo")
    