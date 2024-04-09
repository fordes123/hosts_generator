# Hosts Generator
![Python Version](https://img.shields.io/badge/Python-3%2B-blue?)
![Build Status](https://img.shields.io/github/actions/workflow/status/fordes123/hosts_generator/dns_resolve.yml?branch=main) 

一个简单的 Python 脚本，通过向指定的 DoH 服务器发起 ECS DNS 解析请求，构建适合不同区域的 Hosts 文件。
通过 Github Action 托管，可简单解决部分地区对特定网站的 DNS 污染以实现直连。

## 如何使用

将生成的 hosts 文件加入系统的 hosts 中，或者将文件链接 加入 AdGuard Home DNS 黑名单中
(另需在`DNS 服务配置` > `拦截模式` 中选择 `默认`)  

> ⚠️ 请勿使用本仓库内的 hosts 文件，它是用于测试且过时的，如有需要请参考下方说明自行构建  

## 快速开始

1. 克隆仓库
```bash
git clone https://github.com/fordes123/hosts_generator.git
```

2. 安装依赖项
```bash
cd hosts_generator
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

