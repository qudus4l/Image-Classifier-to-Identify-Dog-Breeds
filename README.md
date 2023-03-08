Image Classifier to Identify Dog Breeds

This project is an image classifier that can identify different breeds of dogs using deep learning techniques. The classifier is based on a convolutional neural network (CNN) that has been trained on a large dataset of dog images.

Installation

To use this project, you will need to have Python 3 installed on your system. You will also need to install the following Python packages:

numpy
pandas
matplotlib
seaborn
tensorflow
keras
You can install these packages using the following command:

pip install numpy pandas matplotlib seaborn tensorflow keras
Usage

To use the image classifier, you can run the predict_breed.py script. This script takes a path to an image file as input, and outputs the predicted breed of dog in the image.

python predict_breed.py /path/to/image/file
You can also run the test_classifier.py script to test the accuracy of the classifier on a test set of images.

python test_classifier.py
Dataset

The dataset used to train the classifier is the Stanford Dogs Dataset. This dataset contains over 20,000 images of 120 different dog breeds.

Model

The classifier is based on a convolutional neural network (CNN) that has been trained on the Stanford Dogs Dataset. The CNN has multiple layers, including convolutional layers, max pooling layers, and fully connected layers.

The model architecture used in this project is based on the VGG16 architecture. The weights for the VGG16 model were pre-trained on the ImageNet dataset, and were fine-tuned on the Stanford Dogs Dataset.

Results

The image classifier achieved an accuracy of 85% on the test set of images. The classifier was able to correctly identify the breed of dog in 85% of the images in the test set.


