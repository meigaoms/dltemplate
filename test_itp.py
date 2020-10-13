import logging
import os
from azureml.core.run import Run

logging.basicConfig(level=logging.DEBUG)
# if __name__ == "__main__":
logging.info("This is from logging info %s", __file__)
print("print results here")
dataset = "DATASET"

print("print dir", os.listdir(dataset))


run = Run.get_context()

run.log('alpha', 1.23)
