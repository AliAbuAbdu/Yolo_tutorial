import os
HOME = os.getcwd()
print(HOME)

# Fix requirements.txt using Python (Windows-compatible, no sed needed)
with open('C:\\Users\\mrgum\\Desktop\\Yolo_tutorial\\ByteTrack\\requirements.txt', 'r') as f:
    content = f.read()
content = content.replace('onnx==1.8.1', 'onnx==1.9.0')
with open('C:\\Users\\mrgum\\Desktop\\Yolo_tutorial\\ByteTrack\\requirements.txt', 'w') as f:
    f.write(content)
print("Updated requirements.txt")
# Install dependencies using conda
os.system('conda install -y -c conda-forge --file requirements.txt')
os.system('python setup.py -q develop')
