import os
all_dir = os.listdir("/allure_result/PyTest/Lab_test001.py")

os.environ['MY_VAR'] = 'arpit'
print(os.getenv("MY_VAR"))