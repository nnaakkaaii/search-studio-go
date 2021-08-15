# search-studio-go
studioを検索するのに必要なバックエンドコードの管理

## プロジェクト構成

### python_server

* DRFによるサーバー
* openapiの簡易的な実装を行う
* データベースはMySQL

## セットアップ

### 仮想環境の作成

このREADME.mdと同じディレクトリで次を実行

```bash
$ python3 -m venv .venv
```

さらに、次で有効化

```bash
$ source .venv/bin/activate
```

### データベース作成

python_server/内で次を実行

```bash
$ python3 manage.py migrate
```

### 管理者作成

python_server/内で次を実行

```bash
$ python manage.py createsuperuser
```

(ex : username : dev, password : dev-xxx)

## コマンド

### 起動

python_server/内で次を実行することで起動が可能

```bash
$ python3 manage.py runserver
```

### apiのルートディレクトリ

/api/v1/search/にアクセス

### 管理者画面

/adminにアクセス
