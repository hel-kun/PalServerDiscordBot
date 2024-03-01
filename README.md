# PalServerDiscordBot
A bot that notifies you about PalServer's startup status and memory usage of the entire server.

PalServerの起動状況やサーバー全体のメモリ使用量を通知するボットです。

## 概要
PalServer.exeが起動したり落ちたるした際や、サーバー全体のメモリ使用量が80%を超えた際に通知を飛ばすBotです。
WindowsOSでサーバーを立てている人は使えます。Ubuntsuサーバー使っている人は、まあこのコードなんて簡単にUbuntsuサーバー用に書き換えができるでしょう。(Ubuntsuサーバーはあまり詳しくはないですが、大した書き換えはないと思います)

## 使い方
1. あらかじめ[DiscordDeveloper](https://discord.com/developers/applications)でBotを作成し、動かしたいサーバーに入れておいてください。
2. Pythonをサーバーにインストールし、インストールが完了したらターミナル(PowerShell)で`pip install discord.py`と`pipi install psutil`を実行してください。
3. DiscordBot.pyというファイルをサーバー内のどこかに作ってこのリポジトリに入っているPythonファイルのコードをペーストします。
4. `TOKEN = 'Add DiscordBot TOKEN'`の`Add DiscordBot TOKEN`の部分にBotのTOKENを入れます。
5. `CHANNEL_ID = 0123456789`の欄にBotの通知を飛ばしたいチャンネルのIDを入れます。
6. DiscordBot.pyがあるディレクトリ上で`python DiscordBot.py`とターミナル(PowerShell)で打つとBotが動きます。

## バク等があったら
Issueに追加しておいてください。
