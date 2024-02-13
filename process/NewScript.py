
import os
import requests

def download_file(url, paths):
    response = requests.get(url)
    with open(paths, 'wb') as file:
        file.write(response.content)

urls_and_path = [
    ('https://github.com/LeslieZhoa/HeSer.Pytorch/releases/download/v0.0/parsing.pth', '../pretrained_models/parsing.pth'),
    ('https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/sr_cf.onnx', '../pretrained_models/sr_cf.onnx'),
    ('https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/Blender-401-00012900.pth', '../pretrained_models/Blender-401-00012900.pth')
]

os.makedirs('../pretrained_models', exist_ok=True)

for url, paths in urls_and_path:
    download_file(url, paths)
