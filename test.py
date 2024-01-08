# this will show the how templet.py will execute 

import os 

path = "notebook/research.ipynb"
dir,file = os.path.split(path)
os.makedirs(dir,exist_ok=True) #exits will not thorugh error if dir already exists 

with open(path,"w") as f:
    pass