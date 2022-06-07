import os
import sys
from datetime import datetime
from pathlib import PurePath as PurePath

def setupIMG():
    os.system('lta NROW 700')
    os.system('lta NCOL 20')
    os.system('lta NBINROW 1')
    os.system('lta NBINCOL 1')
    os.system('lta NSAMP 1')
    os.system('lta EXPOSURE 0')
    
    return print('image size, bin, NSAMP and exposure values done!')

def doClean():
    os.system('lta name $imgFOLDER/skp_mod9_wfr13_NSAMP1_NROW700_NCOL20_EXPOSURE_0_cleanimg')
    os.system('lta read')
    return print('clean image done!')



#setting up the image size, bin, NSAMP and exposure values
def main(argv):
    os.system('source VOpt_init_LTA.sh')
    if len(argv)>1:
        pathName=argv[1]
    else:
        pathName=str(PurePath(argv[0]).parents[0])
        
    #setupIMG()


    with os.scandir(pathName) as Directory:
        for file in Directory:
            if not file.name.startswith('.') and file.is_file():
                os.system('source '+file.name) #load the Voltage file
                doClean()   #take clean image
                os.system('lta name $imgFOLDER/skp_mod9_wfr13_NSAMP1_NROW700_NCOL20_EXPOSURE_0_img') #change the name
                os.system('lta read') #read
                now= datetime.now()
                current_time = now.strftime("%H:%M:%S")

                print('image done at: '+current_time)
    
    return print('All done! at: '+current_time)


if __name__ == "__main__":
    argv = sys.argv
    exitcode = main(argv)
    exit(code=exitcode)