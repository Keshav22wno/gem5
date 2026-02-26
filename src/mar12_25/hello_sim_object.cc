#include "mar12_25/hello_sim_object.hh"
//#include "hello_sim_object.hh"

#include <iostream>

// as source is added ininclude search path. So, all includes are relative to source.
// This file has the definition of DPRINTF statement
#include "base/trace.hh"

// auto generated files
// the auto generated files will not be there in the osurce. They will be there in th ebuild directory
#include "debug/HelloExampleFlag.hh"

#include "sim/sim_exit.hh"

// Whenver the HelloSimObject will be instantiated. This event object will also be instantiated. And whenever this event object is instantiated it will call the processEvent() function form the HelloSimObject
// The event object takes two arguments. 1=> the function to execute, 2=> name of this event object
// event([this]{ processEvent();},name()+"some_string")

// Simobject or base simobject has a function "name()" which returns the name of the object.

// Every simobject inherits from a event manager.
// And, every evnet manger has a memeber schedule(pointer_to_event,tick_at_which_evnt_is_scheduled). SO, every simobject can schedule things into the queue.

// There is a line limit of 79 alphabets in gem5
namespace gem5
{
	HelloSimObject::HelloSimObject(const Params &params):
		SimObject(params),
		event([this] {processEvent();},name()+".event"),
		latency(params.var_latency),
		timesLeft(params.var_number_of_times)
	{
		std::cout << "Hello World from a SimObject (constructor)." << std::endl;
		//this->n=params.n;
		//this->L=params.L;
		// print using debug flag
		// print using own defined debug flag
		// The bebug flags come out with tick. So, probably they are being scheduled
		DPRINTF(HelloExampleFlag,"Hello World from a SimObject"
			       "(constructor) with own debug flag.\n");
		// because we were exceeding the line limit
		DPRINTF(HelloExampleFlag,"%s: Hello World from a"
				"SimObject (constructor).\n", __func__);
	}
	
	// this startup() function will be called by default at tick=0.
	void HelloSimObject::startup() 
	{
		DPRINTF(HelloExampleFlag,"%s: Hello World"
				"From a SimObject.\n",__func__);
		// event is litreally a event wrapped witha function. It's of EventFunctionWrapper type
		//schedule(event, 101); 
		schedule(event, latency); 
		/*
		for(int i=1; i<=this->n; i=i+1)
		{
			schedule(event,(this->L)*i);
		}
		*/
	}

	void HelloSimObject::processEvent()
	{
		DPRINTF(HelloExampleFlag,"%s: Hello world."
			       	" Processing and event\n",__func__);
		if (timesLeft>0)
		{
			timesLeft=timesLeft-1;
			DPRINTF(HelloExampleFlag,"%s: Hello World. Greeting left"
					"%d\n",__func__,timesLeft);
		}
		if (timesLeft==0) {
			DPRINTF(HelloExampleFlag,"%s: Done Greeting",__func__);
			// exit now with the given message
			exitSimLoopNow("No greets left");
		}
		if (timesLeft>0) {
			schedule(event, curTick()+latency);
		}
	}

}	// namespace gem5
