#include "posix.c"
#include "linux.c"

void sys_exit(int status) __noreturn __syscall(60);
void sys_exit_group(int status) __noreturn __syscall(231);

void cgc_longjmp(int, int) __noreturn;
void _terminate(unsigned int status) __noreturn;
void terminate(unsigned int status) __noreturn;