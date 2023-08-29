import subprocess
import time


process = subprocess.Popen(["python3", "data/buffer.py"])
time.sleep(2)
process.terminate()
