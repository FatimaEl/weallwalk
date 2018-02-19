import os
import shutil
import time
import types 

#input path
fpath_input = "./ark+=b7291=d17p46_version_5/WeAllWalkToPublish8-20-17/SENSORDATA"
#ouput path
fpath_output = "./t2"

def copy_and_rename_sensor(fpath_input, fpath_output):
    folder_list = []
    for folder in os.listdir(fpath_input):
        folder_name = os.path.splitext(folder)[0]
        if(folder_name[0]=='P'):
            folder_list.append(fpath_input+'/'+folder_name+"/iPhone6-1L")
            folder_list.append(fpath_input+'/'+folder_name+"/iPhone6-2R")

    print(len(folder_list))

    for folder_path in folder_list:
        for folder in os.listdir(folder_path):
            if(folder[0]!='T'):
                continue
            # print(folder)
            for file in os.listdir(folder_path+'/'+folder):
                if(file=='iPhoneSensors.csv'):
                    # print('\t', file)
                    oldname = os.path.join(folder_path+'/'+folder, file)
                    newname = os.path.join(fpath_output, os.path.splitext(file)[0]+'_'+folder+".csv")
                    # print(oldname)
                    # print(newname)
                    shutil.copy(oldname, newname)
        # print('===========')

def copy_and_rename_xml(fpath_input, fpath_output):
    folder_list = []
    for folder in os.listdir(fpath_input):
        folder_name = os.path.splitext(folder)[0]
        if(folder_name[0]=='P'):
            folder_list.append(fpath_input+'/'+folder_name+"/XMLS")

    print(len(folder_list))

    for folder_path in folder_list:
        for file in os.listdir(folder_path):
            if(file[0]!='T'):
                continue
            # print(file)
            oldname = os.path.join(folder_path, file)
            newname = os.path.join(fpath_output, file)
            # print(oldname)
            # print(newname)
            shutil.copy(oldname, newname)

        # print('===========')


if __name__ == '__main__':
    fpath_csv = fpath_output+'/sensor'
    fpath_xml = fpath_output+'/xml'

    #create folder
    if not os.path.exists(fpath_output):
        os.makedirs(fpath_output)
        print fpath_output+' created'

    if not os.path.exists(fpath_csv):
        os.makedirs(fpath_csv)
        print fpath_csv+' created'

    if not os.path.exists(fpath_xml):
        os.makedirs(fpath_xml)
        print fpath_xml+' created'

    print('start ...')
    t1 = time.time() * 1000
    copy_and_rename_sensor(fpath_input, fpath_csv)
    copy_and_rename_xml(fpath_input, fpath_xml)
    t2 = time.time() * 1000
    print('take time:' + str(t2 - t1) + 'ms')
    print('end.')
