#ifndef LIBC
#define LIBC(x) x
#endif

typedef void* va_list;

void LIBC(exit)(int status) __noreturn;
void LIBC(_exit)(int status) __noreturn;
void LIBC(__stack_chk_fail)() __noreturn;
void LIBC(pthread_exit)(void* retval) __noreturn;
void LIBC(abort)() __noreturn;
void LIBC(err)(int eval, const char *fmt, ...) __noreturn;
void LIBC(verr)(int eval, const char *fmt, va_list args) __noreturn;
void LIBC(errc)(int eval, int code, const char *fmt, ...) __noreturn;
void LIBC(verrc)(int eval, int code, const char *fmt, va_list args) __noreturn;
void LIBC(errx)(int eval, const char *fmt, ...) __noreturn;
void LIBC(verrx)(int eval, const char *fmt, va_list args) __noreturn;
