import os

# 获取 GITHUB_TOKEN 环境变量
github_token = os.getenv('OPENAI_KEY')

if github_token:
    print(f"OPENAI key: {github_token}")
else:
    print("OPENAI jkey is not available.")
