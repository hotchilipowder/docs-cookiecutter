# hooks/post_gen_project.py
import os
import shutil

# 获取用户在 cookiecutter.json 中填写的选项
include_github_actions = "{{ cookiecutter.include_github_actions }}".strip().lower()

if include_github_actions in ("yes", "y", "true", "1"):
    # 当前工作目录即为生成后的项目根目录
    project_dir = os.getcwd()
    project_dir = os.path.abspath(os.path.join(project_dir, ".."))

    github_action_dir = os.path.join(project_dir, "github_actions")
    for fname in os.listdir(github_action_dir):
        src_path = os.path.join(github_action_dir, fname)

        dest_dir = os.path.join(project_dir, ".github", "workflows")
        dest_path = os.path.join(dest_dir, fname)

        # 确保目标文件夹存在
        os.makedirs(dest_dir, exist_ok=True)

        try:
            shutil.copy(src_path, dest_path)
            print(f"[post_gen_project] GitHub Actions 文件已复制到: {dest_path}")
        except FileNotFoundError:
            print(f"[post_gen_project] 未找到文件: {src_path}。请检查模板目录结构。")
else    :
    print("[post_gen_project] 用户选择不复制 GitHub Actions 文件。")

