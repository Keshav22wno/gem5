from m5.params import *
from m5.SimObject import SimObject

class SimpleMemObject(SimObject):
    type="SimpleMemObject"
    cxx_header="mar12_25/object_btw_cpu_mem/simple_mem_object.hh"
    cxx_class="gem5::SimpleMemObject"

    '''
    # this object is sitting btw memeory and cpu
    inst_port=ResponsePort("port to recieve instruction request from cpu")
    data_port=ResponsePort("port to recieve data request from cpu")
    mem_port=RequestPort("port to send requests to memory")
    '''
    
    # More precise
    inst_port=ResponsePort("CPU side port, recieves requests. (Instruction)")
    data_port=ResponsePort("CPU side port, recieves requests. (Data)")
    mem_port=RequestPort("Mem side port, send requests (Instruction +Data)")
