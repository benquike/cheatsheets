# Terminal Programs

## teraterm

### Key setting

By default, the `meta` key is disabled in teraterm.
which is not very convenient when using shell, as `meta`
is a frequently used prefix key. To enable it, Memu -> Setup
-> Keyboard -> Meta Key. 

### Connecting to cygwin

We can use teraterm as a terminal of cygwin.[^1]

We can setup logging.

There is some trouble when conncting to 64-bit cygwin.
The solution is in ref[^1](replacing the 32-bit cygterm
with the 64-bit one).

[^1]: http://changineer.info/network/terminal_software/windows_terminal_teraterm.html


## console 2

Console2 can be used to connect to both cygwin and cmd.

1. how to connect to cygwin:ref[^2]
2. A better option is called consoleZ based on Console2[^3].

[^2]: http://bryanlor.com/blog/cygwin-tutorial-integrating-cygwin-console2-windows
[^3]: https://github.com/cbucher/console/wiki/Downloads


## zsh

### oh my zsh

	https://www.smashingmagazine.com/2015/07/become-command-line-power-user-oh-my-zsh-z/

To show the special chars, we need to install this package

	https://github.com/powerline/fonts


On windows, we need to run this command to install the fonts:

	Powershell.exe -executionpolicy remotesigned -File install.ps1
