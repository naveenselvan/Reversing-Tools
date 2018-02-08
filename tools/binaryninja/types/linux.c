void __libc_start_main(int (*main)(int argc, char** argv, char** envp), int argc, char** ubp_av,
                       void (*init)(), void (*fini)(), void (*rtld_fini)(), void* stack_end) __noreturn;
void __uClibc_main(int (*main)(int argc, char** argv, char** envp), int argc,
                   char** argv, void (*init)(void), void (*fini)(void),
                   void (*rtld_fini)(void), void *stack_end) __noreturn;
void __assert_fail(const char* assertion, const char* file, unsigned int line, const char* function) __noreturn;