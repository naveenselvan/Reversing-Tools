struct timeval
{
	uint32_t tv_sec;
	uint32_t tv_usec;
};

void terminate(int status) __noreturn __syscall(1);
int transmit(int fd, const void* buf, size_t count, size_t* tx_bytes) __syscall(2);
int receive(int fd, void* buf, size_t count, size_t* rx_bytes) __syscall(3);
int fdwait(int nfds, uint32_t* readfds, uint32_t* writefds, timeval* timeout, int* readyfds) __syscall(4);
int allocate(size_t len, size_t prot, void** addr) __syscall(5);
int deallocate(void* ptr, size_t len) __syscall(6);
int random(void* buf, size_t count, size_t* rnd_out) __syscall(7);
