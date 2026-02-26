from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import CustomResource
from gem5.simulate.simulator import Simulator
from gem5.isas import ISA

cache_hierarchy=PrivateL1CacheHierarchy(
        l1d_size="32KiB",
        l1i_size="32KiB",
        )
memory=SingleChannelDDR3_1600("1GiB")

processor=SimpleProcessor(
        #cpu_type=CPUTypes.ATOMIC,
        #cpu_type=CPUTypes.TIMING,
        cpu_type=CPUTypes.O3,
        num_cores=1,
        isa=ISA.X86
        )

board=SimpleBoard(
        clk_freq="1GHz",
        processor=processor,
        memory=memory,
        cache_hierarchy=cache_hierarchy,
        )

binary=CustomResource("/home/docker_share/gem5/configs/learning_gem5/mar12_25/int_mul")
board.set_se_binary_workload(binary)

simulator=Simulator(board=board)
simulator.run()

# command to test this configuration script
#./build/X86/gem5.opt configs/learning_gem5/mar12_25/cpu_models_ex1.py
#./build/X86/gem5.opt configs/learning_gem5/mar12_25/cpu_models_ex1.py
