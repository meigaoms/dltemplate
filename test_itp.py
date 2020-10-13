import logging
import os

logging.basicConfig(level=logging.DEBUG)
# if __name__ == "__main__":
logging.info("This is from logging info %s", __file__)
print("print results here")
dataset = "DATASET/luna16"

print("print dir", os.listdir(dataset))


import mlflow
with mlflow.start_run():
    mlflow.log_metric("example", 1.23)
