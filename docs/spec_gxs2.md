# GXS 2.0 Specification

Largely based on LoaderPatch;


Basic Addr:Data patches are written as:

```
0x6860: 48 00 01 68
```


Multi-line patches are also supported:

```
0x31E0:
    12 31 E7 12 32 41 22 78 A4 B6 00 FA 78 BF E6 30
    E2 07 A2 E3 92 E0 C2 E2 F6 A2 E0 40 05 30 E1 E6
    80 03 20 E1 E1 75 79 E3 30 E1 03 75 79 EB 12 29
    95 20 D5 D2 78 A4 76 04 78 BF E6 D2 E2 A2 E1 92
    E3 F6 22 C0 00 78 C1 E6 43 BF 01 B5 77 02 80 0B
    A6 77 B4 15 05 B6 01 02 80 01 D3 53 BF FE D0 00
    22 78 C0 79 BF E7 20 86 02 76 00 B6 00 11 C2 85
    C2 E1 F7 20 E0 14 30 86 11 79 C2 77 FF 80 2C B6
```



## PPC ASM

PowerPC ASM patches are compiled to hex during the conversion process:

```
[ASM] 0xE70:
	mfmsr   %r5 
        li      %r6, 0x10
        andc    %r6, %r5, %r6
```

### Compilation Process

ASM sections are compiled using platform-specific toolchains:

**Linux:**
- Uses `powerpc-linux-gnu-as` from GNU binutils
- Requires `powerpc-linux-gnu-objcopy` for binary extraction

**Windows:**
- Uses `xenon-as.exe` from Xenon GCC toolchain
- Requires `xenon-objcopy.exe` for binary extraction

**macOS:**
- **Not supported** - ASM compilation will fail with error message

### Macro Support

ASM sections have access to standard PowerPC register definitions and xeBuild-compatible macros:
- Register definitions: `hrmor`, `hsprg0`, `ctr`, `lr`, etc.
- Base address: `KBASE, 0x80000000`
- Standard PowerPC instructions and syntax

### Example Conversion

Input ASM:
```
[ASM] 0xE70:
	mfmsr   %r5 
        li      %r6, 0x10
        andc    %r6, %r5, %r6
```

Compiled Output:
```
0xE70: 7C A0 02 A6 38 60 00 10 7C C6 23 78
```