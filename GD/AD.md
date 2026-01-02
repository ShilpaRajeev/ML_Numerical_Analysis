### Computing Derivatives

Four ways
1. Manual Differentiation
2. Numerical Differentiation
3. Symbolic Differentiation
4. Automatic Differentiation (AD)

Any complex function can be broken down into a sequence of elementary operations. This sequence is called a **Wengert List**  or an evaluation trace.

The Wengert list directly defines a Directed Acyclic Graph (DAG)


## Automatic Differentiation

Automatic Differentiation assumes a function is evaluated by a sequence of elementary operations (add, multiply, exp, etc.) and attaches derivative information to each intermediate value while respecting the chain rule. Unlike numerical differentiation using finite differences, AD avoids truncation error; unlike symbolic differentiation, it works directly on numbers during execution rather than generating huge symbolic expressions.


## Forward Mode Automatic Differentiation
Forward mode propagates derivatives from inputs to outputs in the same direction as the ordinary computation and is best for functions with few inputs and many outputs. Conceptually, each variable carries a pair (v,v˙), where v is its value and v˙is the derivative of v with respect to some chosen input direction.

## Backward Mode Automatic Differentiation

Reverse mode propagates derivatives from outputs back to inputs and is particularly efficient when there are many inputs and few outputs, such as a loss scalar depending on millions of neural network parameters. It is closely related to backpropagation: first a forward pass computes and stores intermediate values, then a backward pass traverses the graph in reverse to accumulate gradients.


The key trade-off between forward and reverse modes is their asymptotic cost relative to the input and output dimensions. For a function with n inputs and m outputs:​

Forward mode is efficient when n is small and m is large, since each pass effectively computes a Jacobian–vector product (one input direction to all outputs).​

Reverse mode is efficient when n is large and m is small (especially m=1), since one backward sweep gives a vector–Jacobian product (all input derivatives for one output), which is why modern deep learning libraries primarily use reverse mode for gradient computation.

## Jacobian Matrix

If we have multiple fuctions with multiple variables, then the Jacobian matrix captures the possible partial derivatives as a matrix.

