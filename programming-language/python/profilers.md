#python profilers

`cProfile` and `profile` provide deterministic profiling of Python programs.[^1]


## cProfile Usage

### how to run cProfile

1. From Program

	import cProfile
	cProfile.run("foo()", "foo.profile")

2. Outside of program

	python -m cProfile -o barbazzr.profile barbazzr.py

### view the profiling data

1. kcachegrind[^2][^5]
2. runsnakerun[^3]
3. snakeviz[^4]
4. pstats[^6]

[^1]: https://docs.python.org/2/library/profile.html
[^2]: http://kcachegrind.sourceforge.net/html/Home.html
[^3]: http://www.vrplumber.com/programming/runsnakerun/
[^4]: https://jiffyclub.github.io/snakeviz/
[^5]: https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara
[^6]: http://stefaanlippens.net/python_profiling_with_pstats_interactive_mode
