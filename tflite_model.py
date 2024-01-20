# import lrequired libraries
from PIL import Image
import numpy as np
import tflite_runtime.interpreter as tflite


# load test data
path = "./data/test/Abyssinian"
name = "Abyssinian_104.jpg"
fullname = f"{path}/{name}"

with Image.open(fullname) as img:
    img = img.resize((299, 299), Image.NEAREST)


def preprocess_input(x):
    x /= 127.5
    x -= 1.0
    return x


x = np.array(img, dtype="float32")
X = np.array([x])

X = preprocess_input(X)


# set-up model
interpreter = tflite.Interpreter(model_path="catbreeds-model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]


# make prediction
interpreter.set_tensor(input_index, X)
interpreter.invoke()
preds = interpreter.get_tensor(output_index)


# prepare output
classes = [
    "Abyssinian",
    "American Bobtail",
    "American Curl",
    "American Shorthair",
    "Bengal",
    "Birman",
    "Bombay",
    "British Shorthair",
    "Egyptian Mau",
    "Exotic Shorthair",
    "Maine Coon",
    "Manx",
    "Norwegian Forest",
    "Persian",
    "Ragdoll",
    "Russian Blue",
    "Scottish Fold",
    "Siamese",
    "Sphynx",
    "Turkish Angora",
]

print(dict(zip(classes, np.round(preds[0], 4))))
