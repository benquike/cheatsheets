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

## 
[^1]: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
