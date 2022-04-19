# Exercise 7: Stigmergic Interaction for Smart Colony Optimization

A template for the implementation of an Ant System algorithm [1] for solving the [att48](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/) Travelling Salesman Problem instance. 

[1] Dorigo, M., & St ̈utzle, T. (2004). Ant colony optimization. The MIT Press.

### Project overview
```bash
├── ant-colony.py # the ant colony that behaves base on the Ant System algorithm
├── ant.py # an artificial ant of the ant colony
├── environment.py # the environment of the ant colony
└── att48-specs # specification of the att48 TSP
    ├── att48.opt.png
    ├── att48.opt.tour
    ├── att48.tsp
    ├── att48_coordinates.txt
    └── att48_distance_matrix.txt

```

### How to run the project
Run with [Python 3](https://www.python.org/downloads/): 

```shell
python3 ant-colony.py
```
