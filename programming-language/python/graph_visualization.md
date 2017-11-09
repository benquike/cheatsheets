# graph and visualization


## pygraphviz

http://matthiaseisen.com/articles/graphviz/
https://blog.laisky.com/p/pygraphviz/


## lolviz

https://github.com/parrt/lolviz

## networkx

NetworkX is a Python language software package for the creation,
manipulation, and study of the structure, dynamics, and functions
of complex networks.

https://networkx.github.io/

## matplotlib

## wxPython

https://www.wxpython.org/


Installation:

```
sudo apt-get install python-wxgtk3 python-wxtools wx3-doc wx3-examples wx3-headers wx3-i18n
```

## NodeBox

https://www.nodebox.net/code/index.php/Graph


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

### animation

```python
import numpy as np
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from networkx.drawing.nx_agraph import graphviz_layout

G = nx.Graph()
G.add_edges_from([(0,1),(1,2),(2,0)])
fig = plt.figure(figsize=(8,8))

pos=graphviz_layout(G)
nc = np.random.random(3)
nodes = nx.draw_networkx_nodes(G,pos,node_color=nc)
edges = nx.draw_networkx_edges(G,pos)


def update(n):
  nc = np.random.random(3)
  nodes.set_array(nc)
  return nodes,

anim = FuncAnimation(fig, update, interval=50, blit=True)

plt.show()
```

Where is `graphviz_layout`:

```
from networkx.drawing.nx_agraph import graphviz_layout
```

Directional graph:

```
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])

nx.draw_networkx(G)
plt.show()
```

Other examples:

[Bayes updates](https://matplotlib.org/examples/animation/bayes_update.html)
[dynamic_image](https://matplotlib.org/examples/animation/dynamic_image.html)
[strip_chart_demo](https://matplotlib.org/examples/animation/strip_chart_demo.html)

https://stackoverflow.com/questions/18229563/using-networkx-with-matplotlib-artistanimation
https://github.com/ankurankan/nx_animation
http://ankurankan.github.io/blog/2013/10/11/plotting-and-animating-networkx-graphs/
http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
