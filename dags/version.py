import os
import secrets

# Generate a random secret key
def generate_secret_key():
    return secrets.token_hex(16)

# Set the environment variable
os.environ['AIRFLOW_WEBSERVER_SECRET_KEY'] = generate_secret_key()

# Print the generated secret key
print("AIRFLOW_WEBSERVER_SECRET_KEY:", os.environ['AIRFLOW_WEBSERVER_SECRET_KEY'])
