# BRAIN TUMOR SEGMENTATION USING UNET,MULTIRES UNET & PROPOSED UNET MODELS

1. This Dataset consists of 3929 images and their corresponding mask.All the images and masks are pre-processed and resized to 256x256x1 before feeding into the Unet,Multires Unet and Proposed Unet.The pre-processed dataset can be accessed using the following link https://buffalo.app.box.com/v/BrainTumorDependentFiles/folder/94776422608

2. To evalute the model performance we have used DICE score as the metric and DICE loss function.

3. The Ipyhton notebook "Unet_Model_Training.ipnynb" explains the training of Unet model.

4. The Ipyhton notebook "multires_Unet_Train.ipnynb" explains the training of MultiRes-Unet model.

5. The Ipyhton notebook "Proposed_unet_train.ipnynb" explains the training of Proposed Unet model.
We Propose a U-net model that gives a Better result compared to the Normal Unet and MultiRes Unet model.
Our proposed model consists of a Dowsampling Path, Proposed Multires Upath and an Upsampling Path.

5.1. Down Sampling Block Architecture: Its consists of 4 Downsampling blocks
 
 *  Conv_layer---->Batch Normalization----> Conv_layer----> Max pooling layer
                                    
5.2. Up Sampling Block Architecture: Its consists of 4 Upsampling blocks

 *  Skip_connection + Input from previous Conv_layer->Batch Normalization->Conv_layer->Batch Normalization->Conv_layer->Up sampling layer

5.3. Proposed MultiRes Path: The inspiration to this is architecture is derived from this paper:https://arxiv.org/pdf/1902.04049.pdf. However, the skip connections that we have defined is different interms of its architecture.

In The paper,the authors have used Respaths that connects the Encoder and Decoder in the following manner:
1. The first Respath has length 4 with 32 filters each
2. The Second Respath has length 3 with 64 filters each
3. The Third Respath has length 2 with 128 filters each
4. The fourth Respath has length 1 with 256 filters each

In the model that we have proposed, the Respath in the following manner:
1. The first Respath has length 1 with 32 filters each
2. The Second Respath has length 2 with 64 filters each
3. The Third Respath has length 3 with 128 filters each
4. The fourth Respath has length 4 with 256 filters each

Explanation for the choosen architecture: The convolution neural networks only learns low level features such as lines, edges and corners in the earlier layers.Furthermore, as the networks grows in depth, the convolution neural networks can capture more and a finer context present in an image.Hence, we felt using more number of conv_layers in the first Respath was not a good idea and we have only used length 1 in the first Respath,length 2 conv_layer in the second Respath,length 3 conv_layer in the third Respath and length 4 in the fourth Respath that contains more context of the image.Also, this model architecture resulted in a imporved performance and we achieved a highest validation Dice score of 0.8702

# TRAINED MODELS
All the three trained models with weights can be accessed using the following link https://buffalo.app.box.com/v/BrainTumorDependentFiles/folder/94778410225 
These trained models can be used for generating the segmentation maps for a given image.

# COMPARING THE PERFORMANCE OF THE MODELS
1. The Ipython notebook "TestimagesegmentationModels.ipynb" can be used to visualize the Train and Validation - Mertics,Losses.

2. It aslo provides a comparison bewteen the with ground truth and segmentation maps given the three models
