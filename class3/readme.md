# class3

プログラムは[`modularized_calculator.py`](https://github.com/Gyuchan3/STEP2021/blob/main/class3/modularized_calculator.py)である。

## 実行方法

```
$ python3 modularized_calculator.py
```

## 宿題1

掛け算と割り算に対応するために、関数`read_mul`と`read_divide`を追加し、tokenの種類を増やした。式の一回目の評価で関数`calc_mul_divide`を使用して掛け算と割り算の計算を処理している。

### `calc_mul_divide`について

引数にtokensを受け取り、掛け算と割り算の計算を済ませてtokensを直接編集する。

例) 1+2*3+4を計算する時

```
indexを^の位置で示す。
indexが'*'の位置に来た時
1+2*3+4
   ^
indexの一つ前と一つ後ろがnumberであることを確認し、indexの一つ前を掛け算結果にする。
1+6*3+4
   ^
indexの位置の要素をtokensから削除し
1+63+4
   ^
掛ける数の要素もtokensから削除する。
1+6+4
   ^
```

## 宿題3

括弧に対応するために関数`read_bra`と`read_ket`を追加し、tokenの種類を増やした。括弧関連の処理は関数`process_brackets`で行う。現在は括弧が1組のときのみ対応している。

### 関数`process_brackets`について

`tokens`を受け取り、括弧の中身が計算された状態の`no_braket_tokens`を返す。`tokens`の中身を調べ、括弧の範囲外であるときは`no_braket_tokens`に`tokens`の内容をそのまま追加する。括弧の始まりを判定したら、括弧が終わるまで中身を`inside_braket`に追加し、括弧の中身の式を関数`evaluate`によって計算する。

`flag_bra`は複数括弧にも対応するのに使えないかと思って書いてあるだけであり、現在のコードでは機能していない。
