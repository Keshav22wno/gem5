import m5
from m5.objects import *

#import args

# root is a special sim object that is going to be the root of that object tree
# evry object that we add is below this root object
root=Root(full_system=False)

# adding a child to root by name "hello" of type HelloSimObject
root.hello=HelloSimObject(var_latency="2ns",var_number_of_times=12);
#arguments=args.parse_args()
#root.hello=HelloSimObject(n=params.n,L=params.L);

# here gem5 instantiates these above created sim objects
m5.instantiate()

print("Begining Simulation")
exit_event=m5.simulate()
print(f"Exiting at {m5.curTick()} because {exit_event.getCause()}")
