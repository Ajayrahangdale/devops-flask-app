# DevOps Flask Application

A simple Python Flask application containerized using Docker.  
This project is used to practice DevOps tools like Docker, GitHub, CI/CD, Terraform, and Kubernetes.

## Project Structure

devops-flask-app/
 ├── app.py
 ├── requirements.txt
 ├── Dockerfile
 └── README.md
## Run Locally

1. Install dependencies:
pip install -r requirements.txt
  
2. Start Flask App:

python app.py

## Docker Commands

### Build Image
docker build -t dockerflask .
### Run Container
docker run -p 5000:5000 dockerflask

### Push to Docker Hub

docker tag dockerflask <your-dockerhub-username>/dockerflask:v1
docker push <your-dockerhub-username>/dockerflask:v1

## Technologies Used
- Python Flask
- Docker
- Git & GitHub
- Linux
- CI/CD (Jenkins) – Coming Soon
- Terraform – Coming Soon
- Kubernetes – Coming Soon
- AWS (EC2 Deployment) – Final Step
## Future Enhancements
- CI/CD pipeline using Jenkins
- Terraform for infrastructure automation
- Kubernetes deployment
- AWS EC2 deployment

## Author
**Ajay Rahangdale**  
DevOps Engineer (In Progress)
