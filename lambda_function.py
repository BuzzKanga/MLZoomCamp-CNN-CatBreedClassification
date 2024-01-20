# import tensorflow.lite as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor("xception", target_size=(150, 150))

interpreter = tflite.Interpreter(model_path="catbreeds-model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

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

# url = 'https://raw.githubusercontent.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/master/Abyssinian_1.jpg'


def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    return dict(zip(classes, preds[0]))


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result
