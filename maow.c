#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <readline/readline.h>

char *username;

void maow(){
	printf("maow!\r\n");
}

void clear(){
	printf("\033[2J\033[H");
}

int main(int argc, char **argv){
	int running;
	char* cmd;

	running = 1;
	while(running){
		cmd = readline("maow> ");
		if(cmd == (char*)NULL || strcmp(cmd, "quit") == 0){
			running = 0;
			continue;
		}
		if(strcmp(cmd, "maow") == 0){
			maow();
			continue;
		}
		if(strcmp(cmd, "clear") == 0){
			clear();
			continue;
		}
	}
	return 0;
}

