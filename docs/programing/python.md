# Python

## Anaconda

常用命令

```bash
# 创建环境:
conda create --name env_name python=3.11

#环境移植:
# 1.导出环境
conda env export -n env_name > enviroment.yaml
# 2.在目标电脑上使用导出的环境文件创建
conda env create -n env_name -f environment.yaml
```

## 打包

```bash

pyinstaller -i 图标 -F -w 文件

```
