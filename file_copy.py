import json
import os
import shutil

json_data = json.load(open('data.json'))  # load json data

labels = []  # define empty list for labels in json

currentWorkingDir = os.getcwd()  # get current working directory

for item in json_data:
    fileName = item['file_name'] #assign variables for dict keys in json
    label = item['original_label']
    newPathToImg = item['new_path_to_img']

    if not label in labels:
        labels.append(label)
        thisLabelFolderpath = currentWorkingDir + '/' + label
        # create folder from label names in current working dir
        if not os.path.exists(thisLabelFolderpath):
            try:
                os.makedirs(thisLabelFolderpath)
            except OSError:
                if not os.path.isdir(thisLabelFolderpath):
                    raise

    source = newPathToImg
    target = thisLabelFolderpath + '/' + fileName   
    try:
        shutil.copy(source, target)
        print("Successfully copied file : %s" % source)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())




    
