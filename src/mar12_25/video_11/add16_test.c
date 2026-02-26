#include <stdio.h>
#include <stdint.h>

// This is a test to check evaluate the appended isa
// we appended the isa by ading a simd instructin which adds 64bit as 4x16bit ignoring overflow.
// we made this instruction to be xecuted in one cycle using timing simple cpu
// or we are saying that we have the hardware at alu o perform that instruction in single cycle

int main(void)
{
	uint64_t num1=0x0004000300020001, num2=0x0004000300020001, output=0;
	printf("RISC_V packed addition using {0x4,0x3,0x2,0x1} with {0x4,0x3,0x2,0x1}\n");
	// now it's like inline assembly
	// we specified the below mentioned format in src/arch/risc/isa/decoder.isa at line 526
	// we were using ROp format there and here also
	asm volatile("add16 %0, %1,%2\n":"=r"(output):"r"(num1),"r"(num2):);
	if (output == 0x0008000600040002) {
		printf("test passed\n");
	} else {
		printf("Test Failed\n");
	}
	return 0;
}
