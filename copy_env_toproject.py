import shutil

# Source path
source = ".env"

# Destination path
destination = "project/config/.env"

# Copy the content of source to destination
shutil.copy2(source, destination)

print(f"Content of {source} copied to {destination}")
