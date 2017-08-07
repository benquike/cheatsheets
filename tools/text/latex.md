# latex usage

## defining new command

To define a new command, use the following format:

```
\newcommand{name}[num]{definition}
```

`num` means the number of arguments in the argument. In `definition`,
we can use `#1`, `#2`, ... to refer the arguments.

The following is an example:

```
\newcommand{\wbalsup}[1] {
      This is the Wikibook about LaTeX 
        supported by #1}
```


## cross referencing

First define a lable using `\label{mark}`, then refer
it using `\ref{}`.

Use `autoref` will help adding label type to the
reference location.

https://tex.stackexchange.com/questions/137432/whats-the-difference-between-ref-and-autoref


## change the label of a list

Use `enumitem` package.

```
\usepackage{enumitem}
...
\begin{enumerate}[label=\Alph*]
\item this is item a
\item another item
\end{enumerate}
```

## trouble shooting

### enumitem conflicts with IEEEtran

Fix:

```
\let\labelindent\relax
```

https://tex.stackexchange.com/questions/170772/command-labelindent-already-defined

## reference
1. https://en.wikibooks.org/wiki/LaTeX/Macros
2. https://www.sharelatex.com/learn/Referencing_Figures
3. https://tex.stackexchange.com/questions/2291/how-do-i-change-the-enumerate-list-format-to-use-letters-instead-of-the-defaul
