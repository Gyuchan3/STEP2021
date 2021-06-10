#!/usr/bin/env python3

from os import path
import sys
import math
import random

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# 初期配置のランダムなルートを生成する
def generate_random_tour(N):
    # 初期化
    tour = [i for i in range(N)]
    
    # ランダムに入れ替える
    for i in range(N):
        r1 = random.randint(0, N - 1)
        r2 = random.randint(0, N - 1)
        tour[r1], tour[r2] = tour[r2], tour[r1]
    
    return tour

def generate_greedy_tour(N, dist):
    current_city = random.randint(0, N - 1)
    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(current_city)
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    
    return tour
        
# 2-opt
def swap_cross(cities, dist, N):
    tour = generate_greedy_tour(N, dist) # 毎回計算するの時間の無駄
    # ランダムに入れ替える(greedyのままだと局所最適解にはまる気がしたので)
    for i in range(N // 10 + 1):
        r1 = random.randint(0, N - 1)
        r2 = random.randint(0, N - 1)
        tour[r1], tour[r2] = tour[r2], tour[r1]
        
    # tour = generate_random_tour(N)
    step = 10**3
    for i in range(step):
        # 入れ替え候補の2点をランダムに選ぶ
        r1 = random.randint(0, N - 1)
        r2 = random.randint(0, N - 1)
        
        if r1 > r2: r1, r2 = r2, r1 #r1 < r2にする
        if r2 - r1 <= 2:
            continue #絶対に交差しない
        
        # r1―(r1 + 1) % Nと(r2 - 1 + N) % N―r2が交差している時
        #(r1 + 1) % Nはr1の一つ先。r1 = N - 1のときr1の一つ先が0になる
        #(r2 - 1 + N) % Nはr2の一つ前。r2 = 0のときr2の一つ前がN-1になる
        if (dist[tour[r1]][tour[(r1 + 1) % N]] + dist[tour[r2]][tour[(r2 - 1 + N) % N]]) > (dist[tour[r1]][tour[(r2 - 1 + N) % N]] + dist[tour[r2]][tour[(r1 + 1) % N]]):
            # r1とr2の間を逆向きにする
            while True:
                r1 = (r1 + 1) % N
                r2 = (r2 - 1 + N) % N
                tour[r1], tour[r2] = tour[r2], tour[r1]
                if 0 <= r2 - r1 <= 1: break
        
    path_length = sum(distance(cities[tour[i]], cities[tour[(i + 1) % N]]) for i in range(N))
    
    return tour, path_length
    
    
def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    step = 100
    ans_tour = generate_greedy_tour(N, dist)
    ans_path_length = sum(distance(cities[ans_tour[i]], cities[ans_tour[(i + 1) % N]]) for i in range(N))
    
    for i in range(step):
        tour, path_length = swap_cross(cities, dist, N)
        if path_length < ans_path_length:
            ans_tour = tour
            ans_path_length = path_length
            
    return ans_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
    