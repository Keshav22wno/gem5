from m5.SimObject import SimObject

class HelloSimObject(SimObject):
    type="HelloSimObject"       # same as the object name
    cxx_header="mar12_25/hello_sim_object.hh"   # specify the path relative to src
    cxx_class="gem5::HelloSimObject"        # this imobject is implemented inside the gem5 namespace
