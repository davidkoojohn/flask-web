## pyenv & pyenv-virtualenv

```
$ pyenv install --list
$ pyenv install 3.6.7
$ pyenv versions
$ pyenv global 3.6.7
$ pyenv uninstall x.x.x
```

* 使用 `pyenv-virtualenv` 创建虚拟环境：

```
# 查询可用
$ pyenv versions

# 创建
$ pyenv virtualenv [version] <venv-name>
$ pyenv virtualenv 2.7.11 venv-2.7.11
```

* 命令手动激活和退出虚拟环境：

```
# 激活
$ pyenv activate <venv-name>
$ pyenv activate venv-2.7.11

# 退出
$ pyenv deactivate

# 删除
$ pyenv uninstall venv-2.7.11
```

## `requirements.txt`

```
# 产生 requirements.txt 文件
$ pip freeze > requirements.txt

# 安装包
$ pip install -r requirements.txt
```

