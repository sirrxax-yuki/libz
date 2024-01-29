# 開発者向け手順書


## クラウド環境構築

1. Dockerfile を使用して、以下の環境変数を与えつつコンテナをビルドする
    - RSI_CLIENT_ID
    - RSI_AUTH_REDIRECT_URL
      - ex.) $ docker build -t xxx/xxx:xxx --build-arg RSI_CLIENT_ID=xxx --build-arg RSI_AUTH_REDIRECT_URL=xxx .
2. port80を開放して、以下の環境変数を与えつつコンテナを起動する
    - DATABASE_HOST
    - DATABASE_PORT
    - DATABASE_USER
    - DATABASE_PASSWORD
    - DATABASE_NAME
      - ex.) $ docker run --name xxx -p 80:80 -e DATABASE_HOST=xxx -e DATABASE_PORT=xxx .... -d xxx/xxx:xxx
4. docker exec [コンテナ名] python tools/initialize_database.py を実行してDBを初期化する
5. [サーバホスト]:80 にアクセスする


### AWS環境構築

  - 以下の順でCloudFormationテンプレートを実行
    - libz-Keypair
    - libz-VPC
    - libz-IAM
    - libz-DB
    - libz-EC2
  - EC2サーバに docker をインストール


### 補足

  - docker-compose.yml は使用しない (念のため用意しているだけ)
  - dockerイメージは .github/workflows/deploy.yml を使用して GitHub Actions で作成することを推奨



## ローカル環境構築 (本番動作確認用)

1. docker-compose.local.yml を使用して、以下の環境変数を与えつつコンテナをビルドする
    - RSI_CLIENT_ID
    - RSI_AUTH_REDIRECT_URL
      - ex.) $ docker-compose -f docker-compose.local.yml --build-arg RSI_CLIENT_ID=xxx --build-arg RSI_AUTH_REDIRECT_URL=xxx
2. docker-compose.local.yml を使用してコンテナを起動する
3. tools/initialize_database.local.sh を実行してDBを初期化する
4. http://localhost:8000 にアクセスする



## ローカル環境構築 (開発用)

1. docker-compose.local.yml を使用して、以下の環境変数を与えつつコンテナをビルドする
    - RSI_CLIENT_ID
    - RSI_AUTH_REDIRECT_URL
      - ex.) $ docker-compose -f docker-compose.local.yml --build-arg RSI_CLIENT_ID=xxx --build-arg RSI_AUTH_REDIRECT_URL=xxx
2. docker-compose.local.yml を編集して backend に以下の環境変数を定義する
    - DEBUG_MODE: 'yes'
3. docker-compose.local.yml を使用してコンテナを起動する
4. tools/initialize_database.local.sh を実行してDBを初期化する
5. 以下の手順を実行してデバッグサーバを起動
    - $ docker exec -it libz-frontend bash
      - $ npm run dev
6. http://localhost:3000 にアクセスする


### 補足

  - 手順1は面倒なので docker-compose.local.yml の args の値を直接編集することを推奨
  - または frontend 直下に .env.development.local を作ってそちらに記載
    - frontend を単体で起動して確認したい場合にも上記が使える



## ユニットテスト

1. backend ディレクトリに移動
2. unittest.sh と apitest.sh を必要に応じて実行する (後者はbackend全体の結合テスト)



## backendAPI仕様書

1. [サービスURL]/api/openapi.json にGETリクエストを投げてjsonデータを取得
2. 適切なOpenAPIビューアで開く

### 補足

  - 開発者向けの自動生成ドキュメント

