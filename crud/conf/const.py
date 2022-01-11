import os

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')  # database名
DB_HOST = os.environ.get('DB_HOST')  # コンテナ名 or RDSのエンドポイント
DB_PORT = os.environ.get('DB_PORT')  # ポート番号
