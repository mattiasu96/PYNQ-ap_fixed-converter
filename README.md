# PYNQ-ap_fixed-converter

## Overview
This repo contains a small code meant to work with PYNQ framework + Vivado/Vitis_HLS tools. 

One of the commonly used data types in FPGA development is the ap_fixed. It can be imported in your Vivado/Vitis HLS using the ```#include <ap_fixed.h>``` directive inside your HLS code. It allows the developer to declare fixed point data types, which are knows to be better than floating point for some applications, since they do not need heavy use of dsp and resources.

PYNQ is a framework that allows the user to control the board using high level Python code. Once the hardware design has been exported and mounted on the board, the developer can rely on Python and its vast amount of libraries to write code and control the hardware. 

However, Python doesn't support ap_fixed data types, so we need to convert our float/int/ecc... Python data types to something that is compatible with our hardware ports/interfaces. 


## Example



