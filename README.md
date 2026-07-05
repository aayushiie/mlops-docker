- playing around with docker
- creates an image for a sample flask app
---
```bash
# Build the Docker image and tag it
docker build -t my-app:latest .

# Run the container in detached mode on port 3000
docker run -d -p 3000:3000 --name running-app my-app:latest
```

