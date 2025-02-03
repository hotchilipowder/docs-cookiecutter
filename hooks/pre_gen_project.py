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


