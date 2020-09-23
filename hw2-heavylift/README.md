## Heavy Lift - Operand Analysis 

Using digital logic to test for carry propagation and carry generation,
determine the average length of the maximum carry chain for 8, 10, 12, 14, and
16 bit additions.

As an example, if you add 0xF to 0xF, that's a 4 bit position carry, so the
maximum length is four. If you add 0x3 to 0x3, that's 2 bits.

You may use any scripting/programming language you like to accomplish this. Just
randomize the input operands for say 10000 samples per bit length.

Here's some explanation to get you started: 
[Wikipedia Article](https://en.wikipedia.org/wiki/Carry-lookahead_adder#Implementation_details)

### Why

This is intended to show you how carry propagate/generate detection works for
more complex adders than ripple carry. Also, it starts to expose a rationale for
"designing for the average case." If you want to know more, you can check this
paper out: 
[An Operand-Optimized Asynchronous IEEE 754 Double-Precision Floating-Point
Adder](https://avlsi.csl.yale.edu/~rajit/ps/fpa.pdf)

