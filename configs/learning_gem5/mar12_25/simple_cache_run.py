import m5
import argparse
import importlib
from m5.objects import Root
from gem5.components.boards.test_board import TestBoard
from gem5.components.processors.linear_generator import LinearGenerator
from gem5.components.memory import SingleChannelDDR3_1600

parser=argparse.ArgumentParser(
        description="A traffic generator that can be used to test a gem5"
        "memory component."
)

parser.add_argument(
        "generator_cores",type=int,help="The number of generator cores to use."
)

parser.add_argument(
        "cache_system",
        type=str,
        help="The cache class to import and instantiate",
        choices=["Classic","MESITwoLevel"],
)

parser.add_argument(
        "mem_args",
        nargs="*",
        help="The argumnets needed to instantiate the memory class.",
)

def cache_factory(cache):
    if cache == 'Classic':
        from gem5.components.cachehierarchies\
                .classic.private_l1_private_l2_cache_hierarchy import (
                        PrivateL1PrivateL2CacheHierarchy,
                        )
        return PrivateL1PrivateL2CacheHierarchy(
                l1d_size="32KiB",
                l1i_size="32KiB",
                l2_size="256KiB",
                )
    elif cache=='MESITwoLevel':
        from gem5.components.cachehierarchies\
                .ruby.mesi_two_level_cache_hierarchy import (
                        MESITwoLevelCacheHierarchy,
                        )
        return MESITwoLevelCacheHierarchy(
                l1i_size="32KiB",
                l1i_assoc="8",
                l1d_size="32KiB",
                l1d_assoc="8",
                l2_size="256KiB",
                l2_assoc="4",
                num_l2_banks=1,
                )
    else:
        raise ValueError(f"The cache class {cache} is not supported")


args=parser.parse_args()
cache_hierarchy=cache_factory(args.cache_system)
memory=SingleChannelDDR3_1600(*args.mem_args)
generator=LinearGenerator(
        duration="250us",
        rate="40GB/s",
        num_cores=args.generator_cores,
        max_addr=memory.get_size(),
        )

motherboard=TestBoard(
        clk_freq="3GHz",
        #processor=generator,    # we pass the traffic generator as processor
        generator=generator,    # we pass the traffic generator as processor
        memory=memory,
        cache_hierarchy=cache_hierarchy,
        )

root=Root(full_system=False,system=motherboard)
motherboard._pre_instantiate()
m5.instantiate()
generator.start_traffic()
print("Begining Simulation")
exit_event=m5.simulate()
print(
        "Exiting at tick {} because {}.".format(m5.curTick(),exit_event.getCause())
)

'''
# command to runthis above configuration file
./build/NULL_MESI_Two_Level/gem5.opt configs/learning_gem5/mar12_25/simple_cache_run.py 2 Classic 512MB
./build/NULL_MESI_Two_Level/gem5.opt configs/learning_gem5/mar12_25/simple_cache_run.py 4 MESITwoLevel 512MB
'''
