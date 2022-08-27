#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Tolulope Abolade
# DATE CREATED:          20|08                        
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from specified folder
    in_files = listdir(image_dir)
    # Creates empty dictionary named results_dic
    results_dic = dict()
    
    for idx in range(0, len(in_files), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if in_files[idx][0] != ".":
            #Creating local variable to store the pet labels
            pet_labels = ""
            #format the pet labels so that they are in all lower case letters
            lower_pet_labels = in_files[idx].lower()
            #Format pet labels so it is seperated by the underscores.
            seperated_labels = lower_pet_labels.split("_")
            #Format so leading & trailing characters are removed.
            for label in seperated_labels:
                if label.isalpha():
                    pet_labels += label + " "
            #Format pet labels so leading and trailing whitespace characters are stripped from them.
            pet_labels = pet_labels.strip()
            # Adds new key-value pairs to dictionary ONLY when key doesn't already exist.
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_labels]
            else:
                print("** Warning: Key=", in_files[idx], "already exists in results_dic with value =", 
                      results_dic[in_files[idx]])
    
    return results_dic