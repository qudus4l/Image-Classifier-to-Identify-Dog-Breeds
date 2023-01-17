#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
# PROGRAMMER: Qudus .A
# DATE CREATED:   15|01|23
# REVISED DATE: 15|01|23
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the program using the classifier's model
#          architecture to classify the images. This function will use the
#          results in the results dictionary to calculate these statistics.
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best'
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the
#          how to calculate the counts and percentages for this function.
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results' statistics
#          (either a percentage or a count) where the key is the statistic's
#           name (starting with 'pct' for percentage or 'n' for count) and value
#          is the statistic's value.  This dictionary should contain the
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches'
#            pct_correct_dogs - percentage of correctly classified dogs'
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results' statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    """
    # Creates empty dictionary for results_stats_dic
    results_stats_dic = {'n_dogs_img': 0, 'n_match': 0, 'n_correct_dogs': 0, 'n_correct_notdogs': 0,
                         'n_correct_breed': 0}

    # Sets all counters to initial values of zero so that they can
    # be incremented while processing through the images in results_dic

    # process through the results dictionary
    for key in results_dic:

        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Pet Image Label is a Dog AND Labels match-counts Correct Breed
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1

        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

            # Classifier classifies image as Dog (& pet image is a dog)
            # counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        # Pet Image Label is NOT a Dog
        else:
            # Classifier classifies image as NOT a Dog(& pet image isn't a dog)
            # counts number of correct NOT dog classifications.
            results_stats_dic['n_correct_notdogs'] += 1

    # Calculates run statistics (counts & percentages) below that are calculated
    # using the counters from above.

    # calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)

    # calculates number of not-a-dog images using - images & dog images counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] -
                                          results_stats_dic['n_dogs_img'])

    # Calculates % correct for matches
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] /
                                      results_stats_dic['n_images']) * 100

    # Calculates % correct dogs
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] /
                                             results_stats_dic['n_dogs_img']) * 100

    # Calculates % correct breed of dog
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] /
                                              results_stats_dic['n_dogs_img']) * 100
    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                    results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic
