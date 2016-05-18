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

[^1]: http://www.bibtex.org/Using/