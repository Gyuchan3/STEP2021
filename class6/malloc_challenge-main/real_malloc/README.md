## 作成したコード
+ [`malloc.c`](https://github.com/Gyuchan3/STEP2021/blob/main/class6/malloc_challenge-main/real_malloc/main.c) : Best-fitでmallocして、freeするときに右側が空き領域なら統合する。`my_malloc.c`のコメントの範囲を変えるとFirst-fit, Worst-fitでも実行できる。
+ [`first_fit.c`](https://github.com/Gyuchan3/STEP2021/blob/main/class6/malloc_challenge-main/real_malloc/first_fit.c) : sample_malloc.cの内容を写したもの。
+ [`best_fit.c`](https://github.com/Gyuchan3/STEP2021/blob/main/class6/malloc_challenge-main/real_malloc/best_fit.c) : Best-fit
+ [`worst_fit.c`](https://github.com/Gyuchan3/STEP2021/blob/main/class6/malloc_challenge-main/real_malloc/worst_fit.c) : Worst-fit
+ [`merge.c`](https://github.com/Gyuchan3/STEP2021/blob/main/class6/malloc_challenge-main/real_malloc/merge.c) : freeする領域の両側が空き領域かを考慮する。

## 実行方法

以下のコマンドを実行する。
+ malloc.c

  ```
  make
  make run
  ```
+ その他

  ```
  gcc -O3 -o malloc_challenge.bin main.c <ファイル名> simple_malloc.c -lm
  ./malloc_challenge.bin
  ```

## 結果
simple malloc => my malloc

|           | Challenge 1 | Challenge 2 | Challenge 3 | Challenge 4 | Challenge 5 | 
| --------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | 
| First-fIt | Time: 13 ms => 12 ms<br>Utilization: 70% => 70% | Time: 11 ms => 11 ms<br>Utilization: 40% => 39% | Time: 134 ms => 134 ms<br>Utilization: 7% => 7% | Time: 25045 ms => 25758 ms<br>Utilization: 16% => 15% | Time: 19133 ms => 18935 ms<br>Utilization: 15% => 14% | 
| Best-fit  | Time: 16 ms => 1475 ms<br>Utilization: 70% => 70%|Time: 11 ms => 610 ms<br>Utilization: 40% => 39%|Time: 135 ms => 948 ms<br>Utilization: 7% => 50%|Time: 25041 ms => 10290 ms<br>Utilization: 16% => 71%|Time: 24354 ms => 7163 ms<br>Utilization: 15% => 71%|
| Worst-fit | Time: 17 ms => 1592 ms<br>Utilization: 70% => 70%|Time: 11 ms => 773 ms<br>Utilization: 40% => 39%|Time: 133 ms => 65248 ms<br>Utilization: 7% => 3%|Time: 19647 ms => 681385 ms<br>Utilization: 16% => 7%|Time: 15321 ms => 579671 ms<br>Utilization: 15% => 7%|
|merge-left<br>(Best-fit)| Time: 19 ms => 1164 ms<br>Utilization: 70% => 70%|Time: 11 ms => 566 ms<br>Utilization: 40% => 39%|Time: 134 ms => 942 ms<br>Utilization: 7% => 48%|Time: 19113 ms => 2465 ms<br>Utilization: 16% => 76%|Time: 18076 ms => 2467 ms<br>Utilization: 15% => 75%



## わかったこと

+ Challenge1, 2ではfitの仕方が時間やメモリ効率に与える影響が小さい。
+ Best-fitが最も時間が短く、メモリ効率も良い。Worst-fitは実行時間が非常に長くメモリ効率も非常に悪い。
+ freeする開放領域に隣接する右側の領域も空き領域だった時に統合する場合が最も時間が短くメモリ効率も良い傾向にある。
+ freeする開放領域の両側が空き領域だったときに統合するコードも書いたが、メモリ効率は上がらず計算時間が少し長くなった。freeするときの比較回数が増えたせいだと考えられる。メモリ効率が良くならないのは、隣接左側が空き領域であることが少ないのか、コードが機能していないかだと思っている。

## 疑問

空き領域が繋がっていたときに統合するコードを`my_add_to_free_list`関数に移動しても計算時間はさほど変わらなかった。`my_add_to_free_list`関数が呼ばれるのは`free`が呼ばれる回数よりも多いので計算時間は長くなると予想したのですがなぜなのでしょう。

## 感想

Best-fitの探索をするときにmetadataの単連結リストを前から辿っていくのは時間がかかるので、metadata->sizeの値で木構造を作ったら探索は速くなりそうだと思いました。