import os
import re
from datetime import datetime

# 要搜索的目录：当前目录
target_dir = '.'

# 当天日期作为版本号
version = datetime.now().strftime('%Y%m%d')

# CSS 文件路径（根据实际情况修改）
css_file = 'asserts/style.css'

# 正则表达式：
# 匹配：assets/style.css 或 assets/style.css?v=xxx （v=后可以是任何东西）
pattern = re.compile(r'{}(\?v=[^"\']*)?'.format(re.escape(css_file)))

count = 0

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 替换为统一格式：assets/style.css?v=当天日期
            new_content, num = pattern.subn(f'{css_file}?v={version}', content)
            if num > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += num

print(f'✅ 共更新了 {count} 处 CSS 链接到版本号 {version}。')
