# -*- coding : UTF-8 -*-

# ライブラリのインポートと変数定義
import socket

# 中間サーバのIPとポート
target_ip = "127.0.0.2"
target_port = 8080
buffer_size = 4096

# ソケットオブジェクトの作成
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 中間サーバに接続
tcp_client.connect((target_ip,target_port))

# 中間サーバからのデータを受信
while True:
    data = tcp_client.recv(buffer_size)
    print("[*] Received a data : {}".format(data))
