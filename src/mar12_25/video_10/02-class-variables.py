class Processor:
    default_frequency="3GHz"
    # the baove-one is a class variable

    # the below one is the constructor
    def __init__(self,name):
        self.name=name

    def change_default_frequency(self,new_frequency):
        # this does not change Processor.default_frequency
        # it creates an *object* variable instead
        self.default_frequency=new_frequency

    def to_string(self):
        return str(vars(self))


class ProcessorWithClassFunction(Processor):
    def __init__(self,name):
        super().__init__(name)

    @classmethod # A proper method to update class variables
    def change_default_frequency_with_class_function(cls,new_frequency):
        cls.default_frequency=new_frequency

if __name__=="__m5_main__":
    cpu1=Processor("Processor 1")
    cpu2=Processor("Processor 2")

    print("**** Class variable example 1: Accessing a class variable")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()

    Processor.default_frequency="1GHz"
    print("**** Class variable example 2: Directly changing a class variable")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()
    
    cpu1.change_default_frequency("220MHz") # this will create a new variable inside the instance
    print("**** Class variable example 2.2: Mistakenly creating a object variable")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()
    
    cpu1.default_frequency="200MHz" # this will create a new variable inside the instance
    print("**** Class variable example 3: Mistakenly creating a object variable")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()
    
    #cpu1.change_default_frequency="220MHz" # this will create a new variable inside the instance
    cpu1.change_default_frequency("220MHz") # this will create a new variable inside the instance
    print("**** Class variable example 4: Mistakenly creating a object variable")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()


    # change the default_frequency back to the original frequency
    Processor.default_frequency="3GHz"
    cpu1=ProcessorWithClassFunction("ProcessorWithClassFunction1")
    cpu2=ProcessorWithClassFunction("ProcessorWithClassFunction2")

    print(
            "**** Class function example 5:"
            "Changing a class variable")
    ProcessorWithClassFunction.change_default_frequency_with_class_function(
            "13GHz")
            #ProcessorWithClassFunction,"13GHz")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()

    #cpu1.change_default_frequency_with_class_function(cpu1,"14GHz")
    cpu1.change_default_frequency_with_class_function("14GHz")
    print(
            "**** Class function example 6:"
            "Changing a class variable")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print(f"Accesing default_frequency via ProcessorWithClassFunction:\
        {ProcessorWithClassFunction.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()

    #cpu2.change_default_frequency_with_class_function(cpu1,"15GHz")
    cpu2.change_default_frequency_with_class_function("15GHz")
    print(
            "**** Class function example 7:"
            "Changing a class variable")
    print(f"Accesing default_frequency via cpu1:{cpu1.default_frequency}")
    print(f"Accesing default_frequency via cpu2:{cpu2.default_frequency}")
    print(f"Accesing default_frequency via Processor:{Processor.default_frequency}")
    print(f"Accesing default_frequency via ProcessorWithClassFunction:\
        {ProcessorWithClassFunction.default_frequency}")
    print()
    print(f"cpu1 object variables: {vars(cpu1)}")
    print(f"cpu2 object variables: {vars(cpu2)}")
    print()
