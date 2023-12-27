# Steam Hosts
![Python Version](https://img.shields.io/badge/Python-3%2B-blue?)
![Build Status](https://img.shields.io/github/actions/workflow/status/fordes123/steam_hosts/auto_update.yml?branch=main)

利用 Github Action 通过 ECS DNS 解析，自动更新适合不同区域的 Steam Hosts 文件

## 如何使用

将生成的 Hosts 文件加入系统的 Hosts 中，或者将 [🔗文件链接](https://raw.githubusercontent.com/fordes123/steam_hosts/main/hosts) 加入 AdGuard Home DNS 黑名单中
(⚠️ 另需在 AdGuard Home `DNS 服务配置` > `拦截模式` 中选择 `默认`)  

> PS: 如果你使用本仓库提供的 Hosts 文件，需要注意以下为本仓库的默认配置，它可能不适用于你的网络环境:  
> ECS CIDR: `127.0.0.0/8`  
> DNS 服务器: `https://dns.google/dns-query` (Google Public DNS over HTTPS)

## 快速开始

1. 克隆仓库
```bash
git clone https://github.com/fordes123/steam_hosts.git
```

2. 安装依赖项
```bash
cd steam_hosts
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. 运行
```bash
python dns_resolve.py [-h] [-c CIDR] [-s SERVER] [-o OUTPUT] [-d DOMAINS]
```

命令行参数说明：
```text
options:
  -h, --help            show this help message and exit
  -c CIDR, --cidr CIDR  CIDR for the target area
  -s SERVER, --server SERVER
                        DoH Server (Must support ECS)
  -o OUTPUT, --output OUTPUT
                        output file
  -d DOMAINS, --domains DOMAINS
                        domain list file
```

---

## Github Action

1. Fork 本仓库
2. 编辑 `domains.txt` 文件, 修改需要解析的域名
3. 在仓库的 Actions 中启用 Github Action, 选中 `DNS_RESOLVE`，并立即运行一次
4. Enjoy it!

