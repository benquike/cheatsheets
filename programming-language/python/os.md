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
