# Basic NumPy

## 1.1. Creating Arrays

In NumPy, arrays can be created directly from Python lists or with special functions that generate pre-filled arrays.

Creating from lists:
* 1-dim array, shape (3,)
```
a = np.array([1, 2, 3]) 
```

* 2-dim array shape (1,3)
```
b = np.array([[1, 2, 3]]) 
```

* 2-dim array, shape (3,1)
```
c = np.array([[1], [2], [3]]) 
```

* 2-dim array shape (2, 3)
```
d = np.array([[1, 2, 3], [4, 5, 6]]) 
```

* 2-dim array shape (3, 2)
```
e = np.array([[1, 2], [3, 4], [5, 6]]) 
```

Note:
np.array([1, 2, 3]) has shape (3,) (1D).



NumPy provides functions for initializing arrays with default values:
* zeros
  ```
  np.zeros(4) # 1D array of 4 zeros, shape (4,)
  np.zeros((2,3)) # 2D array of zeros, shape (2,3)
  ```

* ones
  ```
  np.ones(4) # 1D array of 4 ones
  np.ones((2,3)) # 2D array of ones, shape (2,3)
  ```

* full
  ```
  np.full(1, 4) # 1D array with value 4
  np.full((2,3), 4) # 2D array (2x3) filled with 4
  ```
  The data type is int64. 
  To change to float64, add decimal or set dtype parameter:
  - np.full(1, 4.0) # 1D array float64 by default (4.0)
  - np.full(1, 4, dtype=np.float64) # 1D with value 4.0 explicitly float64

* arange(p1, p2, p3)
  Create an array with start from p1 (default 0), end stop before p2, step size is p3.
  Example: 
  ```
  np.arange(0, 10, 3) # will create array with data start from 0, and step in 3 until before 10.
  array([0, 3, 6, 9])
  ```

* linspace(p1, p2, p3)
  Create an array with start from p1 (default 0), end at p2, with p3 is number of points (include start and end)
  Example:
  ```
  np.linspace(0, 10, 6) # will create array with 6 elements (include 0 and 10 as start and end). So it will contain 4 additional item (so total 6, with start and end).
  array([ 0.,  2.,  4.,  6.,  8., 10.])
  ```

* eye(n, m, k)
  Create identity matrix, with size (n,m). Parameter k is index of the diagonal. if k = 0, main diagonal. k negative, below the main diagonal. k positive, above the main diagonal. 
  Example:
  ```
  np.eye(3, k=0) # will create identity matrix 3x3
  array([[1., 0., 0.],
         [0., 1., 0.],
         [0., 0., 1.]])

  np.eye(3, k=-1) # will create identity matrix 3x3, below the main diagonal
  array([[0., 0., 0.],
         [1., 0., 0.],
         [0., 1., 0.]])

  np.eye(3, k=1) # will create identity matrix 3x3, above the main diagonal
  array([[0., 1., 0.],
         [0., 0., 1.],
         [0., 0., 0.]])
  ```



## 1.2. Arithmetic Operations (+, -, *, /)

In NumPy, arithmetic operations are element-wise. And arrays must have the same shape.
A and B have same shape (4,).
```
A = np.array([1, 2, 3, 4])
B = np.array([2, 3, 4, 5])

A+B = [3 5 7 9]
A-B = [-1 -1 -1 -1]
A*B = [ 2  6 12 20]
A/B = [0.5 0.66666667 0.75 0.8 ]
```
When doing arithmetic with a scalar, the operation applies to every element.
Example: A+2, it will add every element in A with 2.
A+2 = [3 4 5 6]


## 1.3. Comparison & Boolean Operations

In NumPy lets you compare arrays element-wise and filter data using boolean masks.
The comparison is done by comparing every elements one by one.

Example:
```
a = np.array([1, 2, 3])
b = np.array([1, 3, 3])
print(a == b)
[True False True]
```
When comparing a and b, it will check every element, 1==1, 2==3, 3==3. And the result is an array with value true/false.

The comparison operator are:
* Equal, ==
* Not Equal, !=
* Greater, >
* Less, <
* Greater and equal, >=
* Less and equal, <=


### Boolean masking
We can filter an array, using boolean masking, to get the result that is true.
Example, array a contains elements [1,2,3]. And we want to get value that greater than 1.
First, create mask with condition a > 1
```
mask = a > 1
print(mask)
[False True True]
```
Than apply mask into a
```
a1 = a[mask]
print(a1)
[2 3]
```
It keeps only the elements where the condition is True (values greater than 1).


### Logical Operations (&, |, ~)
With logical operations (and &, or |, not ~), we can define multiple condition/filter.
Example
```
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```
AND example: values must greater than 2 and less than 5.
```
# create mask
mask = (a > 2) & (a < 5)
a1 = a[mask]
print(a1)
[3 4]
```

OR example: values must less than 3 or greater than 7.
```
mask = (a < 3) | (a > 7)
print(a[mask])   
[1 2 8 9]
```

NOT example: values not greater than 5.
```
mask = ~(a > 5)
print(a[mask])
[1 2 3 4 5]
```


## 1.4. Dot Product
In NumPy, dot product can be calculate using np.dot or @.

Example:
```
A = np.array([[1, 2], [3, 4]])
B = np.array([[10, 20], [30, 40]])

np.dot(A,B)
A @ B

[[ 70 100]
 [150 220]]
```


## 1.5. Reshape & Basic Indexing

In NumPy, an array can be reshaped into a different dimension (rows, columns), but the total number of elements must remain the same.
Reshape does not change the data, only how it’s viewed.

Example, original shape is (9,), it can be reshape to (3,3), (9,1), (1,9), (9,1,1) etc.
The product of dimensions must match the original size (9 here).
* (3,3) = 3x3
* (9,1) = 9x1
* (1,9) = 1x9
* (9,1,1) = 9x1x1
```
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a1 = a.reshape(3, 3)
a2 = a.reshape(9, 1)
a3 = a.reshape(1, 9)

a1 = [[1 2 3]
      [4 5 6]
      [7 8 9]]

a2 = [[1]
      [2]
      [3]
      [4]
      [5]
      [6]
      [7]
      [8]
      [9]]

a3 = [[1 2 3 4 5 6 7 8 9]]
```

### Basic Indexing
NumPy arrays can be access the elements by using indexing.
The index is start from 0.
1D example:
* Get first element, a[0] ->  Result = 1
* Get third element, a[2] ->  Result = 3
* Get value from index 1-4, a[1:4] ->  Result = [2,3,4]
* Get first 3, a[:3] ->  Result = [1,2,3]
* Get from index 3 until end, a[3:] ->  Result = [4,5,6,7,8,9]

For 2-dim or more, it's same concept with 1-dim.
The same concept works for higher dimensions (3D, 4D, etc.), just add more indexes separated by commas.
Example:
```
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
```
Array b can be visualize:
```
      Col0  Col1  Col2
Row0   1     2     3
Row1   4     5     6
Row2   7     8     9
```

* Get first row, b[0]
  Result = [1 2 3]
* Get first column, b[:,0]
  Result = [1 4 7]
* Get value of second row (Row1), third column (Col2), b[1,2]
  Result = 6





