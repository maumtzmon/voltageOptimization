#!/bin/bash

setupIMG(){
    lta NROW 700
    lta NCOL 20
    lta NBINROW 1
    lta NBINCOL 1
    lta NSAMP 1
    lta EXPOSURE 0

    echo"image size, bin, NSAMP and exposure values done!"
}

doClean(){
    lta name $imgFOLDER/skp_mod9_wfr13_NSAMP1_NROW700_NCOL20_EXPOSURE_0_cleanimg_
    lta read
    echo "clean image done!"
}

### Main

source VOpt_init_LTA.sh

pathFiles="default/path"

if [ $# -eq 0 ]
then 
    pathFiles=$(pwd)/ #save the argument as /path/of/files
else
    pathFiles=$1 #save the argument as /path/of/files
fi

setupIMG()
doClean()
lta name $imgFOLDER/skp_mod9_wfr13_NSAMP1_NROW700_NCOL20_EXPOSURE_0_img_

for file in $pathFiles*
do
    source $file
    lta read
    echo "image done at :" $(date)

done




#for smp in `seq 20 20 2500`
#do
#	if [ ! -f "$lockfilename" ]; then break; fi
#	delay=$((smp+100))
#	lta set ssamp $smp
#	lta set psamp $smp
#	lta delay_Integ_ped $delay
#	lta delay_Integ_sig $delay
#	lta name $imgFOLDER/skp_${runname}_loopSSAMP_SSAMP${smp}_PSAMP${smp}_img
#	lta read
#done
