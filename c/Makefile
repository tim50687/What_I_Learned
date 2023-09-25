CFLAGS = -Wall -g # doesn't hurt to include both during compiling and linking
# target: dependencies
#   action

# if the first target is built, it stop

all: ex1  # If you want to build multiple target (each target you want to build)

ex1: ex1.o ex2.o
	gcc $(CFLAGS) ex1.o ex2.o -o ex1

ex1.o: ex1.c
	gcc $(CFLAGS) -c ex1.c

ex2.o: ex2.c
	gcc $(CFLAGS) -c ex2.c

clean:
	rm -f ex1

