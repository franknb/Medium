# Notes on Experimental PlaidML Hardware Config

Run this command to setup PlaidML: 

```
plaidml-setup
```
You should see this output:
```
PlaidML Setup (0.7.0)

Thanks for using PlaidML!

The feedback we have received from our users indicates an ever-increasing need
for performance, programmability, and portability. During the past few months,
we have been restructuring PlaidML to address those needs.  To make all the
changes we need to make while supporting our current user base, all development
of PlaidML has moved to a branch — plaidml-v1. We will continue to maintain and
support the master branch of PlaidML and the stable 0.7.0 release.

Read more here: https://github.com/plaidml/plaidml

Some Notes:
  * Bugs and other issues: https://github.com/plaidml/plaidml/issues
  * Questions: https://stackoverflow.com/questions/tagged/plaidml
  * Say hello: https://groups.google.com/forum/#!forum/plaidml-dev
  * PlaidML is licensed under the Apache License 2.0


Default Config Devices:
   llvm_cpu.0 : CPU (via LLVM)
   metal_amd_radeon_pro_vega_ii_duo.1 : AMD Radeon Pro Vega II Duo (Metal)
   metal_amd_radeon_pro_vega_ii_duo.0 : AMD Radeon Pro Vega II Duo (Metal)

Experimental Config Devices:
   llvm_cpu.0 : CPU (via LLVM)
   opencl_amd_radeon_pro_vega_ii_duo_compute_engine.1 : AMD AMD Radeon Pro Vega II Duo Compute Engine (OpenCL)
   opencl_amd_radeon_pro_vega_ii_duo_compute_engine.0 : AMD AMD Radeon Pro Vega II Duo Compute Engine (OpenCL)
   metal_amd_radeon_pro_vega_ii_duo.1 : AMD Radeon Pro Vega II Duo (Metal)
   metal_amd_radeon_pro_vega_ii_duo.0 : AMD Radeon Pro Vega II Duo (Metal)

Using experimental devices can cause poor performance, crashes, and other nastiness.

```
I was offered this choice, and went **bold** with a `y`
```
Enable experimental device support? (y,n)[n]:y



Multiple devices detected (You can override by setting PLAIDML_DEVICE_IDS).
Please choose a default device:

   1 : llvm_cpu.0
   2 : opencl_amd_radeon_pro_vega_ii_duo_compute_engine.1
   3 : opencl_amd_radeon_pro_vega_ii_duo_compute_engine.0
   4 : metal_amd_radeon_pro_vega_ii_duo.1
   5 : metal_amd_radeon_pro_vega_ii_duo.0
```

You can see I chose one of the experimental devices on my new Mac Pro `CheeseGrater`

```
Default device? (1,2,3,4,5)[1]:2

Selected device:
    opencl_amd_radeon_pro_vega_ii_duo_compute_engine.1

Almost done. Multiplying some matrices...
Tile code:
  function (B[X,Z], C[Z,Y]) -> (A) { A[x,y : X,Y] = +(B[x,z] * C[z,y]); }
Whew. That worked.

Save settings to /Users/gogginsS/.plaidml? (y,n)[y]:y
Success!
```
