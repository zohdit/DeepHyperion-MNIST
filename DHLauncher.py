import os

for i in range(1, 2):
    os.environ['RUN_ID'] = str(i)
    os.system("python mapelites_mnist.py")