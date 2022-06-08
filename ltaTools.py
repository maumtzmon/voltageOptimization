###
# Tools to analysis and operations for skipper-CCD and LTA v2
#
# Mauricio Martinez Montero
###

#Acquisition of Voltages values from configuration files of LTA 
def readoutVoltages(archivoVoltajes): 
    dic_Voltages={}
    dic_Bias={}
    with open(archivoVoltajes,'r') as File_voltages:
        varList=[]
        for linea in File_voltages:
            if '=' in linea:
                #print(linea, end='\r')
                #       vh = 9
                varList.append(float(linea.split('=')[1]))
                if len(varList)==2:
                    dic_Voltages[linea.split('=')[0][0]]=varList
                    varList=[]

            elif 'vdrain ' in linea or 'vdd ' in linea or 'vr ' in linea or 'vsub ' in linea:
                dic_Bias[linea.split(' ')[2]]=float(linea.split(' ')[3].split('#')[0])

    return dic_Voltages, dic_Bias

#Generates a file from template with new values
def setupVoltages(dic_Voltages, dic_Bias, newName='test_V.sh'):  #Needs 2 dictionaries with voltages values
    with open('voltageFiles/voltage_ICN_test_.sh','r') as template,\
         open('voltageFiles/'+newName,'w') as newFile:              
        for linea in template:
            if '=' in linea:
                if linea.split('=')[0][0] in dic_Voltages:
                    if linea.split('=')[0][1]=='h':
                        newFile.write(linea.split('\n')[0]+str(dic_Voltages[linea.split('=')[0][0]][0])+'\n')
                    elif linea.split('=')[0][1]=='l':
                        newFile.write(linea.split('\n')[0]+str(dic_Voltages[linea.split('=')[0][0]][1])+'\n')

            elif 'vdrain ' in linea or 'vdd ' in linea or 'vr ' in linea or 'vsub ' in linea:
                newFile.write(linea.split('#')[0].split('\t'or '\n')[0] + str(dic_Bias[linea.split('#')[0].split('\t'or'\n')[0].split(' ')[-2]])+'\n')
            else:
                newFile.write(linea)
        newFile.close()
        template.close()
    return print('\n\nThe file "'+'voltageFiles/'+newName+'" is ready\n\n')



#"new values for"
#Generates Dictionaries with new values of setup variables
#uses a file for a reference, change the value of a setup variable in a specific range and
#return two dictionaries and a code name for reference.
#Needs a file, variable to be edited

def newVals(template='file.sh', var4change='empty', limit_h=[1,-1],limit_l=[0,-2], steps=.1):
    #template: file as reference, e.g. file that works good and we want to improve
    #var4change: variable to generate new combinations
    #limits: values interval, max and min of h and l values of the var
    #steps: increments of the values
    listDicts=[] #lista que contendra los diccionarios necesarios para generar los nuevos archivos
    #E.g. of a ListDicts=[dict_1={'dic_Voltages':{}, 'dic_Bias':{}, newName='test_V.sh'},dict_2, dict_3]
    #From template takes a reference of the values we will change
    #takes all the variables and copy them to the dict, only replace the var4change
    dicTemplate=readoutVoltages(template)
    #from dicTemplate, 
    #   loop to make a copy and replace the values of the var4change in the dict
    #       append the dictionary in the list,  listDicts.append(dict_1:{'dic_Voltages':{}, 'dic_Bias':{}, 'name':'of the NewFile'})

    for newDict in listDicts: #with the list full of new dicts, create the files to change the configuration to the LTA
        setupVoltages(newDict['dict_1'][dic_Voltages], newDict['dict_1'][dic_Bias], newDict['dict_1'][newName])
    return print('All Done!')




dic_Voltages, dic_Bias=readoutVoltages('voltageFiles/voltage_skp_lta_v1_microchip.sh')

setupVoltages(dic_Voltages, dic_Bias, newName='voltage_ICN_test_01.sh')