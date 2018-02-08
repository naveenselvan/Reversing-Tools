#include "posix.c"
#include "linux.c"

void sys_exit(int status) __noreturn __syscall(4001);
void sys_exit_group(int status) __noreturn __syscall(4246);
