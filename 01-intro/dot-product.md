# dot product
dot product is basically, multiply each elements of 2 array, row x column, with same shape and then sum of multiplication result. But this is for 1-dim only.

Example 1-dim:
```
u = [1, 2, 3]
v = [ 1
      4
      2 ]
```

Multiply u and v, each elements, [ 1*1 2*4 3*2 ] and sum them 1+8+6 = 15
To visualize, let make array u in horizontal (row) and array v in vertical (column)
```
u . v = [1, 2, 3] . [ 1
                      4
                      2 ]
```

It can be said, multiply corresponding elements of two vectors with the same shape, then add the results together.
In matrix form, it looks like a row vector multiplied by a column vector.
So, the dot product can be seen as a row vector multiplied by a column vector.

The basic concept of "row vector multiplied by a column vector" is applied into matrix with shape more than one.
The rule of dot product is the shape of 2 matrix must align: 
if matrix A shape is (m, n), then matrix B shape must be (n, p) -> result is (m, p).
In other word, number of columns matrix A must be same with number of rows matrix B (n).
And the result is (m,p) 

In example 1-dim above, u.v, the matrix u is 1 row 3 column, it's can be said u have shape (1,3). 
Matrix v is 3 rows 1 column, it's can be said v have shape (3,1). 
Using concept above, u.v is (1,3) . (3,1) and the result is (1x1). 
So in example above, the u.v result is scalar 15.


### dot product with shape larger than 1
Matrix A have shape (2,3)
```
A = [[ a11 a12 a13],
     [ a21 a22 a23]]
```

Matrix B have shape (3,2)
```
B = [[ b11 b12 ],
     [ b21 b22 ],
     [ b31 b32 ]]
```

The dot product of A.B will give result (2,3) . (3,2) = (2,2)
```
A dot B = [[ a11*b11+a12*b21+a13*b31  a11*b12+a12*b22+a13*b32 ],
           [ a21*b11+a22*b21+a23*b31  a21*b12+a22*b22+a23*b32 ]]
```

Each row of A is multiplied with each column of B, and the results are summed to form each element of the new matrix.

Example:
```
A = [[ 1 2 3],
     [ 3 1 0]]

B = [[ 2 1 ],
     [ 1 3 ],
     [ 3 2 ]]

A dot B = [[ 1*2+2*1+3*3  1*1+2*3+3*2 ],
           [ 3*2+1*1+0*3  3*1+1*3+0*2 ]]
        = [[13 13],
           [7  6]]
```


