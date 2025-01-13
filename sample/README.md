# Djangoによるスプレッドシードの値を取得するサンプルプログラム
## 環境構築
### pythonのインストール
https://www.python.org/downloads/

上記URLからインストーラーをダウンロード
### Djangoのインストール
ターミナル（コマンドプロンプトでも可）で以下コマンドを実行
~~~
python -m pip install Django
~~~

### ディレクトリ構成
sample: サンプルのメイン

polls: プロジェクト名（チュートリアル準拠）

service: MVCモデルとは別に機能を提供(基本的に調査したサンプルはこちらに作成します)

### チートシート
サーバーの起動
~~~
python manage.py runserver
~~~
カレントディレクトリをsampleにしてサーバーを起動

localhost/polls/1/

にアクセスすると確認できます。