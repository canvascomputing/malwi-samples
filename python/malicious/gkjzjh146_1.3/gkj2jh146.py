import os

def malicious_function():
    os.system('echo "恶意代码执行成功"')
    # 这里可以添加你的其他恶意行为

if __name__ == '__main__':
    malicious_function()
