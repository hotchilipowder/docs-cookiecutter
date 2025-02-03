import os
import re

# 获取当前目录名称
current_folder = os.path.basename(os.getcwd())

# 如果需要对文件夹名做一些处理，比如将非字母数字字符替换掉
def slugify(value):
    value = value.lower().strip()
    value = re.sub(r'\s+', '-', value)            # 把空格替换为 -
    value = re.sub(r'[^\w\-]', '', value)          # 移除非字母数字和非连字符
    value = re.sub(r'[-]+', '-', value)            # 合并重复的-
    return value

# 如果用户在交互时输入了其他值，可以在这里根据需要选择是否覆盖
# 这里假设你希望总是以当前目录为准
project_name = slugify(current_folder)

# 打印调试信息（可选）
print(f"当前文件夹名称: {current_folder}")
print(f"生成的 project_name: {project_name}")

# 修改 cookiecutter 上下文
cookiecutter_context = globals().get('cookiecutter', {})
cookiecutter_context['project_name'] = project_name

