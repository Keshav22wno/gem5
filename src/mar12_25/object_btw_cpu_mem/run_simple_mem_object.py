import m5
from m5.objects import *


# clk_domain, voltage_domain, ports are not sime objects

system=System()
system.clk_domain=SrcClockDomain()
system.clk_domain.clock='1GHz'
system.clk_domain.voltage_domain=VoltageDomain()
system.mem_mode='timing'
system.mem_ranges=[AddrRange('512MB')]

system.cpu=TimingSimpleCPU()

system.memobj=SimpleMemobj()

system.cpu.icache_port=system.memobj.inst_port
system.cpu.dcache_port=system.memobj.data_port

system.membus=SystemXBar()

system.memobj.mem_side=system.membus.cpu_side_ports

system.cpu.createInterruptController()
system.cpu.interrupts[0].pio=system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor=system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder=system.membus.mem_side_ports

system.mem_ctrl=MemCtrl(dram=DDR3_1600_8x8(range=system.mem_ranges[0]))
system.mem_ctrl.port=system.membus.mem_side_ports

system.system_port=system.membus.cpu_side_ports

# path is with respectto gem5/
binary="tests/test-progs/hello/bin/x86/linux/hello"
system.workload=SEWorkload.init_compatible(binary)

process=Process()
process.cmd=[binary]
system.cpu.workload=process
system.cpu.createThreads()

root=Root(full_system=False, system=system)

m5.instantiate()
print(f"Begining Simulation")
exit_event=m5.simulate()
print('Exiting at tick %i because %s' %(m5.curTick(), exit_event.getCause()))
