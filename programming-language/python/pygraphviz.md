# pygraphviz


python binding for graphviz.

https://stackoverflow.com/questions/35078247/how-to-create-a-dot-file-in-python


## parsing and manipulating dot files in python

[pydot](https://github.com/erocarrera/pydot) can be used.

```
import pydot

## parsing dot file

# graph_from_dot_file returns a list of Dot
dot_files = pydot.graph_from_dot_file('TEST_00003.dot')

dot0 = dot_files[0]

## write to dot file

dot0.write_dot('xxxx.dot')

## write to png file
dot0.write_png('xxxx.png')
```

## reference
2. https://github.com/erocarrera/pydot
1. https://pythonhaven.wordpress.com/2009/12/09/generating_graphs_with_pydot/
