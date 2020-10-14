from enum import EnumMeta
from azureml.tensorboard import Tensorboard
import argparse
import os
import subprocess
import re
import json
from pathlib import Path

output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "OUTPUT")


def parse_args():
    parser = argparse.ArgumentParser(description="Tensorboard to monitor metrics.")
    parser.add_argument('run', type=str, help="Experiment id to monitor.")
    return parser.parse_args()



def tensorboard():
    args = parse_args()
    tb = Tensorboard([args.run])
    # If successful, start() returns a string with the URI of the instance.
    tb.start()

    # # After your job completes, be sure to stop() the streaming otherwise it will continue to run. 
    # tb.stop()

if __name__ == "__main__":
    output = subprocess.getoutput('vislib-log list').split('\n')
    exp_id = []
    for i, each in enumerate(output):
        if i == 0:
            continue
        x = re.split(r'\s\s+', each)
        exp_id.append(x[1])
    
    output_storage = json.load(open(os.path.join(Path.home(), '.config/vislib-toolbox.log.json'), 'r'))
    account = output_storage["storage"]["account"]
    secret = output_storage["storage"]["secret"]
    from datetime import datetime, timedelta
    from azure.storage.blob import BlockBlobService

    blob = BlockBlobService(account, secret)

    container = exp_id[0]
    for name in blob.list_blob_names(container):
        local_path = os.path.join(output_dir, container, name)
        try:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
        except:
            pass
        blob.get_blob_to_path(container, name, os.path.dirname(local_path), max_connections=20)
