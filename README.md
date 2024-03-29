# MLZoomCamp 2023 Capstone Project

# CNN-CatBreedClassification

Capstone Project for MLZoomCamp Course - Use CNN deep learning model to identify cat breeds

## Problem Description

This is a project about cats ... and who doesn't like cats :) 

Identifying a breed of a cat from an image can help owners identify the breed of cat if they don't already know. 

However, this project is to test the limits of a deep learning model and to determine if cat breeds look significantly different to a CNN model for it to be accurately determine which breed they are

![cat-breeds.png](cat-breeds.png)

Once the CNN model has been trained, a user will be able to submit a photograph of a cat and the model will try to identify which breed the cat is from a set of 20 breeds that the model is trained upon.
The model will not be sophisticated enough to identify if a cat is from a breed that is not from one of the 20 popular cat breeds used for training the model. This is a possible future enhancement for the model.

## Dataset

The dataset used is available from [Kaggle](www.kaggle.com) at the following url: [CatBreedsRefined-7k](https://www.kaggle.com/datasets/doctrinek/catbreedsrefined-7k)

The breeds included are:
Abyssinian, American Curl, American Shorthair, Bengal, Birman, Bombay, Bristish Shorthair,  Egyptian Mau, Exotic Shorthair, Himalayan, Maine Coon, Manx, Munchkin, Norwegian Forest,  Persian , Regdoll, Russian Blue , Scottish Fold, Siamese , Sphynx.

## Project Deliverables

| Area                                 | Criteria                                                                                                                                                                                        | Reference                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Problem Description                  | Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used                                                                         | This document                                                                                                                                                                                                                                                                                                                           |
| EDA                                  | For images: analyzing the content of the images.                                                                                                                                                | See [notebook](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/notebook.ipynb) - **Explore** section                                                                                                                                                                                                       |
| Model Training                       | Trained multiple models and tuned their parameters.                                                                                                                                             | See [notebook](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/notebook.ipynb) section Build Baseline Model and :<br>Iteration 1: Adjust Learning Rate<br>Iteration 2: Implement callbacks<br>Iteration 3: Add more layers <br> Iteration 4: Dropout and regularisation <br>Iteration 5: Larger image size |
| Exporting notebook to script         | The logic for testing the model is exported to a separate script                                                                                                                                | See [test_python.py](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/test_python.py)                                                                                                                                                                                                                       |
| Reproducibility                      | it's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data | See [Reporduce-Project.md](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/Reproduce-Project.md)                                                                                                                                                                                                           |
| Model Deployment                     | Model is deployed AWS Lambda and API Gateway.                                                                                                                                                   | See [Cloud-Deployment.md](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/Cloud-Deployment.md)                                                                                                                                                                                                             |
| Dependency and enviroment management | Provided a file with requirements.txt dependency file with instructions on how to install dependencies.                                                                                         | See [Dependencies.md](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/Dependencies.md)                                                                                                                                                                                                                     |
| Containerization                     | The application is containerized and the README describes how to build a contained and how to run it                                                                                            | See [Containerisation.md](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/Containerisation.md)                                                                                                                                                                                                             |
| Cloud deployment                     | There's code for deployment to cloud or kubernetes cluster (local or remote). There's a URL for testing - or video/screenshot of testing it                                                     | See [Cloud-Deployment.md](https://github.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/blob/main/Cloud-Deployment.md)                                                                                                                                                                                                             |
