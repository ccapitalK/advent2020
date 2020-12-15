PROGRAM = little
OBJS = main.o
CXXFLAGS = -g -Os -std=c++2a

all: $(PROGRAM)

$(PROGRAM): $(OBJS)
	$(CXX) -o $@ $(OBJS) -lcore

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c $< 

clean:
	rm $(OBJS) $(PROGRAM)

run:
	./$(PROGRAM)
