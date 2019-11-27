# DATASET DISCRIPTION

1. This Dataset consists of 3929 images and their corresponding mask.All the images and masks are pre-processed and resized to 256x256x1 before feeding into the Unet,Multires Unet and Proposed Unet.The pre-processed dataset can be accessed using the following link https://buffalo.app.box.com/v/BrainTumorDependentFiles/folder/94776422608

2. To evalute the model performance we have used DICE score as the metric and DICE loss function.

3. The Ipyhton notebook "Unet_Model_Training.ipnynb" explains the training of Unet model.

4. The Ipyhton notebook "multires_Unet_Train.ipnynb" explains the training of MultiRes-Unet model.

5. The Ipyhton notebook "Proposed_unet_train.ipnynb" explains the training of Proposed Unet model.


