#include <unistd.h>
#include "/home/docker_share/gem5/include/gem5/m5ops.h"
//#include "gem5/m5ops.h"

int main(void){
	
	m5_reset_stats(0,0);

	// write is a system call. write(file_descriptor, string, string_size);	
	write(1, "This will be written in the stdout new1\n",41);

	m5_exit(0);
	return 0;	
/*
 * The command to link link m5 and adding the out directory in linlker serach path
 * gcc this_file_path -o o_file_binary_name 
 * 	-I gem5/include		to incluide header files from gem5/include
 * 	-lm5			link against libm5.a
 * 	-Lgem5/util/m5/build/x86/out	add the recently build utility instructions of m5 into likner serach path
 */
}

