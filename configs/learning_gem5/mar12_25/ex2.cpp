#include<iostream>
#include<dirent.h>

int main(void) {
	
	struct dirent *d;
	DIR *dr;
	dr=opendir("/home/docker_share/gem5/configs/learning_gem5/mar12_25");
	if(dr!=NULL) {
		for(d=readdir(dr); d!=NULL; d=readdir(dr)) {
			std::cout << d->d_name<<",";
		}
		closedir(dr);
	}
	else {
		std::cout<<"Invalid directory path";
	}
	std::cout<<std::endl;
	return 0;

}
