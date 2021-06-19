# -*- coding : UTF-8 -*-

# ライブラリのインポートと変数定義
import time
import socket

# 上流側サーバ（strsvr）のIPとポート
up_server_ip = "127.0.0.1"
up_server_port = 52001
buffer_size = 4096

# 下流側サーバIPとポート
down_server_ip = "127.0.0.2"
down_server_port = 8080
listen_num = 5
#buffer_size_s = 1024

# ソケットオブジェクトの作成（上流側）
up_tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ソケットオブジェクトの作成（下流側）
down_tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 上流側サーバに接続
up_tcp_client.connect((up_server_ip,up_server_port))
print("[U] Connected to strsvr")

# 作成した下流側ソケットオブジェクトにIPアドレスとポートを紐づける
down_tcp_server.bind((down_server_ip, down_server_port))
# 作成した下流側ソケットオブジェクトを待ち受け状態にする
down_tcp_server.listen(listen_num)
print("[D] Listen start")
# 下流側クライアントからの接続を許可
down_client, down_address = down_tcp_server.accept()
print("[D] Connected from down [ Source : {}]".format(down_address))

time.sleep(3)

# ループして接続を待ち続ける
while True:

    print("waiting upstream...")

    # データを上流側から受信する
    data = up_tcp_client.recv(buffer_size)
    #data = client.recv(buffer_size_c)
    print("[U] Received Data : {}".format(data))

    # 下流側クライアントへデータを流す
    # down_client.send(b"Recieved data  ")
    down_client.send(data)

    time.sleep(3)

    # 接続を終了させる
    #client.close()
