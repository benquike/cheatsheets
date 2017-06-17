# Daily Usage

## Job management

### Suspend a job ###
{% highlight shell %}
$ Ctrl-z
{% endhighlight %}

### Put a job in the background ###

{% highlight shell %}
$ bg
{% endhighlight %}

### View all the background jobs

{% highlight shell %}
$ jobs
{% endhighlight %}

### Put a job in the foreground ###

{% highlight shell %}
$ fg %1
{% endhighlight %}

## Shell programming

### get the path of a script

    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

is a useful one-liner which will give you the full directory name
of the script no matter where it is being called from.[^1]


## wild card

to match number range

```
mv some/dir/{1..10}.txt ..
```

[^1]: http://stackoverflow.com/questions/59895/can-a-bash-script-tell-which-directory-it-is-stored-in
