# ssh usage

## enabling x11 forwarding

Setup on both the server side and client side are needed.

On the client side, the `-X` (capital X) option to ssh enables
X11 forwarding, and you can make this the default 
(for all connections or for a specific conection) with ForwardX11 yes in ~/.ssh/config

If you use `-Y`, trusted X11 forwarding will be enabled.

n the server side, X11Forwarding yes must specified in /etc/ssh/sshd_config. Note that the default is no forwarding (some distributions turn it on in their default /etc/ssh/sshd_config), and that the user cannot override this setting.

The xauth program must be installed on the server side. If there are any X11 programs there, it's very likely that xauth will be there. In the unlikely case xauth was installed in a nonstandard location, it can be called through ~/.ssh/rc (on the server!).

Note that you do not need to set any environment variables on the server. DISPLAY and XAUTHORITY will automatically be set to their proper values. If you run ssh and DISPLAY is not set, it means ssh is not forwarding the X11 connection.

To confirm that ssh is forwarding X11, check for a line containing Requesting X11 forwarding in the ssh -v -X output. Note that the server won't reply either way.





## reference
1. https://unix.stackexchange.com/questions/12755/how-to-forward-x-over-ssh-to-run-graphics-applications-remotely
