import os
import subprocess

# Define input and output directories
input_dir = 'data/input'
output_dir = 'data/output'

model_path = "models/G_106000.pth"
config_path = "config.json"

os.makedirs(output_dir, exist_ok=True)

def run_command(audio_file, model_path, config_path, output_dir):
    # Prepare the command
    command = f"svc infer \"{audio_file}\" -m \"{model_path}\" -c \"{config_path}\""
    
    # Run the command
    try:
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was executed successfully
        if process.returncode == 0:
            print("Command executed successfully.")
            output_file = os.path.join(output_dir, os.path.basename(audio_file) + "_output.wav")
            with open(output_file, 'wb') as f:  # Open the file in binary mode ('wb')
                f.write(process.stdout.encode())  # Encode the string to bytes before writing
            print(f"Output saved to: {output_file}")
        else:
            print("Error in command execution.")
            print("Error:\n", process.stderr)
    except subprocess.CalledProcessError as e:
        print("Error in command execution.")
        print("Command output:\n", e.stdout)
        print("Command error output:\n", e.stderr)

        
# Loop through audio files in input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.wav'):
        audio_file = os.path.join(input_dir, filename)
        print(audio_file)
        run_command(audio_file, model_path, config_path, output_dir)
