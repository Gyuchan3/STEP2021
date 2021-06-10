#!/usr/bin/env python3

from common import format_tour, read_input

import mysolver

CHALLENGES = 7

    
def generate_myoutput():
    for i in range(CHALLENGES):
        cities = read_input(f'input_{i}.csv')
        solver, name = (mysolver, 'output')
        tour = solver.solve(cities)
        with open(f'{name}_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':  
    generate_myoutput()