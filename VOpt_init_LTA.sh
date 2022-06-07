#!/bin/bash

Vvsub = 70
channel=3

imgFOLDER=`dirname $BASH_SOURCE`/images/microchip/07APR2022
runname=mod9_wfr13
lockfilename=lockfile

setupLTA(){
        source setup_lta.sh
        source voltage_skp_lta_v1_microchip.sh #initial Voltage configuration
        lta sseq sequencers/microchip/sequencer_microchip_binned_brenda.xml

        lta set sinit 30
        lta set pinit 0
        lta set ssamp 200
        lta set psamp 200
        lta set packSource 9
        lta set cdsout 2

        lta set vsub $Vvsub
        }

doClean(){
        if [ ! -f "$lockfilename" ]; then break; fi
        lta NROW 650
        lta NCOL 600
        lta NBINROW 1
        lta NBINCOL 1
        lta NSAMP 1
        lta EXPOSURE 0
        lta name $imgFOLDER/skp_${runname}_NSAMP1_NROW650_NCOL600_EXPOSURE0_cleanimg
        lta read
        }

touch $lockfilename
mkdir -p $imgFOLDER

setupLTA
doClean
