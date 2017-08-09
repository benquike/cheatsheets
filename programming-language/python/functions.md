# functions

## variable argument functions

### Using *args
This is used for defining a vari-arg functions and the arguments
can be accessed by a **list**[^1]

	def test_var_args(f_arg, *argv):
	    print "first normal arg:", f_arg
	    for arg in argv:
	        print "another arg through *argv :", arg
	
	test_var_args('yasoob','python','eggs','test')

This produces the following result:

	first normal arg: yasoob
	another arg through *argv : python
	another arg through *argv : eggs
	another arg through *argv : test

### Using **kwargs
This is used for defining a vari-arg functions and the arguments
can be accessed by a **dict**[^1]


	def greet_me(**kwargs):
	    if kwargs is not None:
	        for key, value in kwargs.iteritems():
	            print "%s == %s" %(key,value)
	
	>>> greet_me(name="yasoob")
	name == yasoob

passing `**kwargs` to another function

```
# python likes
def save(filename, data, **kwargs):
    fo = openX(filename, "w", **kwargs) # <- #1
    fo.write(data)
    fo.close()
# python doesnt like
def save2(filename, data, **kwargs):
    fo = openX(filename, "w", kwargs) # <- #2
    fo.write(data)
    fo.close()

def openX(filename, mode, **kwargs):
    #doing something fancy and returning a file object
```

https://stackoverflow.com/questions/9867562/pass-kwargs-argument-to-another-function-with-kwargs

## 
[^1]: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
