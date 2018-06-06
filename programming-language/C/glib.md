# glib usage

## installation

```
sudo apt-get install libglib2.0-dev
```

## Components

- Memory chunks
- Doubly-linked lists
- Singly-linked lists
- Hash tables
- Strings (which can grow dynamically)
- String chunks (groups of strings)
- Arrays (which can grow in size as elements are added)
- Balanced binary trees
- N-ary trees
- Quarks (a two-way association of a string and a unique integer identifier)
- Keyed data lists (lists of data elements accessible by a string or integer id)
- Relations and tuples (tables of data which can be indexed on any number of fields)
- Caches

## main loop



## Example


```C
#include <stdio.h>
#include <glib.h>
int main(int argc, char** argv) {
  GList* list = NULL;
  list = g_list_append(list, "Hello world!");
  printf("The first item is '%s'\n", (char *)g_list_first(list)->data);
  return 0;
}
```

compilation:

```
gcc test.c `pkg-config --cflags --libs glib-2.0` -o test
```




# reference
1. [GLib Reference Manual](https://developer.gnome.org/glib/stable/)
2. [The GLib/GTK+ Development Platform](https://people.gnome.org/~swilmet/glib-gtk-dev-platform.pdf)
3. [Application Programming Using the GNOME Libraries](http://devernay.free.fr/cours/IHM/GTK/gnome-libs-tutorial.pdf)
4. [The Official GNOME 2 Developer's Guide](https://www.dgsiegel.net/files/tog2dg.pdf)
5. [Glib-C: C as an alternative Object Oriented Environment](http://lore.ua.ac.be/Publications/pdf/Hendrickx2004.pdf)
6. [Object-Oriented Programming in C](https://www.cs.colorado.edu/~kena/classes/5448/f12/presentation-materials/gatchell.pdf)
7. [Manage C data using the GLib collections](https://www6.software.ibm.com/developerworks/education/l-glib/l-glib-pdf.pdf)
8. [Compiling GLib Applications](https://developer.gnome.org/glib/stable/glib-compiling.html)
9. [The Main Loop: The Engine of a GUI Library](http://www.lanedo.com/the-main-loop-the-engine-of-a-gui-library/)
10. [C Programming/GObject](https://en.wikibooks.org/wiki/C_Programming/GObject)
11. [Object-oriented programming with ANSI-C](https://www.cs.rit.edu/~ats/books/ooc.pdf)
