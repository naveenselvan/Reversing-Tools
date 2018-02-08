#Set this variable to point to your SDK directory
#Default configuration below assumes this Makefile
#resides in idasdkXX/ldr/cgc_ldr
IDA_SDK=../../

PLATFORM=$(shell uname | cut -f 1 -d _)
BIN=$(shell which idaq 2>/dev/null)
ifeq ($(strip $(BIN)),)
BIN=$(shell which idal 2>/dev/null)
ifeq ($(strip $(BIN)),)
BIN=$(HOME)/ida/idaq
endif
endif

#specify any additional libraries that you may need
EXTRALIBS=

#Set this variable to the desired name of your compiled loader
PROC=cgc

ifeq "$(PLATFORM)" "Linux"

ifeq ($(strip $(BIN)),)
BIN=$(shell find /opt -name idaq | tail -n 1)
ifeq ($(strip $(BIN)),)
BIN=$(HOME)/ida/idaq
endif
endif

IDA=$(dir $(BIN))
PLATFORM_CFLAGS=-D__LINUX__
PLATFORM_LDFLAGS=-shared -s
IDADIR=-L$(IDA)
LOADER_EXT32=.llx
LOADER_EXT64=.llx64

IDALIB32=-lida
IDALIB64=-lida64

else ifeq "$(PLATFORM)" "Darwin"

IDA=$(shell dirname "`find /Applications -name idaq | tail -n 1`")
PLATFORM_CFLAGS=-D__MAC__
PLATFORM_LDFLAGS=-dynamiclib
IDADIR=-L"$(IDA)"
LOADER_EXT32=.lmc
LOADER_EXT64=.lmc64

IDALIB32=-lida
IDALIB64=-lida64

else

$(error Unsupported platform $(PLATFORM))

endif

#Platform specific compiler flags allbinaries are 32-bit
CFLAGS=-Wextra -Os $(PLATFORM_CFLAGS) -m32

#Platform specific ld flags all binaries are 32-bit
LDFLAGS=$(PLATFORM_LDFLAGS) -m32

# Destination directory for compiled plugins
OUTDIR=$(IDA_SDK)bin/loaders/

#list out the object files in your project here
OBJS=cgc.o

SRCS=cgc.cpp

BINARY32=$(OUTDIR)$(PROC)$(LOADER_EXT32)
BINARY64=$(OUTDIR)$(PROC)64$(LOADER_EXT64)

all: $(OUTDIR) $(BINARY32) $(BINARY64)

clean:
	-@rm *.o
	-@rm $(BINARY32)
	-@rm $(BINARY64)

$(OUTDIR):
	-@mkdir -p $(OUTDIR)

CC=g++
INC=-I$(IDA_SDK)include/

%.o: %.cpp
	$(CC) -c $(CFLAGS) $(INC) $< -o $@

LD=g++

ifdef X64

%.o: %.cpp
	$(CC) -c $(CFLAGS) -D__X64__ $(INC) $< -o $@

$(BINARY64): $(SRCS)
	$(LD) $(LDFLAGS) -o $@ $(CFLAGS) -D__X64__ $(SRCS) $(INC) $(IDADIR) $(IDALIB64) $(EXTRALIBS) 

else

%.o: %.cpp
	$(CC) -c $(CFLAGS) $(INC) $< -o $@

$(BINARY32): $(SRCS)
	$(LD) $(LDFLAGS) -o $@ $(CFLAGS) $(SRCS) $(INC) $(IDADIR) $(IDALIB32) $(EXTRALIBS) 

$(BINARY64): $(SRCS)
	$(LD) $(LDFLAGS) -o $@ -D__EA64__ $(CFLAGS) $(SRCS) $(INC) $(IDADIR) $(IDALIB64) $(EXTRALIBS) 

endif

cgc.o: cgc.cpp
