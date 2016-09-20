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

Examples[^7][^6][^9].


[^1]: http://www.bibtex.org/Using/
[^2]: http://www.sagemath.org/
[^3]: https://www.ctan.org/tex-archive/macros/latex/contrib/sagetex/?lang=en
[^4]: http://www.texample.net/tikz/
[^5]: http://tug.ctan.org/macros/latex/contrib/sagetex/example.pdf
[^6]: http://faculty.essex.edu/~bannon/sp/sagetextexshop.pdf
[^7]: http://tex.stackexchange.com/questions/207667/how-to-add-function-body-to-latex-algorithm-pseudocode
[^8]: http://tex.stackexchange.com/questions/179320/parameter-section-similar-to-input-and-output
[^9]: http://www.cs.toronto.edu/~frank/Useful/algorithm2e.pdf