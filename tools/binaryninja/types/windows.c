void exit(int status) __noreturn;
void _exit(int status) __noreturn;
void __stdcall ExitProcess(uint32_t exitCode) __noreturn;
void __stdcall ExitThread(uint32_t exitCode) __noreturn;
void __stdcall RaiseException(uint32_t exceptionCode, uint32_t flags, uint32_t argCount, size_t* args) __noreturn;
void __stdcall _CxxThrowException(void* pExceptionObject, void* pThrowInfo) __noreturn;
