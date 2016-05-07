# port knocking

Port knocking is a technique used to hide some service. Some service
is running on some server, but it does not listen on a port, the client
side must `knock` the server side by sending several tcp sync packet to
some ports in a given order, then the server side will try to connect
the client side.

Refs[^1][^2].

[^1]: https://en.wikipedia.org/wiki/Port_knocking
[^2]: http://www.portknocking.org/
