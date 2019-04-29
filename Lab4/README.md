# Visual Question Answering
In this project we have used the MSCOCO data set from https://visualqa.org/download.html, In this we firstly need to download the Training annotations, Training questions and the COCO images datasets from the above given link.

After downloading, it needs to be unzipped and can be split into training and test dataset for model preparation.

## Requirements
- Python 3.6
- Tensorflow 1.3.0
- tensorboard for Visualizing

## Model
This model is implemented using Tensorflow of the VIS + LSTM visual question answering model from the paper Exploring Models and Data for Image Question Answering by Mengye Ren, Ryan Kiros & Richard Zemel. The model architectures vaires slightly from the original - the image embedding is plugged into the last lstm step (after the question) instead of the first. The LSTM model uses the same hyperparameters as those in the Torch implementation of neural-VQA.

## Steps for Achieving VQA
1. Collecting Data
2. Data Refining
3. Extracting the relavant features
4. Training the model (VGG-16 and Resnet in our case)
5. Testing the Dataset

### Collecting Data
After we have downloaded the required Annotations, Questions and Images with Caption dataset from MSCOCO dataset, I have placed them in a single directory named Data/

### Data Refining
![](https://github.com/charankottapalliCK/CS5542_BigDataAnalytics/blob/master/Lab4/documentation/Screen%20Shot%202019-04-29%20at%205.27.55%20PM.png)

1. Since the Data is huge(26MB!!), I have limited the dataset to only a few images with my set of keywords(sunflower, airplane, anchor, accordian, tuplis).

2. By fetching these respective imageIds of my keywords, I have minimized the model training time for the VQA on my dataset.
These results are then sent to a VGG-16 and Resnet model.

3. Next step, the coco openended questions, annotations are rewritten according the images being considered are passed to data_loader.py

4. We load the Train, validation annotations and question files to create a qa_data_file.json which consists of questions, question indices, answer confidence for training images that we have passed

5. Also a Vocab_file.json is created after execution of dataloader.py which consists of vocabulary dictionary for the questions, answers indices and , max_question_length

![](https://github.com/charankottapalliCK/CS5542_BigDataAnalytics/blob/master/Lab4/documentation/Screen%20Shot%202019-04-29%20at%205.32.59%20PM.png)

### Extract the Image features

#### Preprocess Questions/Answers


### Training the attention model

  
### Evaluating a trained model


## Generating Answers/Attention Distributions
#### Pretrained Model

## Sample Results



## References
