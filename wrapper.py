import os
import math
import shutil
names  = os.listdir('testfolder')
batch_size = 1

for k in range(len(names)):
    if k%batch_size ==0 :
        os.system('python demo.py --indir temp --outdir examples/res_attention --save_img')
        os.rename('examples/res_attention/alphapose-results.json', 'examples/res_attention/'+names[k][0:-4]+'json')
        print("OIWJEFOJWEOJFOWEOFJOWEJFJOEFWOJOFJWFOJFEOJWE")
        shutil.rmtree('temp', ignore_errors=True)
        os.mkdir('temp')
    shutil.copy('testfolder\\'+names[k], "temp")
    
    
