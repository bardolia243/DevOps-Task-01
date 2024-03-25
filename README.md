# Basic Python Web Server Dockerized and Hosted on EC2

This repository contains a basic Python web server that says "hello world", Dockerized for easy deployment, and hosted on an Amazon EC2 instance.

## Instructions

### Running Locally

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/basic-python-web-server.git
    cd basic-python-web-server
    ```

2. Build the Docker image:

    ```bash
    docker build -t hello-world-server .
    ```

3. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 hello-world-server
    ```

4. Access the server at [http://localhost:8000](http://localhost:8000) in your web browser.

### Hosting on EC2

1. Launch an EC2 instance:

    - Choose an appropriate AMI (Amazon Linux, Ubuntu, etc.).
    - Configure security groups to allow inbound traffic on port 8000 (HTTP).
    - Note the public IP address of your EC2 instance.

2. SSH into your EC2 instance:

    ```bash
    ssh -i your-key.pem ec2-user@your-ec2-public-ip
    ```

3. Install Docker on the EC2 instance:

    ```bash
    sudo apt update -y
    sudo yum install docker -y
    sudo service docker start
    sudo usermod -a -G docker ubuntu
    ```

4. Transfer your Docker image to the EC2 instance using `docker save` and `docker load` commands or a service like AWS ECR.

5. Load the Docker image on the EC2 instance:

    ```bash
    docker load -i <path_to_your_image.tar>
    ```

6. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 hello-world-server
    ```

7. Access the server using your EC2 instance's public IP address, for example: [http://your-ec2-public-ip:8000](http://your-ec2-public-ip:8000).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
