
## CNN Basic Operation

Kernel size 3x3.

Stride = 1 (kernel move 1 pixel each step).

Input image 5x5:
```
1 2 3 4 5
2 2 3 4 5
3 2 3 4 5
4 2 3 4 5
5 2 3 4 5
```

Sliding the 3x3 kernel
Row 1 (block 1-3)
```
block1   block2   block3
1 2 3    2 3 4    3 4 5
2 2 3 -> 2 3 4 -> 3 4 5
3 2 3    2 3 4    3 4 5
```

Row 2 (block 4-6)
```
block4   block5   block6
2 2 3    2 3 4    3 4 5
3 2 3 -> 2 3 4 -> 3 4 5
4 2 3    2 3 4    3 4 5
```

Row 3 (block 7-9)
```
block7   block8   block9
3 2 3    2 3 4    3 4 5
4 2 3 -> 2 3 4 -> 3 4 5
5 2 3    2 3 4    3 4 5
```

Kernel 3x3 is:
```
k1 k2 k3
k4 k5 k6
k7 k8 k9
```

The kernel is applied element-wise multiplication with the input (block). Then sum all into a single scalar output for that block.

Example convolution calculation for block1
```
1 2 3   k1 k2 k3   1*k1 2*k2 3*k3
2 2 3 * k4 k5 k6 = 2*k4 2*k5 3*k6
3 2 3   k7 k8 k9   3*k7 2*k8 3*k9
```

then sum it, b1 = 1*k1 + 2*k2 + 3*k3 + 2*k4 + 2*k5 + 3*k6 + 3*k7 + 2*k8 + 3*k9

continue for the rest block.
the final result is:
```
b1 b2 b3
b4 b5 b6
b7 b8 b9
```

The final result is matrix 3x3

Output Formula: ( (input_size - kernel) / stride ) + 1
In this example: ( (5-3) / 1)+1 = 3


## Stride
if stride more than 1, example stride=2, the block will be move in 2 step right or down.

Example data matrix 5x5, and kernel 3x3, stride=2
```
1 2 3 4 5
2 2 3 4 5
3 2 3 4 5
4 2 3 4 5
5 2 3 4 5
```

Based on formula above, the output is:
```
( (5-3) / 2)+1 = 2
```
It will result matrix 2x2

Sliding the 3x3 kernel
Row 1 (block 1-2)
```
block1   block2 (jump right 2 columns)
1 2 3    3 4 5
2 2 3 -> 3 4 5
3 2 3    3 4 5
```

Row 2 (block 3-4), jump down 2 rows
```
block3   block4 (jump right 2 columns)
3 2 3    3 4 5
4 2 3 -> 3 4 5
5 2 3    3 4 5
```

Multiply each blocks with kernel and sum it.
the final result is:
```
b1 b2
b3 b4
```

Larger stride reduces output spatial size, like downsampling.




## Padding
Padding means adding extra pixels (usually zeros) around the border of the input image before applying convolution. This helps control the output size and preserves information near the edges.

Without padding, the output will become smaller. 
With padding=1, output will same with input.
With padding=2, output will larger than input.
By adding padding, it make no loss information from edge images.
Example, using padding=1, the output is same with the input. No loss information to be processed.

Output Formula: ( (input_size - kernel + (2*padding) ) / stride ) + 1

Example: 
1. input=10x10, kernel=3x3, stride=1, padding=0
output = ( (10-3+2*0)/1 ) + 1 = 8
2. input=10x10, kernel=3x3, stride=1, padding=1
output = ( (10-3+2*1)/1 ) + 1 = 10
3. input=10x10, kernel=3x3, stride=1, padding=2
output = ( (10-3+2*2)/1 ) + 1 = 12

Padding will add 0 value surrounding the data
Padding=1
```
0 0 0 0 0 0 0
0 1 2 3 4 5 0
0 2 2 3 4 5 0
0 3 2 3 4 5 0
0 4 2 3 4 5 0
0 5 2 3 4 5 0
0 0 0 0 0 0 0
```
Padding=2
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 1 2 3 4 5 0 0
0 0 2 2 3 4 5 0 0
0 0 3 2 3 4 5 0 0
0 0 4 2 3 4 5 0 0
0 0 5 2 3 4 5 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

Padding prevents spatial shrinking and preserves edge information.
Padding greater than 1 increases the output spatial size beyond input size, adding more context around edges (large border).


## Cascading CNN

CNNs are typically stacked in multiple layers, where the output feature maps of one convolutional layer become the input to the next.




