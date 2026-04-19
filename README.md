# GXP Sources

Raw source code for SMC patches, converted to GXP (xeBuild-like) format.

- Glitch3
- Argon Data
- Aud Clamp

## Others

SMC+ and Glitch1/2 can be applied on top of other patches. Instead of building a binary for every possibility, SMC+ and Glitch1/2 SMC patches are integrated directly into [gxBuild](https://github.com/ExposureMG/gxBuild).

As for CR4 SMC:

Do we even need it? The CR4 glitcher is obsolete and for the most part is only used by collectors. If you *really* need CR4 SMC, couldn't you just use an ECC? gxBuild supports parsing, building and applying ECCs fine.


## Developer

The GXP format is nearly exactly the same as xeBuild. I have kept it fully forwards compatible, where no patch code has to be changed from xeBuild to GXP. 

All patches built for xeBuild will work on gxBuild; The major difference is a 16-byte header at the beginning to stop backwards compatibility. xeBuild has no SMC patchfile system, and would interpret 4-section RGH patches as JTAG patches.


## License

Leaving unlicensed as no party involved has given me permission.

- JTAG by [tmbinc](), [GliGli]() and [Tiros]()
- Glitch3 SMC by [15432]()
- SMC+ by [15432]() and [Octal450]()
- Smc360 Research by [wurthless-elektroniks]()
- x360utils JTAG SMC patcher by [Swizzy]()
- Glitch1/2 SMC patcher by [c0z]
- ~~RJTAG and CR4 by Team Xecuter~~ No credit deserved