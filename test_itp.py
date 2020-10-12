import logging
import os
import mlflow



# if __name__ == "__main__":
logging.info("This is from logging info %d", __file__)
print("print results here")
dataset = "/DATASET/luna16"
mlflow.log_metric("precision", 0.5)

print("print dir", os.listdir(dataset))
