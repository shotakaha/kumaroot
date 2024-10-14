FROM ubuntu:24.10

# パッケージ情報の更新
# 1. SSHサーバーをインストール
# 2. Rsyncサーバーをインストール
RUN apt-get update && apt-get install -y \
    openssh-server \
    rsync \
    sudo \
    vim \
    && apt-get clean

# SSHサーバーの設定
RUN mkdir /var/run/sshd

# パスワード認証を有効にする
# /etc/ssh/sshd_config を修正

# rootユーザーのパスワードを設定
RUN echo 'root:root_pass' | chpasswd

# SSHポートを解放
EXPOSE 22

# SSHサーバーを起動
CMD ["/usr/sbin/sshd", "-D"]
