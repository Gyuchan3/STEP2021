# 結果
simple malloc => my malloc

|           | Challenge 1 | Challenge 2 | Challenge 3 | Challenge 4 | Challenge 5 | 
| --------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | 
| First-fIt | Time: 13 ms => 12 ms<br>Utilization: 70% => 70% | Time: 11 ms => 11 ms<br>Utilization: 40% => 39% | Time: 134 ms => 134 ms<br>Utilization: 7% => 7% | Time: 25045 ms => 25758 ms<br>Utilization: 16% => 15% | Time: 19133 ms => 18935 ms<br>Utilization: 15% => 14% | 
| Best-fit  |Time: 17 ms => 1576 ms<br>Utilization: 70% => 70% |Time: 11 ms => 769 ms<br>Utilization: 40% => 39%|Time: 131 ms => 1021 ms<br>Utilization: 7% => 50%|Time: 23869 ms => 11336 ms<br>Utilization: 16% => 71%|Time: 19024 ms => 7214 ms<br>Utilization: 15% => 71%|
| Worst-fit | Time: 17 ms => 1592 ms<br>Utilization: 70% => 70%|Time: 11 ms => 773 ms<br>Utilization: 40% => 39%|Time: 133 ms => 65248 ms<br>Utilization: 7% => 3%|Time: 19647 ms => 681385 ms<br>Utilization: 16% => 7%|Time: 15321 ms => 579671 ms<br>Utilization: 15% => 7%|



# Real malloc challenge!

## Instruction

Your task is implement a better malloc logic in [malloc.c](malloc.c) to improve the speed and memory usage.

## How to build & run a benchmark

```
# build
make
# run a benchmark
make run
```

If the commands above don't work, you can build and run the challenge directly by running:

```
gcc -Wall -O3 -lm -o malloc_challenge.bin main.c malloc.c simple_malloc.c
./malloc_challenge.bin
```

## Acknowledgement

This work is based on [xharaken's malloc_challenge.c](https://github.com/xharaken/step2/blob/master/malloc_challenge.c). Thank you haraken-san!
