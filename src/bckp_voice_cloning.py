import torch
import torch.nn as nn
import torchaudio
import librosa
import numpy as np
import os 
import subprocess

from IPython.display import Audio, display
import os

# Filenames
audio_filename =  'test.wav'
model_filename =  'G_106000.pth'
config_filename = 'config.json'

# Construct the full local paths
audio_file = f"\"{os.path.join('data', audio_filename)}\""
model_path = f"\"{os.path.join('models', model_filename)}\""
config_path = f"\"{os.path.join('models', config_filename)}\""


def run_command(audio_file, model_path, config_path):
    # Prepare the command
    command = f"svc infer {audio_file} -m {model_path} -c {config_path}"
    
    # Run the command
    try:
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was executed successfully
        if process.returncode == 0:
            print("Command executed successfully.")
            print("Output:\n", process.stdout)
        else:
            print("Error in command execution.")
            print("Error:\n", process.stderr)
            print("Command output:\n", process.stdout)
    except subprocess.CalledProcessError as e:
        print("Error in command execution.")
        print("Command output:\n", e.stdout)
        print("Command error output:\n", e.stderr)

run_command(audio_file, model_path, config_path)
