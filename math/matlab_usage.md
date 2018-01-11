## defining vector/matrix


```
a = [1 2 3]

b = [1 2 3; 4 5 6]
```


## tranpose

```
B = A.'
B = transpose(A)
```

## declaring variables

```
syms x1 x2 x3

x = [x1 x2 x3]
```



## exponential expr

```
    exp(x2)
 x1*exp(x2)
  3*exp(x3)

```

## find gradient function

https://www.mathworks.com/help/symbolic/gradient.html


## find the hessian matrix

https://www.mathworks.com/help/symbolic/hessian.html


## inverse matrix

```
inv(X)
```


## scripting

### defining function

```
x = 1:10;
n = length(x);
avg = mymean(x,n);
med = mymedian(x,n);

function a = mymean(v,n)
% MYMEAN Example of a local function.

    a = sum(v)/n;
end

function m = mymedian(v,n)
% MYMEDIAN Another example of a local function.

    w = sort(v);
    if rem(n,2) == 1
        m = w((n + 1)/2);
    else
        m = (w(n/2) + w(n/2 + 1))/2;
    end
end
```

### loop

https://www.mathworks.com/help/matlab/matlab_prog/loop-control-statements.html
