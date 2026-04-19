# GXP Sources

Raw source code for SMC patches, converted to GXP (xeBuild-like) format.

- Glitch3
- Argon Data
- Aud Clamp

## Others

SMC+ and Glitch SMC patches are available in standalone/ as JSON files. Unfortunately these patches are NOT compatible with any other builder. This is because xeBuild hardcoded many of these SMC patches. The JSON files are extremely simple, in "<sig>": "<patch>" format, and could be parsed and applied relatively easily.


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