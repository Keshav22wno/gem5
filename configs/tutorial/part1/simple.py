import m5
from m5.objects import *

## ---- system object parent to all othe robjects
## contains functional information, no timing information
system = System()

system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_doamin = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

system.cpu = X86TimingSimpleCPU()

system.membus = SystemXBar()

system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports

#system.cpu.icache_port = system.l1_cache.cpu_side
#system.cpu.icache_port = system.membus.cpu_side_ports

system.cpu.createInterruptController()
#### ---- these below interrupts req, reponse are with X86 only, nO other ISA has it.
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

#### ---- creating a memory controller and connect it to membus
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports


#### ---- we are in syscall mode
#### in syscall mode we need to provide the compiled(statically) binary as a process.
binary = 'tests/test-progs/hello/bin/x86/linux/hello'

system.workload = SEWorkload.init_compatible(binary)

process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

#### ---- Now, just instantiate the system and begin execution.
#### parameters as named arguments
root = Root(full_system = False, system = system)
m5.instantiate()

#### below print is a function not a statement. gem5 function
print("Begining Simulation")
exit_event = m5.simulate()

print('Exiting @ tick {} because {}'.format(m5.curTick(),exit_event.getCause()))
