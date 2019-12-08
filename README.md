# 機械学習アプリの構築

## Docker について
- ### 事前準備
    - 今回、dockerを 利用しての 環境構築についてここに書いておく。
    - https://qiita.com/n-yamanaka/items/ddb18943f5e43ca5ac2e を参照にして
      事前に環境を構築してほしい
    - 今回、API 側 での環境構築を行っているが、のちにフロントエンドが必要と判断すれば、あとで構築する
- ### 環境構築方法
    - はじめに、環境を構築するには、次のコマンドを実行する

      ```sh 
      docker-compose build
      ```
    
    >新たに必要と考えたライブラリが必要と考えたら、`requirement.txt` に必要なライブラリ名とそのバージョンを記入して、もう一度上のコマンドを打つ必要がある

- ### docker を起動させる
    - 環境構築後、docker を立ち上げる際には、次のコマンドを実行する

    ```bash 
    docker-compose up 
    ```

    - 一度 立ち上げた　docker を停止するには、`CTRL+C` か、　別のターミナルで、
    
    ```bash
    docker-compose stop
    ```

    と入力する。
