
java -cp ./tools/openapi-generator-cli.jar:./tools/fastapi-custom-server-openapi-generator-1.0.0.jar org.openapitools.codegen.OpenAPIGenerator generate -g custom-python-fastapi -i ./api/openapi.yaml 

wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.3.0/openapi-generator-cli-6.3.0.jar -O ./tools/openapi-generator-cli.jar-


以下のような構成でgenerateしたい
```
.
├── apis
│   └── tags
│       └── api(endpoint)
│           └── methods
│               ├── delete
│               ├── get
│               ├── post
│               └── put
│       └── api2
│           └── methods
│               ├── delete
│               ├── get
│               ├── post
│               └── put
└── models
    ├── commons
    └── schema
        └── tags
            └── commons
```

## Step1 MakeFile作成
Java使用経験が少ないかつ毎度のjarファイル作成が面倒なのでコマンド化
以降面倒なコマンドラインでの処理は出来るだけMakeFileに記述して簡略化を試みる

## Step2 コードリーディング  

とりあえず生成するときに必要になるだろうファイル目星つける  
継承関係
- FastapiCustomServerGenerator.java
- AbstractPythonCodegen.java
- DefaultCodegen.java


OpenAPIGenrator DefaultCodegen 継承

DefalutCodegen.java はCodegenConfig をimplements
>implementsって何 => interfaceを呼び出せるっぽい

CodegenConfig.java   => こいつが側みたいな役割

DefalutGenerator.java 
コマンド実行時にopen.apiから各ファイルにgenerateしている処理がここっぽい
Generator をimplementsしている。

OpenAPIGenerator　生成関連？実行時に使用しているのはおそらくこれ

## Step3 generateしたものが動くのか
とりあえずは公開されている方で実行して問題ないか確認

## Step4 独自のtemplateファイルを指定しても動くか
とりあえずは公開されている方で実行して問題ないか確認

## Step5 custom generator の作成
今回は　generate の引数に　fastapi-custom-
./openapi-custom-generator の以下が  
Step5によって作成したもの

## Step6 custom generatorの修正
とりあえずディレクトリ構成いじれそうな変数見つけて修正していく  
- apiをタグごとに分けることは可能
- http method と　api endpointの情報を持っている雰囲気がない。。。

## Step7 generatorそのものをカスタマイズする
- http method と　api endpointの情報を持っている雰囲気がない。。  
これに対応する。一つずつ処理することで実現可能

api(endpoint)　の部分をどう表現するのが適切か

- URLをディレクトリ名としたとき対応関係がわかりやすいがデメリットとしてURLが長くなった時に管理が大変になる。
- operationIDをディレクトリ名とした時　可読性は上がることが見込めるが、一目でどのAPIかわからない可能性がある  
  またSwagger UIで表示した時にoperationIDが表示されないため参照しづらい
- URLの階層ごとにディレクトリを作成するか  ネストを辿ることに時間を費やしそうな印象、見た目は個人的には好き

ディレクトリ名をoperationIDにして　APIのdescriptionにoperationIDを記述する流れが一番、作成者・閲覧者のコストが掛からなそうなので
今回はoperationIDで作成する　イメージは以下のようになる


```
├── apis
│   └── tags
│       └── operationID
│           └── methods
│               ├── delete
│               ├── get
│               ├── post
│               └── put
│       └── operationID
│           └── methods
│               ├── delete
│               ├── get
│               ├── post
│               └── put
```

上記で対応試みていたが,operationIDは一意なため無駄にネストが無駄になる。
なのでURLをディレクトリ名とする方針に転換
スラッシュをアンダースコアに変換してディレクトリ化するなお一文字目のアンダースコアは除外する
```
├── apis
│   └── tags
│       └── URL
│               ├── delete
│               ├── get
│               ├── post
│               └── put
│       └── URL
│               ├── delete
│               ├── get
│               ├── post
│               └── put
```
いい感じ！

model fileの作成ではx-tags　プロパティを使うことができるようだが、generatorの情報として取得できない
今回はスキーマ名の_区切りの最初の値をタグと同じ値としてディレクトリを分けることで、対応する。
イメージ
└── models
    └── tags(_区切りの最初の値)
    └── commons(_区切りの最初の値)

更新：
＿区切りの最初だけでなく＿区切りした場合階層をネスト化していく

EX:) tags_commons_order_response
```
└── models  
    └── tags
        └── commons
            └── order
                └──response.py
```

## Step8 カスタマイズされた状態でファイル実行できるように修正する。

ディレクトリ構成変更後にtemplateから生成されるファイルのimport先が既存の状態のままなので修正する
model側の修正は問題なさそう

api側の修正は目処としてはdefaultGeneratorのclassnameをディレクトリと同じ形式にする方法を検討

import pathを変更成功

as の部分が重複するので対応が必要
=> mustache templateの変更で実現可能　（classname）

実行パス周りで修正を重ねてとりあえず動く状態になった。

課題  
- モジュールのパスが他の環境でも通るかの確認
- ネストが深いAPIでも生成処理問題ないか
- 定義書変更するたびにgenerateディレクトリを削除することになるので実際の使用方法の検討


## Step9 課題に対する解決策考案
### モジュールのパスが他の環境でも通るかの確認  
=> 最終的に、作成したAPIをAWS　Lambdaで動作確認するので
この問題は動作確認ができたら良い。一旦スキップ。
問題がある場合は実行パスの追加方法に問題がありそう。
.pthにpath書く方法を初めて試したが、絶対パスしか通らない？  
ファイルはsite-packageに配置推奨

### ネストが深いAPIでも生成処理問題ないか  
=> 実際にネストが深いAPIを新規でyaml定義書に作成し生成実行後、
問題ないかどうかの確認
簡易的にネストが深いAPIを作成したが問題なさそう

### 定義書変更するたびにgenerateディレクトリを削除することになるので実際の使用方法の検討  
現時点で思いついた方法
- API実行関数の中に処理用の関数を必ず呼び出されるようにtemplateを変更（比較的簡単そう）
- fastapi のinclude_louterの処理を修正して実行される関数を内部的に変更する  
include_routerの中でadd_api_routeを実行しており、その中のroute.endpointが実行する関数になっているっぽい

後者の対応方法で実装できた。

## 残課題
- DBと接続できるか(fastapiとsqlalchemyを組み合わせて使用することが多い)  
- AWS Lambdaで動くかの確認
    - Mangumみたいなやつ使いそう
    - moduleのpathが通るか
    - samで正常にビルドできるかどうか
    - APIの疎通が確認できるか
- 処理用のファイル作成は手動で行わなければならない
    - generateと同じ構成で生成することは可能だと思うが、新規で作成するファイルのみ生成するような仕組みにしなければならない
    - 別途必要なファイルは generator編集して作成できるようにする

- openapi-generatorの環境作成(javaが使える環境を前提にしている)
    - Dockerの使用？
    - 不要なログの消去
- openapi.yamlの編集方法(定義ファイルも分割出来るようにしたい)



## 参考
- <https://github.com/OpenAPITools/openapi-generator>
- <https://zenn.dev/ysk1to/books/248fad8cb34abe/viewer/845d1e>



## [7 - License](#table-of-contents)
-------

Copyright 2018 OpenAPI-Generator Contributors (https://openapi-generator.tech)
Copyright 2018 SmartBear Software

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at [apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---
