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

#include "../idaldr.h"
#include <typeinf.hpp>

//from intel.hpp
#define R_ds 32 

#include "cgc.h"
#include "sdk_versions.h"

#define f_CGC 0x4141

#define	CI_IDENT	"\177CGC\x01\x01\x01\x43\x01\x00\x00\x00\x00\x00\x00"

static int idaapi accept_cgc_file(linput_t *li,
                       char fileformatname[MAX_FILE_FORMAT_NAME], int n) {
   CGC32_hdr hdr;   
   bool hasPtGnuStack = false;
   if(n || qlread(li, &hdr, sizeof(hdr)) != sizeof(hdr)) {
      return 0;
   }
   if (memcmp(&hdr.e_ident, CI_IDENT, 9) || hdr.e_machine != CM_386 || hdr.e_type != CT_EXEC ||
              hdr.e_version != 1) {
      return 0;
   }
   if (hdr.e_phentsize != sizeof(CGC32_Phdr) || hdr.e_phnum < 1 || hdr.e_phnum > (65536U / sizeof(struct CGC32_Phdr)) || 
      (hdr.e_shnum != 0 && (hdr.e_shentsize != sizeof(CGC32_Shdr) || hdr.e_shstrndx >= hdr.e_shnum))) {
      return 0;
   }

   if (qlseek(li, hdr.e_phoff) != hdr.e_phoff) {
      return 0;
   }
   uint32_t phdrSize = hdr.e_phentsize * hdr.e_phnum;
   CGC32_Phdr *p = (CGC32_Phdr*)::qalloc(phdrSize);
   if (p == NULL) {
      loader_failure("Failed to allocate memory for program headers\n");
   } 
   if (qlread(li, p, phdrSize) != phdrSize) {
      ::qfree(p);
      loader_failure("Failed to read program headers\n");
   }

   for (int i = 0; i < hdr.e_phnum; i++) {
      switch (p[i].p_type) {
         case PT_LOAD: case PT_NULL: case PT_PHDR: case PT_CGCPOV2:
            break;
         case 0x6474e551:  //PT_GNU_STACK
            hasPtGnuStack = true;
            break;
         default:
            //Very strict on what is allowed in PHDRs here.
            ::qfree(p);
            return 0;
      }
   }

   ::qfree(p);

   if (hdr.e_shnum > 0) {
      bool fail = false;
      if (qlseek(li, hdr.e_shoff) != hdr.e_shoff) {
         return 0;
      }
      uint32_t shdrSize = hdr.e_shentsize * hdr.e_shnum;
      CGC32_Shdr *s = (CGC32_Shdr*)::qalloc(shdrSize);
      if (s == NULL) {
         loader_failure("Failed to allocate memory for section headers\n");
      } 
      if (qlread(li, s, shdrSize) != shdrSize) {
         ::qfree(s);
         loader_failure("Failed to read section headers\n");
      }
      char *sectNames = (char*)::qalloc(s[hdr.e_shstrndx].sh_size);
      if (sectNames == NULL) {
         loader_failure("Failed to allocate memory for section strings\n");
      } 
      if (qlseek(li, s[hdr.e_shstrndx].sh_offset) != s[hdr.e_shstrndx].sh_offset) {
         return 0;
      }
      if (qlread(li, sectNames, s[hdr.e_shstrndx].sh_size) != s[hdr.e_shstrndx].sh_size) {
         ::qfree(s);
         ::qfree(sectNames);
         loader_failure("Failed to read section strings\n");
      }
      ::qfree(s);
      ::qfree(sectNames);
      if (fail) {
         return 0;
      }
   }
   if (hasPtGnuStack) {
      msg("Warning: CGC32 binary file contains PT_GNU_STACK\n");
   }
   qsnprintf(fileformatname, MAX_FILE_FORMAT_NAME, "CGC 32 Loader");
   return 1;
}

static til_t *cgcti = NULL;

til_t *init_til(const char *tilFile) {
   char err[256];
   *err = 0;
   char tilpath[260];
   get_tilpath(tilpath, sizeof(tilpath));     
   return load_til(tilpath, tilFile, err, sizeof(err));
}

//Load the CGC header data types, then apply the templates
//at the appropriate offsets in the database
void applyCGCHeaderTemplates(uint32_t base, CGC32_hdr *cgc) {
   if (cgcti == NULL) {
      init_til("gnuunx.til");
      cgcti = init_til("cgc.til");
      if (cgcti == NULL) {
         return;
      }
   }   
#if IDA_SDK_VERSION >= 520
   tid_t cgch = import_type(cgcti, -1, "CGC32_hdr");
   tid_t cgcph = import_type(cgcti, -1, "CGC32_Phdr");
   tid_t cgcsh = import_type(cgcti, -1, "CGC32_Shdr");
   tid_t cgcsym = import_type(cgcti, -1, "CGC32_Sym");
#else
#if IDA_SDK_VERSION >= 510
   add_til2("gnuunx.til", ADDTIL_SILENT);
   add_til2("cgc.til", ADDTIL_SILENT);
#else
   add_til("gnuunx.til");
   add_til("cgc.til");
#endif
   tid_t cgch = til2idb(-1, "CGC32_hdr");
   tid_t cgcph = til2idb(-1, "CGC32_Phdr");
   tid_t cgcsh = til2idb(-1, "CGC32_Shdr");
   tid_t cgcsym = til2idb(-1, "CGC32_Sym");
#endif

   doStruct(base, sizeof(CGC32_hdr), cgch);
   if (cgc->e_phoff) {
      doStruct(base + cgc->e_phoff, sizeof(CGC32_Phdr) * cgc->e_phnum, cgcph);
   }
   if (cgc->e_shoff) {
      doStruct(base + cgc->e_shoff, sizeof(CGC32_Shdr) * cgc->e_shnum, cgcsh);
   }
}

static void idaapi load_cgc_file(linput_t *li, ushort neflags,
                      const char * /*fileformatname*/) {
   CGC32_hdr hdr;
   uint32_t minAddr = 0xffffffff;
   uint32_t mainAddr = 0;
   qlseek(li, 0);
   if (qlread(li, &hdr, sizeof(hdr)) != sizeof(hdr)) {
      loader_failure();
   }
   sel_t ds = find_free_selector();
   set_selector(ds, 0);
   if (hdr.e_phoff != 0) {
      CGC32_Phdr *phdrs = new CGC32_Phdr[hdr.e_phnum];
      ssize_t hsz = hdr.e_phnum * sizeof(CGC32_Phdr);
      if (qlseek(li, hdr.e_phoff) != hdr.e_phoff || qlread(li, phdrs, hsz) != hsz) {
         delete[] phdrs;
         loader_failure();
      }
      for (uint32_t i = 0; i < hdr.e_phnum; i++) {
         if (phdrs[i].p_type == PT_LOAD) {
            uint32_t base = phdrs[i].p_vaddr & 0xfffff000;
            if (base < minAddr) {
               minAddr = base;
            }
            uint32_t top = (phdrs[i].p_vaddr + phdrs[i].p_memsz + 0xfff) & 0xfffff000;
            if (hdr.e_shnum == 0) {
               const char *clazz = (phdrs[i].p_flags & PF_X) ? "CODE" : "DATA";
               if (!add_segm(0, base, top, NULL, clazz)) {
                  loader_failure();
               }
            }
            for (uint32_t j = base; j < top; j += 4) {
               patch_long(j, 0);
            }
            file2base(li, phdrs[i].p_offset, phdrs[i].p_vaddr, phdrs[i].p_vaddr + phdrs[i].p_filesz, FILEREG_PATCHABLE);
            segment_t *s = getseg(base);
            if (s != NULL) {
               uint8_t perm = 0;
               //so that we can set 32 bit addressing mode on
               set_segm_addressing(s, 1);  //set 32 bit addressing
               if (phdrs[i].p_flags & PF_X) {
                  perm |= SEGPERM_EXEC;
               }
               if (phdrs[i].p_flags & PF_R) {
                  perm |= SEGPERM_READ;
               }
               if (phdrs[i].p_flags & PF_W) {
                  perm |= SEGPERM_WRITE;
               }
               s->perm = perm;
               s->update();
            }
         }
      }
      delete[] phdrs;
   }

   if (hdr.e_shoff && hdr.e_shnum) {
      CGC32_Shdr *shdrs = new CGC32_Shdr[hdr.e_shnum];
      ssize_t ssz = hdr.e_shnum * sizeof(CGC32_Shdr);
      if (qlseek(li, hdr.e_shoff) != hdr.e_shoff || qlread(li, shdrs, ssz) != ssz) {
         delete[] shdrs;
         return;
      }

      char *sectNames = (char*)::qalloc(shdrs[hdr.e_shstrndx].sh_size);
      if (sectNames == NULL) {
         loader_failure("Failed to allocate memory for section strings\n");
      } 
      if (qlseek(li, shdrs[hdr.e_shstrndx].sh_offset) != shdrs[hdr.e_shstrndx].sh_offset) {
         loader_failure("seek failure seeking to shstrtab\n");
      }
      if (qlread(li, sectNames, shdrs[hdr.e_shstrndx].sh_size) != shdrs[hdr.e_shstrndx].sh_size) {
         delete[] shdrs;
         ::qfree(sectNames);
         loader_failure("Failed to read section strings\n");
      }

      uint32_t symtab = 0;
      uint32_t sym_strtab = 0;
      uint32_t sbase = minAddr;
      
      for (uint32_t i = 0; i < hdr.e_shnum; i++) {
         if (shdrs[i].sh_type == SHT_SYMTAB) {
            symtab = i;
            sym_strtab = shdrs[i].sh_link;
         }
         if (shdrs[i].sh_addr == 0) {
            continue;
         }
         if (shdrs[i].sh_type == SHT_PROGBITS && (shdrs[i].sh_flags & SHF_ALLOC) != 0) {
/*
            if (sbase < shdrs[i].sh_addr) { //create a segment to bridge the gap
               add_segm(0, sbase, shdrs[i].sh_addr, NULL, "DATA");
            }
*/
            const char *clazz = (shdrs[i].sh_flags & SHF_EXECINSTR) ? "CODE" : "DATA";
            add_segm(0, shdrs[i].sh_addr, shdrs[i].sh_addr + shdrs[i].sh_size, sectNames + shdrs[i].sh_name, clazz);
            segment_t *s = getseg(shdrs[i].sh_addr);
            if (s != NULL) {
               uint8_t perm = SEGPERM_READ;
               set_segm_addressing(s, 1);  //set 32 bit addressing
               if (shdrs[i].sh_flags & SHF_EXECINSTR) {
                  perm |= SEGPERM_EXEC;
               }
               if (shdrs[i].sh_flags & SHF_WRITE) {
                  perm |= SEGPERM_WRITE;
               }
               s->perm = perm;
               s->update();
            }
            if (i < (hdr.e_shnum - 1)) {
               sbase = shdrs[i + 1].sh_addr;
            }
         }
         else if (shdrs[i].sh_type == SHT_NOBITS && (shdrs[i].sh_flags & SHF_ALLOC) != 0) {
/*
            if (sbase < shdrs[i].sh_addr) { //create a segment to bridge the gap
               add_segm(0, sbase, shdrs[i].sh_addr, NULL, "DATA");
            }
*/
            add_segm(0, shdrs[i].sh_addr, shdrs[i].sh_addr + shdrs[i].sh_size, sectNames + shdrs[i].sh_name, "DATA");
            segment_t *s = getseg(shdrs[i].sh_addr);
            if (s != NULL) {
               uint8_t perm = SEGPERM_READ;
               set_segm_addressing(s, 1);  //set 32 bit addressing
               if (shdrs[i].sh_flags & SHF_EXECINSTR) {
                  perm |= SEGPERM_EXEC;
               }
               if (shdrs[i].sh_flags & SHF_WRITE) {
                  perm |= SEGPERM_WRITE;
               }
               s->perm = perm;
               s->update();
            }
            if (i < (hdr.e_shnum - 1)) {
               sbase = shdrs[i + 1].sh_addr;
            }
         }
         sbase = shdrs[i].sh_addr + shdrs[i].sh_size;
      }
      ::qfree(sectNames);
      if (symtab) {
         char *strtab = new char[shdrs[sym_strtab].sh_size];
         if (qlseek(li, shdrs[sym_strtab].sh_offset) != shdrs[sym_strtab].sh_offset || 
             qlread(li, strtab, shdrs[sym_strtab].sh_size) != shdrs[sym_strtab].sh_size) {
            delete[] shdrs;
            delete[] strtab;
            return;
         }

         uint32_t numSyms = shdrs[symtab].sh_size / shdrs[symtab].sh_entsize;
         CGC32_Sym *syms = new CGC32_Sym[numSyms];
         ssize_t ssz = numSyms * sizeof(CGC32_Sym);
         if (qlseek(li, shdrs[symtab].sh_offset) != shdrs[symtab].sh_offset || qlread(li, syms, ssz) != ssz) {
            delete[] shdrs;
            delete[] strtab;
            delete[] syms;
            return;
         }
         for (uint32_t i = 1; i < numSyms; i++) {
            if (syms[i].st_name) {
               switch (CGC32_ST_TYPE(syms[i].st_info)) {
                  case STT_FUNC:
                     set_name(syms[i].st_value, strtab + syms[i].st_name, SN_NOWARN);
                     auto_make_code(syms[i].st_value);
                     add_func(syms[i].st_value, BADADDR);
                     if (strcmp(strtab + syms[i].st_name, "main") == 0) {
                        mainAddr = syms[i].st_value;
                     }
                     else if (strcmp(strtab + syms[i].st_name, "_main") == 0) {
                        mainAddr = syms[i].st_value;
                     }
                     break;
                  case STT_OBJECT:
                     set_name(syms[i].st_value, strtab + syms[i].st_name, SN_NOWARN);
                     switch (syms[i].st_size) {
                        case 1:
                           doByte(syms[i].st_value, 1);
                           break;
                        case 2:
                           doWord(syms[i].st_value, 2);
                           break;
                        case 4:
                           doDwrd(syms[i].st_value, 4);
                           break;
                     }
                     break;
               }
            }
         }
         delete[] syms;
         delete[] strtab;
      }
      
      delete[] shdrs;
   }      

   applyCGCHeaderTemplates(minAddr, &hdr);

   create_filename_cmt();
   add_entry(hdr.e_entry, hdr.e_entry, "_start", true);
   inf.filetype = f_CGC;
   set_default_dataseg(ds);
   inf.beginEA = hdr.e_entry;
   if (mainAddr) {
      jumpto(mainAddr);
   }
   else {
      jumpto(hdr.e_entry);
   }
}

// LOADER DESCRIPTION BLOCK
loader_t LDSC = {
  IDP_INTERFACE_VERSION,
  0,
  accept_cgc_file,
  load_cgc_file,
  NULL,
  NULL,
  NULL
};
