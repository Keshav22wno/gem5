from abc import ABC, abstractmethod

# "abc" here is abstractbaseclass

# a class is abstract if contains atleast one abstract function
# a fucntion is abstarct if it is not defined but declared

class AbstractCPU(ABC):
    # not all functions have to be abstarct
    def to_string(self):
        return str(var(self))

    # the way to define abstract functions in python
    @abstractmethod
    def connectToInstCache(self,inst_cache):
        pass

    @abstractmethod
    def connectToDataCache(self,data_cache):
        pass

class CPUImplementation1(AbstractCPU):
    def __init__(self,freq):
        self.freq=freq
        self.inst_cache=None
        self.data_cache=None

    def connectToDataCache(self, data_cache):
        self.data_cache=data_cache

class SimpleCacheCPU(AbstractCPU):
    def __init__(self,freq):
        self.freq=freq
        self.data_cache=None

    def connectToInstCache(self,inst_cache):
        # we will use datd cache for caching instructions
        pass

    def connectToDataCache(self,data_cache):
        print("Connecting cpu to data cache")
        self.data_cache=data_cache

class MultiCacheCPU(AbstractCPU):
    def __init__(self,freq):
        self.freq=freq
        self.inst_cache=None
        self.data_cache=None

    def connectToInstCache(self,inst_cache):
        print("Connecting to inst cache")
        self.inst_cache=inst_cache

    def connectToDataCache(self,data_cache):
        print("Connecting to data cache")
        self.data_cache=data_cache 

class Simulator:
    def __init__(self,cpu,inst_cache,data_cache):
        self.cpu=cpu
        self.inst_cache=inst_cache
        self.data_cache=data_cache

    def initialize_system(self):
        self.cpu.connectToInstCache(self.inst_cache)
        self.cpu.connectToDataCache(self.data_cache)

if __name__=="__m5_main__":
    # creating an object from an abstract function will
    try:
        cpu=AbstractCPU()
    except Exception as exception:
        print(type(exception))
        print(exception,'\n')

    # a class having at least one abstract function
    try:
        cpu=CPUImplementation1("4GHz")
    except Exception as exception:
        print(type(exception))
        print(exception,'\n')

    # a class having no abastract method. But, one method is just pass type
    try:
        cpu=SimpleCacheCPU("3GHz")
        print(vars(cpu))
    except Exception as exception:
        print(type(exception))
        print(exception,'\n')

    # a class having all methods properly defined
    try:
        cpu=MultiCacheCPU("2GHz")
        print(vars(cpu))
    except Exception as exception:
        print(type(exception))
        print(exception,'\n')

    inst_cache="inst_cache"
    data_cache="data_cache"

    cpu1=SimpleCacheCPU("2GHz")
    cpu2=MultiCacheCPU("3GHz")

    print("Setting up Simultor1")
    simulator1=Simulator(cpu1,inst_cache,data_cache)
    simulator1.initialize_system()
    print(vars(simulator1),'\n')

    print("Setting up Simulator2")
    simulator2=Simulator(cpu2,inst_cache,data_cache)
    simulator2.initialize_system()
    print(vars(simulator2),'\n')
