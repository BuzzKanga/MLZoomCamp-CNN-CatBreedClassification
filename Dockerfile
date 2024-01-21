FROM public.ecr.aws/lambda/python:3.8

# install libraries required into container
RUN pip install pillow
RUN pip install tflite-runtime==2.7.0
RUN pip install requests

# copy model and program to call model into container
COPY catbreeds-model.tflite .
COPY lambda_function.py .

# set up container for AWS lambda function
CMD ["lambda_function.lambda_handler"]

