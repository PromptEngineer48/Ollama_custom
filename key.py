import os

# Set the environment variable to the path of id_ed25519.pub
os.environ['PUB_KEY_PATH'] = os.path.expanduser("~/.ollama/id_ed25519.pub")

# Now you can access the environment variable in your Python code
pub_key_path = os.getenv('PUB_KEY_PATH')
print(pub_key_path)  # Verify that the path is correctly set

# Read the contents of the public key file
with open(pub_key_path, 'r') as f:
    public_key = f.read()

# Print the public key
print(public_key)
