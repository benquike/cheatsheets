# latex usage

## bibtex
- Collecting citation data and assembly them in a .bib file
We can get the .bib data of papers from a lot of sites, like google scholar, or mendeley. An entry
is usually like this[^1]
```
    @inproceedings {caver,  # the id of this work, we will use this id to cite it
	author = {Byoungyoung Lee and Chengyu Song and Taesoo Kim and Wenke Lee},
	title = {Type Casting Verification: Stopping an Emerging Attack Vector},
	booktitle = {24th USENIX Security Symposium (USENIX Security 15)},
	year = {2015},
	month = Aug,
	isbn = {978-1-931971-232},
	address = {Washington, D.C.},
	pages = {81--96},
	url = {https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/lee},
	publisher = {USENIX Association},
}

```
- citing the refernced work in the paper

Using `\cite{id}` we can cite a piece of work in the paper.

- generating the paper
We need to use the following command sequence to make the reference work.
```
$ latex HexType
```
```
$ bibtex HexType
```
```
$ pdflatex HexType
```
```
$ pdflatex HexType
```

## SageTex

SageTex[^3] is the package which allows us to plot using
results computed by SAGE[^2]

A good tutorial on SageTex is [here](http://www.highschoolmathandchess.com/latex/plotting-with-sagetex/) and [^5] [^6].



## TikZ

TikZ[^4] and PGF are TeX packages for creating graphics programmatically.
TikZ is build on top of PGF and allows you to create sophisticated
graphics in a rather intuitive and easy manner.



## Algorithm

### algorithmic

1. Procedure

```
\Processed
...
\EndProcedure
```

2. connectives

`\And` for `&`; `land` for `/\`.

3. function call

`\Call{func_name}{args}`


Examples[^7][^6][^9].


## Greek alphabet and special symbols

1. Greek alphabet[^10].
2. Distribution of (~) `\sim`.
3. arraows with string on or below it `\xleftarrow`[^13]
4. customizing the lable of a list[^14]. Usage package enumitem and use the label property
of a list or enumerate environment.
5. A good way to figure out how to input special symbols
is to use [Detexify](http://detexify.kirelabs.org/classify.html), where you can write
the symbol and it will tell you what command to use.
6. list of symbols[^15]



Refs[^10][^12]

## Special fonts

Usage includes `\mathcal`

Refs[^11]


## Learning site
*[LaTeX入門](http://medemanabu.net/latex/)

## Books
*[Latex-And-Friends](http://www.stat.wvu.edu/~jharner/courses/stat624/docs/LaTeX-and-Friends.pdf)
*[The TEX Book](http://www.ctex.org/documents/shredder/src/texbook.pdf)
*[Latex Tutorials-A Primer](https://www.tug.org/twg/mactex/tutorials/ltxprimer-1.0.pdf)
*[Latex For the Impatient](http://tug.ctan.org/info/impatient/book.pdf)
*[Writing the first Latex Book](https://www.inf.ethz.ch/personal/gander/talks/vortrag.pdf)
*[Tex By Topic](http://texdoc.net/texmf-dist/doc/plain/texbytopic/TeXbyTopic.pdf)
*[The Not So Short Introduction to Latex](https://tobi.oetiker.ch/lshort/lshort.pdf)

[^1]: http://www.bibtex.org/Using/
[^2]: http://www.sagemath.org/
[^3]: https://www.ctan.org/tex-archive/macros/latex/contrib/sagetex/?lang=en
[^4]: http://www.texample.net/tikz/
[^5]: http://tug.ctan.org/macros/latex/contrib/sagetex/example.pdf
[^6]: http://faculty.essex.edu/~bannon/sp/sagetextexshop.pdf
[^7]: http://tex.stackexchange.com/questions/207667/how-to-add-function-body-to-latex-algorithm-pseudocode
[^8]: http://tex.stackexchange.com/questions/179320/parameter-section-similar-to-input-and-output
[^9]: http://www.cs.toronto.edu/~frank/Useful/algorithm2e.pdf
[^10]: https://www.latex-tutorial.com/symbols/greek-alphabet/
[^11]: http://tex.stackexchange.com/questions/280701/using-mathcal-with-and-without-package
[^12]: http://tex.stackexchange.com/questions/86377/how-can-i-write-tilde-in-math-mode
[^13]: http://medemanabu.net/latex/xleftarrow-xrightarrow/
[^14]: http://tex.stackexchange.com/questions/129951/enumerate-tag-using-the-alphabet-instead-of-numbers
[^15]: https://www.artofproblemsolving.com/wiki/index.php/LaTeX:Symbols

