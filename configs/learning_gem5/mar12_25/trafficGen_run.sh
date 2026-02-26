#!/bin/sh

base_path="/home/docker_share/m5out"
#echo ($base_path)ddr3_ro
#exit
./build/NULL/gem5.opt --outdir=$base_path"_ddr3_ro" configs/learning_gem5/mar12_25/trafficGen_example1.py DDR3_1600_8x8 random 100
./build/NULL/gem5.opt --outdir=$base_path"_ddr4_ro" configs/learning_gem5/mar12_25/trafficGen_example1.py DDR4_2400_16x16 random 100
./build/NULL/gem5.opt --outdir=$base_path"_nvm_ro" configs/learning_gem5/mar12_25/trafficGen_example1.py NVM_2400_1x64 random 100

./build/NULL/gem5.opt --outdir=$base_path"_ddr3_r50" configs/learning_gem5/mar12_25/trafficGen_example1.py DDR3_1600_8x8 random 50
./build/NULL/gem5.opt --outdir=$base_path"_ddr4_r50" configs/learning_gem5/mar12_25/trafficGen_example1.py DDR4_2400_16x4 random 50
./build/NULL/gem5.opt --outdir=$base_path"_nvm_r50" configs/learning_gem5/mar12_25/trafficGen_example1.py DDR3_2400_1x64 random 50

./build/NULL/gem5.opt --outdir=$base_path"_ddr3_wo" configs/learning_gem5/mar12_25/trafficGen_example1.py DDR3_1600_8x8 random 0
./build/NULL/gem5.opt --outdir=$base_path"_ddr4_wo" configs/learning_gem5/mar12_25/trafficGen_example1.py DDR4_2400_16x4 random 0
./build/NULL/gem5.opt --outdir=$base_path"_nvm_wo" configs/learning_gem5/mar12_25/trafficGen_example1.py NVM_2400_1x64 random 0
