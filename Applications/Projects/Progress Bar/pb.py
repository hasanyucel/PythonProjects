from tqdm import tqdm
import time

for i in tqdm(range(110),desc="Loading...",ascii=False,ncols=100):
    time.sleep(0.05)

print("Done!")