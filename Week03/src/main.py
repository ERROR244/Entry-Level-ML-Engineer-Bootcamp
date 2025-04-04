import sys
from train_the_model import train
from deploy_the_model import deploy_gradio, deploy_streamlit
from help import help

def main(CMD):
    if CMD == 'train' or CMD == '-t':
        train()
    elif CMD == 'deploy -g' or CMD == '-dg'or CMD == '-gd':
        deploy_gradio()
    elif CMD == 'deploy -s' or CMD == '-ds'or CMD == '-sd':
        deploy_streamlit()
    elif CMD == 'help' or CMD == '-h':
        help()
    else:
        print(f"main.py: invalid Command -- '{CMD}'")
        print("Try 'python3 main.py help' for more information.")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage: python3 main.py [Command]")
        print("Try 'python3 main.py help' for more information.")
