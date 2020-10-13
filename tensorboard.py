from azureml.tensorboard import Tensorboard
import argparse


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
    tensorboard()