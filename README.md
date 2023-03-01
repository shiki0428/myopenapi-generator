
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
今回は　generate の引数に　fastapi-custom-serverを指定することで独自のgeneratorが呼び出される


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
