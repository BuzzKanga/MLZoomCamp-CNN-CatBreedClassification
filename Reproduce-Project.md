# Reproduce Project

## Pre-requisites

The following are assumed to be available and running in a Unix environment:

- python

- git

- docker

The steps to reproduce the project are listed below:

## 1. Model Training

### 1.1 Clone the repo

Run the following command to clone the project repo

```
git clone https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification.git
```

### 1.2 Prepare the data

Run all the cells in the the following notebook: [notebook.prepare_data.ipynb](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/notebook.prepare_data.ipynb). 
This will download the data set, extract the data and split the data into train, validation and test data sets. Folders will be created for each dataset.

### 1.3. Build a docker image

To build a docker container the following [Dockerfile](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/Dockerfile) will be used.

`docker build -t catbreeds-model .`

This will build a container with: 

- a copy of the catbreeds.model.tflite

- a function to call the model from AWS lambda



## 2. Model Inference

To test the model the following prerequisutes are required:

Deploy container created in Step 1.3 above to lambda function

Create AWS API Gateway and define API with post request to call the lambda_function.predict function with input as the url of the cat image to be used for inference.

The function will return the values calculated for each of the breeds. The largest number will indicate which breed the model has identified as the one the cat belongs to.
