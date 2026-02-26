#!/biin/sh

# building disk image using packer
#npb=> NAS parallel benchmark

PACKER_VERSION="1.7.8"

if [ ! -f ./packer ]; then
	wget https://release.hashicorp.com/packer/$(PACKER_VERSION)/packer_$(PACKER_VERSION)_linux_amd64.zip;
	unzip packer_$(PACKER_VERSION)_linux_amd64.zip;
	rm packer_$(PACKER_VERSION)_linux_amd_64.zip;
fi

./packer validate npb/npb.json
./packer build npb/npb.json
