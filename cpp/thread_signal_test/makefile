NAME=test
LINK=g++
CC=gcc
LINKOPTS+= -pthread
CCOPTS+= -std=c++11
CCOPTS+= -g
CCOPTS+= -Wall

SRCS=$(shell find . -iname "*.cpp")
OBJS=$(patsubst %.cpp, %.o, $(SRCS))

$(NAME) : $(OBJS)
	$(LINK) -o $(NAME) $(OBJS) $(LINKOPTS)

.cpp.o:
	$(CC) -c $< $(CCOPTS)

clean:
	rm -f $(OBJS) $(NAME)
	
