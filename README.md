# Lagrange Interpolation

## What is Lagrange Interpolation?
Lagrange Interpolation is a technique to find a polynomial that estimates the value of a function by having some points of the function. for example, if you have values of function `f(x)`for `x=0`, `x=1` and `x=2`, you can use these values to fit a curve to these points and estimate the function in range [0, 2]. 

### Polynomial estimation is unique!
Since there's is only one polynomial with `n-1` degree that can be fitted on `n` data points, the polynomial estimation is unique and the Lagrange interpolation algorithm is mathematically equal to Newton's and other algorithms.


## Installation & Running
There is nothing complicated! just clone the repository and install `prettytable` package. then run the main file:
```
$ git clone https://github.com/artinZareie/Lagrange-interpolation
$ python -m pip install prettytable
$ python main.py
```

The usage is pretty simple.
