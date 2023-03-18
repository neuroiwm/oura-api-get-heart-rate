# A test code to use oura api

## 連絡先

Seitaro Iwama (Junichi-Ushiba Laboratory)

iwama,at,keio.jp

## 実行環境
Python 3.10

## 使い方
1. Authorization keyの取得

    https://cloud.ouraring.com/personal-access-tokens
    
    上記URLにログインし、トークンを発行

    参考: https://note.com/mxiskw/n/naca60e24e0d1

2. Python実行環境の整備
    
    `oura.py`に1.で発行したアクセストークンを貼り付け
    ```
    self.headers = { 
            'Authorization': 'INSERT TOKEN HERE' }
    ```

    Pythonで仮想環境を作成し、必要なライブラリをインストールして実行
    ```
    python -m venv .venv
    source ./.venv/bin/activate

    pip install -r requirements.txt

    python test_HR_realtime.py
    ```
3. (Option) 取得する時間幅の設定
    
    `test_HR_realtime.py`内の`params`変数の日時を書き換えることでモニタリングする日の範囲を変更可能