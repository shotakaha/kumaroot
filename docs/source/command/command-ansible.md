# Ansibleしたい（`ansible` / `ansible-playbook`）

```console
$ ansible all -i inventory.ini -m ping
$ ansible web -i inventory.ini -m command -a "uptime"
```

Ansibleは「サーバー構成管理ツール」です。
SSH経由で複数のサーバーへの一括設定を自動化できます。
リモートサーバーの日々のヘルスチェックにも利用できます。

`ansible`コマンドは、単発のタスクをアドホックで実行するコマンド、
`ansible-playbook`は、複数のタスクを実行するコマンドです。

## インストールしたい

```console
$ brew install ansible

$ ansible --version
ansible [core 2.19.3]

$ ansible-playbook --version
ansible-playbook [core 2.19.3]
```

AnsibleはHomebrewでインストールできます。
`ansible`と`ansible-playbook`がインストールされます。

## インベントリしたい（`inventory.ini`）

```ini
# inventory.ini

[web]               # ← グループ名
192.168.1.10        # ← 管理対象ホスト（IPまたはホスト名）

# SSH設定を追加する例
[web:vars]
ansible_user=ec2-user      # SSHログインユーザー
ansible_ssh_private_key_file=~/.ssh/id_rsa  # SSH鍵のパス
ansible_python_interpreter=/usr/bin/python3  # Pythonのパス（RHEL8以降など）
```

`inventory.ini`は「どのサーバーを管理するか」を定義するファイルです。

## 接続確認したい（`-m ping`）

```console
$ ansible all -i inventory.ini -m ping
```

## 稼働時間したい

```console
$ ansible all -i inventory.ini -a "uptime"
```

## ディスク使用量したい

```console
$ ansible all -i inventory.ini -a "df -h"
```

## 統合ヘルスチェック

```console
$ ansible-playbook -i inventory.ini healthcheck.yml
```

```yaml
# healthcheck.yml
- hosts: all
  gather_facts: yes
  become: true

  tasks:
    - name: ✅ Ping check
      ansible.builtin.ping:

    - name: 🕰️ Check uptime
      ansible.builtin.command: uptime
      register: uptime_result
    - debug:
        var: uptime_result.stdout

    - name: 💾 Check disk usage
      ansible.builtin.command: df -h
      register: disk_result
    - debug:
        var: disk_result.stdout

    - name: 🧠 Check memory usage
      ansible.builtin.command: free -m
      register: mem_result
    - debug:
        var: mem_result.stdout

    - name: 🌐 Collect service facts
      ansible.builtin.service_facts:

    - name: 🔍 Check if httpd is running
      ansible.builtin.debug:
        msg: "✅ httpd is running"
      when: "'httpd' in ansible_facts.services and ansible_facts.services['httpd'].state == 'running'"

    - name: ⚠️ Warn if httpd is not running
      ansible.builtin.debug:
        msg: "❌ httpd is NOT running"
      when: "'httpd' not in ansible_facts.services or ansible_facts.services['httpd'].state != 'running'"
```
