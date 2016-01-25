'''
Created on Jan 25, 2016

@author: LenovoM
'''

from Domain.Problem import *
from Domain.Student import *
from Repository.PRepository import *
from Repository.Repository import *
from Controller.Controller import *
from UI.UI import *
repo=Repository()
arepo=ProblemRepository()
ctrl=Controller(repo,arepo)
ui=UI(ctrl)
ui.Menu()