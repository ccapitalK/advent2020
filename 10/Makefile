PROGRAM = advent10
OBJS = main.o
CXXFLAGS = -g -Os -std=c++2a
LDFLAGS = -lcore

all: $(PROGRAM)

$(PROGRAM): $(OBJS)
	$(CXX) -o $@ $(OBJS) $(LDFLAGS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ -c $< 

clean:
	rm $(OBJS) $(PROGRAM)

run:
	./$(PROGRAM)
