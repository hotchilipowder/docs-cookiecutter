# 2025-02-03


## Done

- [x] conf.py with extension `myst_parser` and `myst_enable_extensions`
- [x] conf.py with extension `bibtex_bibfiles`
- [x] add github actions for build docs
- [x] Just read the repo_name and inject into options for cookiecutter


## TODO
- [ ] Bug for project name



### Findings

https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html

hooks中, `pre_prompt` 
使用

```
current_folder = os.path.basename(os.getcwd())

```
得到的是模板仓库的目录名，而不是你启动 cookiecutter 时所在的目录名或者最终生成项目的文件夹名。

如果确实需要，需要在调用时传入，太麻烦了...
想办法

修改为默认是default, 如果default那么就会修改为项目名，如果想要改，那么就改.
