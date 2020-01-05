#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void alarm_handler() {
    printf("Timeout...\n");
    exit(0);
}

USELESS_FUNCTIONS

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    signal( SIGALRM, alarm_handler );
    alarm(30);
    USELESS_BUFFERS_1
	char name[BUFFER_SIZE];
    USELESS_BUFFERS_2

    USELESS_CALLS

	printf("What's your name? ");
	gets(name);
	printf("GREETING, %s!\n", name);
	puts("GOOD_BYE!");

	return 0;
}


