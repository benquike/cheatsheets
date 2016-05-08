# Type conversions

## Implicit type conversions

### implicit type conversion of basic types and pointers
1. Narrow types can be implicitly converted to wide types without precision lost, e.g, short -> int, float -> double
2. In other cases there will be a warning, using explicit conversion will suppress the warning
3. Pointers:
   - NULL can be converted to any pointer type
   - pointers to any type can be converted to/from void pointers
   - pointers to children classes can be converted to pointers to parent classes.

### implicit type conversion of class objects
#### single argument constructor
```
class A {};
class B {
public:
B(const A& a) {} // used when inplicit conversion from A to B is needed
}
```
#### assignment operator

```
class A {};
class B {
public:
B& operator=(const A& a) { return *this} // used when assign an object of type A to an object of type B.
}
```

#### type-cast operator

```
class A {};
class B {
public:
operator A() {return A();} // used to implicitly convert object of class B to object of class A.
}
```

#### example
Assume that we have a function taking an object of class B as argument, shown as below:
```
void func(B b);
```

If we pass it an object of class A, then that object will be implicitly converted to class A using the single
argument constructor. Using `explicit` keyword before the declaraton of the single argument constructor can disable
this implicit conversion.

```
A a;
func(a); // a will be converted to B by calling B(a)
```

## Explicit conversion
### Fundamental data types
#### Old C style conversion
```
short a = 55;
int b = (int)a;
```

#### C++ functional style conversion
```
short a = 55;
int b = int(a);
```

### Classes
These conversion approaches can be used to class types(pointer) without any syntactic error, but always invloves
runtime error. So for casting functions are imported in C++.

#### dynamic_cast
1. can only be used on class pointers or references
2. ensures that the converted pointer points to a complete object of the destination type
3. If it can not cast the pointer to the destination type, it will return a NULL poiter to indicate failure.
In case of references, it will throw an exception of bad_cast

Internally, the C++ compiler uses runtime type information[^1] to do type checking. If we use neither `dynamic_cast`
nor `typeid`, we can tell the c++ compiler not to generate these information. In case of GCC, the option for this
purpose is `-fno-rtti`.

#### static_class
1. convert pointers among **related classes**
2. invloves no runtime overhead
3. unsafe
3. it can also be used to do implicit convert
- calling single argument constructor or type conversion operator

#### reinterprete_convert
1. converts any pointer to other classes, even unrelated.


#### const_cast
make a pointer const

[^1]: https://en.wikibooks.org/wiki/C%2B%2B_Programming/RTTI
