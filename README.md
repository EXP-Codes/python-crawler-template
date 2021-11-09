# python-crawler-template

> Python 爬虫开发模板

------

## 运行环境

![](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg) ![](https://img.shields.io/badge/Platform-Linux%20amd64-brightgreen.svg) ![](https://img.shields.io/badge/Platform-Windows%20x64-brightgreen.svg)


## 使用说明

1. 创建 Github Repository 时选择这个仓库做模板
2. 修改 [`script/crawler-create.sql`](./script/crawler-create.sql) 建库脚本
3. 运行 [`python gen_pdm.py`](./gen_pdm.py) 脚本生成数据库 pdm 代码
4. 修改 [`src`](./src) 下的爬虫代码，运行 [`python main.py`](./main.py) 启动爬虫
5. 修改 [`autorun.yml`](./.github/workflows/autorun.yml)，可通过 Github Actions 自动运行

