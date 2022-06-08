#Algorithm to create voltages combinations and test which one returns the lower stdev. 

import numpy as np
import pandas as pd

from ltaTools import setupVoltages, readoutVoltages

dic, dic_Bias= readoutVoltages("V123/voltage_skp_lta_v1_microchip.sh")

def Iteraciones(hh, hl, dh, dl): #This function dependes on the voltages given by h high, h low, d high and d low.
    
    step = 1
    
    sh = np.arange(0.0, 5.0, step)
    sl = np.arange(-10.0, 0.0, step)
        
    ol = np.arange(-7.5, -3.0, step)
    oh = np.arange(-3.0, 0.0, step)
    
    rh = np.arange(0.0, 7.5, step)
    rl = np.arange(-3.0, 0.0, step)
    
    for i1,i2 in zip(sh,sl):
        for j1,j2 in zip(oh,ol):
            if i2>j2:
                pass
            else:
                door1 = True
            if i2>hl:
                pass
            else:
                door2 = True
                
            if door1 and door2:
                
                for k1,k2 in zip(rh,rl):
                    if j1<k2:
                        door3 = False
                    else:
                        door3 = True
                    if j2>=k2:
                        door4 = False
                    else:
                        door4 = True
                    if door1 and door2 and door3 and door4:
                        dic_Voltages = {'h':[hh, hl], 's':[i2, i1], 'o':[j2, j1], 'r':[k2, k1], 'd':[dh, dl]}
                        combination = "h" + str(hh) + "_" +  str(hl) + "s" + str(i2) + "_" +  str(i1) + "o" + str(j2) + "_" +  str(j1) + "r" + str(k2) + "_" +  str(k1) + "d" + str(dh) + "_" +  str(dl)
                        combination_name = 'test_' + combination
                        setupVoltages(dic_Voltages, dic_Bias, combination_name)      
            else: 
                pass
            
Iteraciones(6.0,-5.0,10.0,-6.0)