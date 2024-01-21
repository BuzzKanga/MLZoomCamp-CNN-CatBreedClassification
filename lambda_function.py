# import lrequired libraries
from PIL import Image
import numpy as np
import tflite_runtime.interpreter as tflite
import requests
from io import BytesIO


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

# set-up model
interpreter = tflite.Interpreter(model_path="catbreeds-model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]


def predict(url):
    response = requests.get(url)
    with Image.open(BytesIO(response.content)) as img:
        img = img.resize((299, 299), Image.NEAREST)

    # image pre-processing
    x = np.array(img, dtype="float32")
    X = np.array([x])   

    X /= 127.5
    X -= 1.0


    # make prediction
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
