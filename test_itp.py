import logging
import os
from azureml.core.run import Run

run = Run.get_context()
logging.basicConfig(level=logging.DEBUG)

# if __name__ == "__main__":
logging.info("This is from logging info %d", __file__)
print("print results here")
dataset = "/DATASET/luna16"
run.log("precision", 0.5)

print("print dir", os.listdir(dataset))
