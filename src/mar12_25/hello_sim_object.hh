#ifndef __BOOTCAMP_HELLO_SIM_OBJECT_HELLO_SIM_OBJECT_HH__
#define __BOOTCAMP_HELLO_SIM_OBJECT_HELLO_SIM_OBJECT_HH__

// this params file will be generated automaticalyy during gem5 compilation
// python defines this header file
#include "params/HelloSimObject.hh"

// a c or cpp header file of sim_object
#include "sim/sim_object.hh"

// Every simobject has the power to enque events in the event queue of gem5.
// There are many ways of adding events.
// We will use here the event function wrapper.
// It wraps the function that the event needs to call along with the event into one single object

namespace gem5
{

class HelloSimObject : public SimObject
	{
		// This is a function that will wrap the function with the event who will call this fucntion as a single object
		private:
			EventFunctionWrapper event;
			// The below is the functio that this event will execute when popped
			// These functions should not return anything. Or, void functions.
			void processEvent();
			void n_event_after_every_L(int n, int L);
			int n,L;
			const Tick latency;
			int timesLeft;
		public:
			// This PARAMS Macro typecasts a simobject into its params
			PARAMS(HelloSimObject);
			// A constructor in gem5 should take a const objecct of its parameters
			HelloSimObject(const Params& params);
			
			// This functoin is defined in the base simobject and it kicks off at tick=0
			virtual void startup() override;
	};
}	// namespace gem5

#endif	// __BOOTCAMP_HELLO_SIM_OBJECT_HELLO_SIM_OBJECT_HH__
