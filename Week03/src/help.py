def help():
    print("Usage: python3 main.py [Command]\n"
          "a complete pipeline for training and deploying our machine-learning models using Gradio!\n"
          "this allows as to train our model and then deploy it as an interactive demo.\n"
          "COMMANDS:\n"
          "      train,  -t     used to Train our model and displaying two describing plots.\n"
          "      deploy, -d     Launch a Gradio interface to allow users to test our model.\n"
          "              -g     Deploy the model using Gradio."
          "              -s     Deploy the model using Streamlit."
          "      help,   -h      display this help text and exit.")
    