import os
import cv2
from PIL import Image
import json
import shutil

# path where the dataset is downloaded
inputPath = r"/home/ivanna/data/headsegmentation/samples/"
labelsPath = r"/home/ivanna/data/headsegmentation/labels/"

# new folder where the cleanedup and organized dataset is placed
outputPath = r"/home/ivanna/data/headsegmentation/training_arranged/"

# Step 1: Look at folder arrangement
labelsDist = sorted(os.listdir(labelsPath))

# Returns list of folders
# ['female03', 'female10', 'female23', 'femalealison1', 'femalealison2', 'femalebarbera', 'femalebarbera2', 'femalecarla', 'femalecarla2', 'femalefelice', 'femalejoyce', 'femalejoyce2', 'femalelaura', 'femalelaura2', 'femaleroberta', 'male01', 'male06_1', 'male06_2', 'male09', 'male23', 'maleandrew', 'maleandrew2', 'malebruce', 'malebruce2', 'malecarlos', 'malecarlos2', 'malecorry', 'malecorry2', 'maleelias', 'maleelias2', 'malegaberial', 'malegaberial2', 'malekumar', 'maleshawn', 'multiperson', 'real']

# Creating folders in output directory
for folder in labelsDist:
    os.mkdir(os.path.join(outputPath, folder))

# Step 2: Dataset can be grouped into 4 categories as below
folderTypes = {"female": [], "male": [], "multiperson": [], "real": []}

for folder in os.listdir(inputPath):
    if folder.startswith("female"):
        folderTypes["female"].append(folder.split("_")[0])
        if os.path.isdir(os.path.join(outputPath, folderTypes["female"][-1])):
            for file in os.listdir(os.path.join(inputPath, folder)):
                shutil.copy(os.path.join(inputPath, folder, file), os.path.join(outputPath, folderTypes["female"][-1], file))
    
    elif folder.startswith("multiperson"):
        folderTypes["multiperson"].append(folder.split("_")[0])
        if os.path.isdir(os.path.join(outputPath, folderTypes["multiperson"][-1])):
            for file in os.listdir(os.path.join(inputPath, folder)):
                shutil.copy(os.path.join(inputPath, folder, file), os.path.join(outputPath, folderTypes["multiperson"][-1], file))
    
    elif folder.startswith("male"):
        
        folderTypes["male"].append(folder.split("_")[0])
        if folder.startswith("male06") and "nolight" in folder:
            outFolder = "male06_2"
        
        elif folder.startswith("male06"):
            outFolder = "male06_1"
        
        else:
            outFolder = folderTypes["male"][-1]
        if os.path.isdir(os.path.join(outputPath, outFolder)):
            for file in os.listdir(os.path.join(inputPath, folder)):
                shutil.copy(os.path.join(inputPath, folder, file), os.path.join(outputPath, outFolder, file))

    else:
        if folder.startswith("real") and os.path.isdir(os.path.join(outputPath, "real")):
            for file in os.listdir(os.path.join(inputPath, folder)):
                shutil.copy(os.path.join(inputPath, folder, file), os.path.join(outputPath, "real", file))
        
# Step 3: Look at the distribution of images in each folder
# Note: Some images even contain multiple head/face segmentation depending on if the second or third face takes up enough screen real estate space. 
for folder in labelsDist:
    if len(os.listdir(os.path.join(labelsPath, folder))) != len(os.listdir(os.path.join(outputPath, folder))):
        print(folder, len(os.listdir(os.path.join(labelsPath, folder))), len(os.listdir(os.path.join(outputPath, folder))))

# Step 4: Move Dataset to a single folder
finalPath = r"/home/ivanna/data/headsegmentation_rearranged/"

for row, sample in dataSamples.iterrows():
    imagePath = os.path.join(outputPath, sample["folder"], sample["Filename"])
    maskPath = os.path.join(labelsPath, sample["folder"], sample["Filename"])
    
    shutil.copy(imagePath, os.path.join(finalPath, "images", sample["folder"] + "_" + sample["Filename"]))
    shutil.copy(maskPath, os.path.join(finalPath, "masks", sample["folder"] + "_" + sample["Filename"]))