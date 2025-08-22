# API Test Runner

A simple tool for automated API testing using Python and Docker.

## Features
- Automatically tests APIs listed in a configuration file.
- Runs tests inside Docker for consistent environments.
- Easy to extend with new APIs.

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/0smoienh0/api-test-runner.git
cd api-test-runner
pip install -r requirements.txt
```

## Running the Application
Build and run the monitoring app with Docker:

```bash
docker network create my-network
docker build -t monitoring-app .
docker run -d --name monitoring-app --network my-network -p 8000:8000 monitoring-app
```

## Running the Tests
Run the API tests inside Docker:

```bash
docker run --rm --network my-network api-test-runner
```

## Configuration
APIs to test are listed in `config/apis.json`. Update this file to add or remove endpoints.

## License
MIT License
