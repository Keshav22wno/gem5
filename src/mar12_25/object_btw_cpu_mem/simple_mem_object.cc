#include "mar12_25/object_btw_cpu_mem/simple_mem_object.hh"

#include "base/trace.hh"
#include "debug/SimpleMemObject.hh"

namespace gem5
{

SimpleMemObject::SimpleMemObject(const Params& params):
	SimObject(params),
	instPort(name()+".inst_port",this),
	dataPort(name()+".data_port",this),
	memPort(name()+".mem_port",this),
	blocked(false)
{
}

// TODO:
//Port&
//SimpleMemObject::getPort(const std::string& if_name, PortId idx)
Port&
SimpleMemObject::getPort(const std::string& if_name, PortID idx)
{
	if (if_name == "inst_port") {
		return instPort;
	} else if (if_name == "data_port") {
		return dataPort;
	} else if (if_name == "mem_port") {
		return memPort;
	} else {
		return SimObject::getPort(if_name,idx);
	}
}

void
SimpleMemObject::CPUSidePort::recvFunctional(PacketPtr pkt)
{
	owner->handleFunctional(pkt);
}

//AddrRangeList
//SimpleMemObject::CPUSidePort::getAddrranges() const
AddrRangeList
SimpleMemObject::CPUSidePort::getAddrRanges() const
{
	//return owner->getAddrRanges();
	return owner->getAddrRange();
}

void
SimpleMemObject::handleFunctional(PacketPtr pkt)
{
	memPort.sendFunctional(pkt);
}

//AdderangeList
//AddrRangeList
//SimpleMemObject::getAddrRanges() const
AddrRangeList
SimpleMemObject::getAddrRange() const
{
	DPRINTF(SimpleMemObject,"%s: Sending nre ranges.\n",__func__);
	return memPort.getAddrRanges();
}

void
SimpleMemObject::MemSidePort::recvRangeChange()
{
	owner->sendRangeChange();
}

void
SimpleMemObject::sendRangeChange()
{
	// sendrangeChange already implememnted by ResponsePort
	//instPort.sendrangeChange();
	//dataPort.sendrangeChange();
	instPort.sendRangeChange();
	dataPort.sendRangeChange();
}	

bool
//SimpleMemObject::handleRequest()
SimpleMemObject::CPUSidePort::recvTimingReq(PacketPtr pkt)
{
	if (!owner->handleRequest(pkt)) {
		needRetry=true;
		return false;	
	} else {
		return true;
	}
}

bool
SimpleMemObject::handleRequest(PacketPtr pkt)
{
	if (blocked || memPort.blocked() ||
			instPort.blocked() || dataPort.blocked()) {
		return false;
	}

	DPRINTF(SimpleMemObject,"%s: Recieved a request for addr %#x.\n",__func__,pkt->getAddr());
	blocked=true;
	memPort.sendPacket(pkt);
	return true;
}

void
SimpleMemObject::MemSidePort::sendPacket(PacketPtr pkt)
{
	panic_if(blockedPacket != nullptr, "Should not try to send if blocked.");
	if (!sendTimingReq(pkt)) {
		blockedPacket = pkt;
	}
}

void
SimpleMemObject::MemSidePort::recvReqRetry()
{
	assert(blockedPacket != nullptr);
	DPRINTF(SimpleMemObject, "%s: Recieved a request retry.\n",__func__);

	PacketPtr pkt = blockedPacket;
	blockedPacket=nullptr;
	sendPacket(pkt);
}

bool
SimpleMemObject::MemSidePort::recvTimingResp(PacketPtr pkt)
{
	return owner->handleResponse(pkt);
}

bool
SimpleMemObject::handleResponse(PacketPtr pkt)
{
	assert(blocked);
	DPRINTF(SimpleMemObject, "%s: Recieved a response for addr %#x.\n",
			__func__, pkt->getAddr());
	blocked=false;
	if (pkt->req->isInstFetch()) {
		instPort.sendPacket(pkt);	//route to cpu, using instPort
	} else {
		dataPort.sendPacket(pkt);	//route to cpu, using dataPort
	}

	instPort.trySendRetry();		//incase instPort at ourObject rejected a instFetch request from CPU in old times. So, send a signal to CPU to retry that request.
	dataPort.trySendRetry();

	return true;
}

void
SimpleMemObject::CPUSidePort::sendPacket(PacketPtr pkt)
{
	panic_if(blockedPacket != nullptr, "Should never try to send if blocked.");

	if (!sendTimingResp(pkt)) {
		blockedPacket = pkt;
	}
}

void
SimpleMemObject::CPUSidePort::recvRespRetry()
{
	assert(blockedPacket != nullptr);

	//packetPtr pkt = blockedPacket;
	PacketPtr pkt = blockedPacket;
	blockedPacket = nullptr;

	sendPacket(pkt);
}

void
SimpleMemObject::CPUSidePort::trySendRetry()
{
	if (needRetry && (blockedPacket == nullptr)) {
		needRetry = false;
		DPRINTF(SimpleMemObject, "%s: Sending a retry request.\n",__func__);
		sendRetryReq();
	}
}

} // end of namespace gem5
