# test-darshan-12

12

## Overview

This is a api-service built with Python 3.12, created using the Backstage GitHub Repository Generator template.

## Features

- **Application Type**: api-service
- **Runtime**: Python 3.12
- **Port**: 3000
- **Containerized**: Docker support included
- **Kubernetes Ready**: Helm charts included
- **Auto-scaling**: Horizontal Pod Autoscaler configured (2-10 replicas)
- **Health Checks**: Liveness and readiness probes configured
- **CI/CD Pipeline**: Trunk-based deployment with GitHub Actions (auto-deploy to dev, manual promote to staging/prod)

## Getting Started

### Prerequisites

- Python 3.12+
- pip
- Docker (for containerization)
- Kubernetes cluster (for deployment)
- Helm 3+ (for chart deployment)

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/radaisystems/test-darshan-12.git
   cd test-darshan-12
   ```

2. Navigate to the app directory:
   ```bash
   cd app/python
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Adding Extra Packages**: Edit `app/python/requirements.txt` to uncomment and add any additional Python packages you need. Common packages are already listed as examples.

4. Start the application:
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:3000`

### Running Tests

```bash
cd app/python
pytest
```

### Health Checks

- **Health**: `GET /health` - Application health status
- **Readiness**: `GET /ready` - Application readiness status

## Docker

### Build the Docker image:
```bash
docker build -t radaisystems/test-darshan-12:latest .
```

### Run the container:
```bash
docker run -p 3000:3000 radaisystems/test-darshan-12:latest
```

## Kubernetes Deployment

### Using Helm

1. Install the Helm chart:
   ```bash
   helm install test-darshan-12 ./infrastructure/helm
   ```

2. Upgrade the deployment:
   ```bash
   helm upgrade test-darshan-12 ./infrastructure/helm
   ```

3. Uninstall:
   ```bash
   helm uninstall test-darshan-12
   ```

### Configuration

The Helm chart supports the following key configurations:

- **Replicas**: 2 (initial)
- **Auto-scaling**: 2-10 replicas
- **CPU Threshold**: 70%
- **Memory Threshold**: 80%
- **Resources**:
  - CPU: 100m (request), 500m (limit)
  - Memory: 128Mi (request), 512Mi (limit)
- **Service Type**: ClusterIP

### Customize Values

Edit `infrastructure/helm/values.yaml` to customize the deployment according to your needs.

## Deployment Strategy (Trunk-Based)

This project uses **trunk-based deployment** for continuous delivery:

### Automatic Deployments
- **Development**: Auto-deployed on every push to `main` branch
- **Testing**: All PRs are automatically tested before merge

### Manual Deployments (Promotion)
- **Staging**: Manual trigger via GitHub Actions
- **Production**: Manual trigger via GitHub Actions (requires approval)

### How to Deploy

1. **To Development** (Automatic):
   ```bash
   git push origin main
   # Automatically deploys to development environment
   ```

2. **To Staging** (Manual):
   - Go to GitHub Actions → CI/CD Pipeline → Run workflow
   - Select "staging" environment
   - Click "Run workflow"

3. **To Production** (Manual):
   - Go to GitHub Actions → CI/CD Pipeline → Run workflow  
   - Select "production" environment
   - Click "Run workflow"
   - Requires production environment approval

### Rollback Strategy
```bash
# Emergency rollback (if needed)
kubectl rollout undo deployment/test-darshan-12 -n <environment>

# Or re-run workflow with previous stable version
```

## Project Structure

```
test-darshan-12/
├── README.md
├── catalog-info.yaml          # Backstage catalog definition
├── Dockerfile                 # Container definition
├── .github/                   # CI/CD workflows
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions pipeline
├── app/                       # Application code
│   └── python/
│       ├── main.py            # Python Flask application
│       ├── requirements.txt   # Python dependencies
│       ├── __init__.py
│       └── tests/             # Test files
│           ├── __init__.py
│           └── test_main.py
└── infrastructure/
    └── helm/                  # Helm chart
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── deployment.yaml
            ├── service.yaml
            ├── hpa.yaml       # Horizontal Pod Autoscaler
            └── ...
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request