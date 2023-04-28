#abubakarasif3111@gmail.com
#https://github.com/Abubakar3111
#https://www.linkedin.com/in/abubakar-asif-b3b94021a/
#Implementation of TableDrivenVacuumAgent

from agents4e import *
from inspect import getsource
from utils4e import distance_squared,turn_heading

tve=TrivialVacuumEnvironment();
print("The Environment Status is:"+str(tve.status))
a=TableDrivenVacuumAgent()
tve.add_thing(a)
print("The Agent Location"+str(a.location))
tve.step()
print("The Environment Status is:"+str(tve.status))
print("The Agent Location"+str(a.location))
print("Coded by Abubakar Asif")