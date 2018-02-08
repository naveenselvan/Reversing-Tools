/*
   CGC Loader
   Copyright (C) 2014 Chris Eagle
   
   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:
   
   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.
   
   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.
*/

#ifndef _CGC_H_
#define _CGC_H_

#include <stdint.h>

#define CT_EXEC   2
#define CM_386    3

#define SHT_PROGBITS 1
#define SHT_NOBITS   8

#define STT_OBJECT   1
#define STT_FUNC     2

/* The CGC Executable File Header */
#define CI_NIDENT   16

struct CGC32_hdr {
   uint8_t	e_ident[CI_NIDENT];
#define CI_IDENT	"\177CGC\x01\x01\x01\x43\x01\x00\x00\x00\x00\x00\x00"
   /* ELF vs CGC identification 
   * ELF          CGC
   *  0x7f        0x7f
   *  'E'         'C'
   *  'L'         'G'
   *  'F'         'C'
   *  class       1       : '1' translates to 32bit ELF
   *  data        1       : '1' translates to little endian ELF
   *  version     1       : '1' translates to little endian ELF
   *  osabi       \x43    : '1' CGC OS
   *  abiversion  1       : '1' translates to version 1
   *  padding     random values
   */
   uint16_t	e_type;         /* Must be 2 for executable */
   uint16_t	e_machine;      /* Must be 3 for i386 */
   uint32_t	e_version;      /* Must be 1 */
   uint32_t	e_entry;        /* Virtual address entry point */
   uint32_t	e_phoff;        /* Program Header offset */
   uint32_t	e_shoff;        /* Section Header offset */
   uint32_t	e_flags;        /* Must be 0 */
   uint16_t	e_ehsize;       /* CGC header's size */
   uint16_t	e_phentsize;    /* Program header entry size */
   uint16_t	e_phnum;        /* # program header entries */
   uint16_t	e_shentsize;    /* Section header entry size */
   uint16_t	e_shnum;        /* # section header entries */
   uint16_t	e_shstrndx;     /* sect header # of str table */
};

/* The CGC Executable Section Header */
struct CGC32_Shdr {
   uint32_t        sh_name;        /* Name (index into strtab) */
   uint32_t        sh_type;        /* Section type */
#define SHT_SYMTAB  2               /* Symbol table */
#define SHT_STRTAB  3               /* String Table */
   uint32_t        sh_flags;
#define SHF_WRITE   (1<<0)          /* Section is writable */
#define SHF_ALLOC   (1<<1)          /* Section is in memory */
#define SHF_EXECINSTR (1<<2)        /* Section contains code */
   uint32_t        sh_addr;        /* Address of section */
   uint32_t        sh_offset;      /* Offset into file */
   uint32_t        sh_size;        /* Section size in file */
   uint32_t        sh_link;
          /* When sh_type is SHT_SYMTAB, sh_link is the index of
           * the associated SHT_STRTAB section
           */
   uint32_t        sh_info;
          /* When sh_type is SHT_SYMTAB, info is one greater
           * than the symbol table index of the last local
           * symbol.
           */
   uint32_t        sh_addralign;   /* Alignment constraints */
   uint32_t        sh_entsize;
          /* Size in bytes of each entry pointed to by this
           * section table */
};

/* The CGC Executable Program Header */
struct CGC32_Phdr {
   uint32_t        p_type;         /* Section type */
#define PT_NULL     0               /* Unused header */
#define PT_LOAD     1               /* Segment loaded into mem */
#define PT_PHDR     6               /* Program hdr tbl itself */
#define PT_CGCPOV2  0x6ccccccc      /* CFE Type 2 PoV flag sect */
   uint32_t        p_offset;       /* Offset into the file */
   uint32_t        p_vaddr;        /* Virtual program address */
   uint32_t        p_paddr;        /* Set to zero */
   uint32_t        p_filesz;       /* Section bytes in file */
   uint32_t        p_memsz;        /* Section bytes in memory */
   uint32_t        p_flags;        /* section flags */
#define PF_X        (1<<0)          /* Mapped executable */
#define PF_W        (1<<1)          /* Mapped writable */
#define PF_R        (1<<2)          /* Mapped readable */
   /* Acceptable flag combinations are:
   *        PF_R
   *        PF_R|PF_W
   *        PF_R|PF_X
   *        PF_R|PF_W|PF_X
   */
   uint32_t        p_align;        /* Only used by core dumps */
};

struct CGC32_Sym {
   uint32_t   st_name;
   uint32_t   st_value;
   uint32_t   st_size;
   uint8_t  st_info;
   uint8_t  st_other;
   uint16_t st_shndx;
};

#define CGC32_ST_TYPE(info) ((info) & 0xf)

#endif

