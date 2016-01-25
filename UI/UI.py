'''
Created on Jan 25, 2016

@author: LenovoM
'''
from Domain.Problem import *
from Domain.Student import *
from Repository.PRepository import *
from Repository.Repository import *
from Controller.Controller import *
class UI:
    def __init__(self,ctrl):
        self.__ctrl=ctrl
        
    def printMenu(self):
        print('1.Add a student')
        print('2.Remove a student')
        print('3.Add an assignment')
        print('4.Assign laboratory to a group of students')
        print('5.Grade Student')
        print('6.Students average in decreasing order at a given group')
        print('7.Students that are failing the class')
        print('8.Undo')
        print('9.Redo')
        print('0.Exit')
        
    def validCommand(self,command):
        commandDict=['1','2','3','4','5','6','7','8','9','0']
        return (command in commandDict)
    def __addStudent(self):
        try:
            id=int(input("Input id "))
            name=input("Input name ")
            group=int(input("Input group"))
            self.__ctrl.addStudent(Student(id,name,group))
        except ValueError as e:
            print(e)
    def __removeStudent(self):
        try:
            id=int(input("Input id "))
            self.__ctrl.removeStudent(id)
        except ValueError as e:
            print(e)
    def __addProblem(self):
        try:
            id=int(input("Input id "))
            lab=int(input("Input lab "))
            problem=input("Input problem ")
            self.__ctrl.addProblem(Problem(id,lab,problem,0))
            
            
        except ValueError as e:
            print(e)
    def __assignLab(self):
        try:
            lab=int(input("Input laboratory number "))
            group=int(input("Input group"))
            fName=input("Input filename where the lab problems are located(each problem must be on a line)")
            fName.strip()
            self.__ctrl.assignLaboratory(lab,fName,group)
            
        except ValueError as e:
            print(e)
        except IOError:
            print("File does not exist")
    
    def __assignGrade(self):
        try:
            id=int(input("Input id "))
            lab=int(input("Input lab "))
            problem='random'
            grade=int(input('Input grade '))
            if grade<1 or grade>10:
                raise ValueError("wrong grade")
            self.__ctrl.gradeStudent(Problem(id,lab,problem,grade))
            
        except ValueError as e:
            print(e)
    def __topStuds(self):
        try:
            group=int(input("Input group "))
            list=self.__ctrl.topStudent(group)
            for e in list:
                print(e)
        except ValueError as e:
            print(e)
    def __undo(self):
        try:
            self.__ctrl.undo()
        except ValueError as e:
            print(e)
    def __failClass(self):
        l=self.__ctrl.failClass()
        for e in l:
            print(e)
    def __redo(self):
        try:
            self.__ctrl.redo()
        except ValueError as e:
            print(e)
    def Menu(self):
        commandDict={'1':self.__addStudent,
                     '2':self.__removeStudent,
                     '3':self.__addProblem,
                     '4':self.__assignLab,
                     '5':self.__assignGrade,
                     '6':self.__topStuds,
                     '7':self.__failClass,
                     '8':self.__undo,
                     '9':self.__redo
                     
                     }
        while True:
            self.printMenu()
            command=input("Input command ")
            while not self.validCommand(command):
                command=input("Wrong command. Try again ")
            if command=='0':
                return
            commandDict[command]()
            print('\n')
        
        