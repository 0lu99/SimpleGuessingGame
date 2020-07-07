import os

' List the files in the current working directory'
files = os.listdir(os.getcwd())

'''
by default, it will print from smallest to largest, so order has been reversed
'''
files.sort(key=lambda f: os.stat(f).st_size, reverse=True)
print(files)