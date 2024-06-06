# PalServerDiscordBot
A bot that notifies you about PalServer's startup status and memory usage of the entire server.

PalServerの起動状況やサーバー全体のメモリ使用量を通知するボットです。

## 概要
PalServer.exeが起動したり落ちたりした際や、サーバー全体のメモリ使用量が80%を超えた際に通知を飛ばすBotです。
WindowsOSでサーバーを立てている人は使えます。Ubuntsuサーバー使っている人は、まあこのコードなんて簡単にUbuntsuサーバー用に書き換えができるでしょう。(Ubuntsuサーバーはあまり詳しくはないですが、大した書き換えはないと思います)

![](https://helkun.dev/image/works/PalServerDiscordBot.png)

## 使い方
1. あらかじめ[DiscordDeveloper](https://discord.com/developers/applications)でBotを作成し、動かしたいサーバーに入れておいてください。
2. Pythonをサーバーにインストールし、インストールが完了したらターミナル(PowerShell)で`pip install discord.py`と`pipi install psutil`を実行してください。
3. このリポジトリをクローンします
4. リポジトリをクローンしたら`.env`というファイルを作成して、`TOKEN`,`SERVER_PATH`(PalServer.exeがある絶対パス),`HONE_PATH`,`CHANNEL_ID`の環境変数の設定をします。
5. `python src/main.py`をターミナル上で実行！(そろそろ説明を書くのが面倒なのでくそ適当な説明になってます)

## 余談
windowsでサーバーを動かすのはくそです

## バク等があったら
Issueに追加しておいてください。
