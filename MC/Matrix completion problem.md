## Matrix completion problem
- Problem: Complete partially observed low-rank matrix
- Assumption: Low rank r<< min(n,d)
- Approach: Convex relaxation 
    - replace rank with Nuclear norm
    - Provable recovery guarantees
- Algorithm: SVT

### Low rank assumption

 The low-rank assumption states that for an n1*n2 matrix M of rank r, we assume min(n1, n2) >> r, meaning the smaller dimension is much larger than the rank.

#### Why the Low-Rank Assumption Matters
The assumption is needed because low-rank matrices have significantly fewer degrees of freedom compared to full-rank matrices, making them more efficient to work with. 


**Degrees of freedom** represents the number of independent parameters that can vary in a system. In the context of matrices and SVD, it's the count of values that are free to vary independently when constructing the matrix.


### Sparse Vector  
A high-dimensional vector where most elements are zero, storing only non-zero values and their indices for efficiency

### Why does Nuclear norm work
Since direct rank minimization is NP-hard, practitioners typically replace the rank function with the nuclear norm (sum of singular values), which is the tightest convex relaxation of rank. This transforms the intractable problem into a tractable convex optimization problem that can be solved efficiently.

### SVT - Singular Value Thresholding
Even though convex, directly solving nuclear norm minimization is expensive for large matrices.

- SVT is a simple, first-order iterative method for solving nuclear norm minimization problems. 
-  It efficiently finds low-rank matrices satisfying convex constraints by repeatedly applying a soft-thresholding operation to singular values.
- The algorithm is built on the singular value shrinkage operator, which is the proximity operator for the nuclear norm.
- SVT is particularly efficient for large-scale problems where the optimal solution has low rank. Rather than computing full SVD, practical implementations compute only the top singular values exceeding the threshold λ using iterative methods. 

### Soft thresholding
singuar values below a threshold are set to 0, promotes low rank by eliminating small singular values

