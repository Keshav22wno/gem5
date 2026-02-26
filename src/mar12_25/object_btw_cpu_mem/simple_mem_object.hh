#ifndef __BOOTCAMP_SIMPLE_MEM_OBJECT_ISMPLE_MEM_OBJECT_HH__
#define __BOOTCAMP_SIMPLE_MEM_OBJECT_ISMPLE_MEM_OBJECT_HH__

#include "sim/sim_object.hh"
#include "mem/packet.hh"

#include "mem/port.hh"
// the below one is in the params it is created during build
#include "params/SimpleMemObject.hh"

namespace gem5
{

class SimpleMemObject : public SimObject
 	{
	public:
		SimpleMemObject(const Params &params);
	private:
		class CPUSidePort : public ResponsePort
		 {
			 private:
				 SimpleMemObject* owner;

				 bool needRetry;

				 PacketPtr blockedPacket;
			public:
				 CPUSidePort(const std::string& name, SimpleMemObject* owner):
					 ResponsePort(name,owner),
					 owner(owner), needRetry(false), blockedPacket(nullptr)
			 	{
				}
				 // what address this port is responsible for
				 AddrRangeList getAddrRanges() const override;
				 //AddrRangeList getAddrRange() const override;

				 bool blocked() { return blockedPacket!=nullptr; }

				 //void sendPacket(packetPtr pkt);
				 void sendPacket(PacketPtr pkt);

				 //void trysendRetry();
				 void trySendRetry();
			
			protected:
				 //Tick recvAtomic(packetPtr pkt) override
				 Tick recvAtomic(PacketPtr pkt) override
				 {
					 panic("recvAtomic unimpl.");
				 }
				 void recvFunctional(PacketPtr pkt) override;
				 bool recvTimingReq(PacketPtr pkt) override;
				 void recvRespRetry() override;
		 };
		class MemSidePort : public RequestPort
		 {
			 private:
				 SimpleMemObject* owner;
				
				 // we should never reject the response that memory sends you
				 //bool needRetry;
	
				 PacketPtr blockedPacket;
			public:
				 MemSidePort(const std::string& name, SimpleMemObject* owner):
					 RequestPort(name,owner),
					 owner(owner),blockedPacket(nullptr)
			 	{
				}
					//owner(owner),needRetry(false),blockedPacket(nullptr)
				
				bool blocked() {return blockedPacket!=nullptr;}

				void sendPacket(PacketPtr pkt);
			protected:
				//bool recvTimingResp(packetPtr pkt) override;
				bool recvTimingResp(PacketPtr pkt) override;
				void recvReqRetry() override;
				void recvRangeChange() override;

		 };

		CPUSidePort instPort;
		CPUSidePort dataPort;

		MemSidePort memPort;

		bool blocked;

		void handleFunctional(PacketPtr pkt);
		AddrRangeList getAddrRange() const;
		void sendRangeChange();
		bool handleRequest(PacketPtr pkt);
		bool handleResponse(PacketPtr pkt);

	public:
		PARAMS(SimpleMemObject);
		SimpleMemObject(const Params& params);

		Port& getPort(const std::string& if_name,
				PortID idx=InvalidPortID) override;

};
}	// end of namespace gem5
#endif	// __BOOTCAMP_SIMPLE_MEM_OBJECT_ISMPLE_MEM_OBJECT_HH__
