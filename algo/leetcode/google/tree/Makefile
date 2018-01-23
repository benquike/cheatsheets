CPPSRC:=$(wildcard *.cpp)
OBJS:=$(CPPSRC:%.cpp=%.o)

ALL:test

%.o:%.cpp
	g++ -c -g $^

test:$(OBJS)
	g++ $(OBJS) -o test

clean:
	-rm $(OBJS) test
