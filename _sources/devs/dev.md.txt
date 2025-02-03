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

如果确实需要，需要在调用时传入，太麻烦了... (这个没有办法，因为调用pre_prompt 或者 pre_gen都是在临时目录中）

唯一的办法可能只有在完成渲染后。


完成了一个渲染后的，只要你用默认的 `default_xxxx`, 就进行查找替换...

