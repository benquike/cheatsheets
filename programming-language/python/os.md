# how to use os module

## file operation

### check existence of file or path

```
os.path.exists(path)
```

### delete file/directory

	os.remove()
	os.rmdir()
	shutil.rmtree()

### implementation of touch

	def touch(fname, times=None):
		with open(fname, 'a'):
			os.utime(fname, times)

### change permission bits

```
import os
import stat

st = os.stat('somefile')
os.chmod('somefile', st.st_mode | stat.S_IEXEC)
```

https://stackoverflow.com/questions/12791997/how-do-you-do-a-simple-chmod-x-from-within-python


### copy files

```
from shutil import copyfile

copyfile(src, dst)
```

https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
