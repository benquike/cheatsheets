# graph and visualization


## pygraphviz

http://matthiaseisen.com/articles/graphviz/

## networkx

NetworkX is a Python language software package for the creation,
manipulation, and study of the structure, dynamics, and functions
of complex networks.

https://networkx.github.io/


### Create a complete graph


```
import networkx as nx
G = nx.complete_graph(5)
```

## creating animation

### drawing with networkx

To show the graph, we need to add the last line, as shown
in the following code snippet.

```
import networkx as nx
import matplotlib.pyplot as plt
g1 = nx.petersen_graph()
nx.draw(g1)
plt.show()
```

Where is `graphviz_layout`:

```
from networkx.drawing.nx_agraph import graphviz_layout
```

https://stackoverflow.com/questions/18229563/using-networkx-with-matplotlib-artistanimation
https://github.com/ankurankan/nx_animation
http://ankurankan.github.io/blog/2013/10/11/plotting-and-animating-networkx-graphs/
http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
