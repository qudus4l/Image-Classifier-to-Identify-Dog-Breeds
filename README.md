# Image-Classifier-to-Identify-Dog-Breeds

In this project, I used a created image classifier to identify dog breeds.

A city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information.

Tasks:
-Using Python, determine which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs".
-Determine how well the "best" classification algorithm works on correctly identifying a dog's breed. If you are confused by the term image classifier look at it simply as a tool that has an input and an output. The Input is an image. The output determines what the image depicts. (for example, a dog). Be mindful of the fact that image classifiers do not always categorize the images correctly.
-Time how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more time to run and use more computational resources to run.

The model architecture I feel did the best at classifying the four uploaded images is Vgg. This is because:
1. It classified the coffee mug as cup.
2. Unlike the Alexnet which also classified the coffee mug as a cup, it classified the gecko as a gecko. The Alexnet was not able to.
3. It classified dogs and not dogs better.

The rest of my observations are documented in check_images.txt
