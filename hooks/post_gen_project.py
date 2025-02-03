# hooks/post_gen_project.py
import os
import shutil

# 获取用户在 cookiecutter.json 中填写的选项
include_github_actions = "{{ cookiecutter.include_github_actions }}".strip().lower()

if include_github_actions in ("yes", "y", "true", "1"):
    # 当前工作目录即为生成后的项目根目录
    project_dir = os.getcwd()
    github_action_dir = os.path.join(project_dir, "github_actions")
    project_dir = os.path.abspath(os.path.join(project_dir, ".."))

    for fname in os.listdir(github_action_dir):
        src_path = os.path.join(github_action_dir, fname)

        dest_dir = os.path.join(project_dir, ".github", "workflows")
        dest_path = os.path.join(dest_dir, fname)

        # 确保目标文件夹存在
        os.makedirs(dest_dir, exist_ok=True)

        try:
            shutil.copy(src_path, dest_path)
            print(f"[post_gen_project] GitHub Actions 文件已复制到: {dest_path}, 并且删除了github_actions")
        except FileNotFoundError:
            print(f"[post_gen_project] 未找到文件: {src_path}。请检查模板目录结构。")
    shutil.rmtree(github_action_dir)
else    :
    print("[post_gen_project] 用户选择不复制 GitHub Actions 文件。")

## 遍历当前文件。查找project_name_xxxxx, 然后替换为当前的目录名

def is_binary_file(file_path, blocksize=1024):
    """
    判断文件是否为二进制文件。
    通过读取文件的前 blocksize 字节，检查是否存在空字节（b'\0'）。
    """
    try:
        with open(file_path, 'rb') as file:
            chunk = file.read(blocksize)
            if b'\0' in chunk:
                return True
    except Exception as e:
        # 若读取文件出错，为安全起见返回 True
        return True
    return False

def replace_txt(txt_a, txt_b, path):
    if os.path.isdir(path):
        for sub_path in os.listdir(path):
            sub_path = os.path.join(path, sub_path)
            replace_txt(txt_a, txt_b, sub_path)
    else:
        if is_binary_file(path):
            return
        else:
            content = ''
            with open(path) as f:
                content = f.read()
            if content.find(txt_a) > -1:
                content = content.replace(txt_a, txt_b)
                print(f'replace {path} {txt_a} {txt_b}')
                with open(path, 'w') as f:
                    f.write(content)

default_project_name = "{{ cookiecutter.project_name }}"

if default_project_name == 'default_xxxx':
    project_name = os.path.basename(os.path.dirname(os.getcwd()))
    replace_txt('default_xxxx', project_name, os.getcwd())

