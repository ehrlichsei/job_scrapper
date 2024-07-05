import json
from pathlib import Path

EXTRACT_KEY = 'webVideoUrl'
INPUT_PATH = 'data/tiktok_videos.json'
OUTPUT_PATH = 'output/tiktok_webVideoUrl.txt'

# 定义输入和输出文件路径
input_file_path = Path(INPUT_PATH)
output_file_path = Path(OUTPUT_PATH)

# 读取JSON文件内容
with input_file_path.open('r', encoding='utf-8') as input_file:
    data = json.load(input_file)

# 提取所有webVideoUrl的值
web_video_urls = [item[EXTRACT_KEY] for item in data if EXTRACT_KEY in item]

# 将提取的webVideoUrl值写入文本文件
with output_file_path.open('w', encoding='utf-8') as output_file:
    for url in web_video_urls:
        output_file.write(url + '\n')

print(f'已将所有webVideoUrl值写入 {output_file_path}')