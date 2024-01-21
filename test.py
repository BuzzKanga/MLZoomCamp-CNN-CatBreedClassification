import requests

# url = "http://localhost:8080/2015-03-31/functions/function/invocations"
url = "https://nekc22pysf.execute-api.ap-southeast-2.amazonaws.com/test/predict"

data = {
    "url": "https://raw.githubusercontent.com/BuzzKanga/MLZoomCamp-CNN-CatBreedClassification/master/Abyssinian_104.jpg"
}

result = requests.post(url, json=data).json()

print(result)
