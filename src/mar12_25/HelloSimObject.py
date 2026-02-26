from m5.SimObject import SimObject

from m5.params import *

class HelloSimObject(SimObject):
    type="HelloSimObject"       # same as the object name
    cxx_header="mar12_25/hello_sim_object.hh"   # specify the path relative to src
    cxx_class="gem5::HelloSimObject"        # this imobject is implemented inside the gem5 namespace
    
    # gem5 allows simobjects as parameters to another simobject
    # we should never instantiate simobject indide parameter definition
    var_latency=Param.Latency("Time to wait before greeting")
    var_number_of_times=Param.Int(1,"Number of times")

    # setting one parameter which is simobject using another parametr which is simobject
    # should be done form configuration script only
    # never ever call the constructor when you specify the parameter value which is a simobject to anothe simobject

    #def __init__(self,n=1,L=1):
    #    self.n=n
    #    self.L=L
