# MVP Data Pipeline

![Deploy](https://github.com/erikmunkby/mvp-data-pipeline-aws/workflows/CDK%20Deploy/badge.svg?branch=master)

Contains code for:

- Data pipeline in AWS
- Jupyter notebook for testing
- Github actions workflow for cdk deploy

## Requirements
Must have an AWS account with deploy access rights.

## Development

- Fork the repository
- Install [poetry](https://python-poetry.org/)
- Install AWS CDK

    `$ npm install -g aws-cdk`
    
- (Optional) Set poetry config settings to local virtual environments

    `$ poetry config virtualenvs.in-project true`

- Install dependencies and build Virual Environment

    `$ poetry install`
    
- Start the venv shell

    `$ poetry shell`
    
- (Optional) Load a specific AWS profile

    `$ export AWS_PROFILE=<your profile name>`

- Set up AWS CDK in the AWS environment

    `$ cdk bootstrap`
    
- Set up your github secrets with the following parameters:
    - AWSPUBLICKEY
    - AWSSECRETKEY
    
- Push to Main and watch your github actions deploy!

## Set up Jupyter
- Start the poetry shell (if you haven't already)
    
    `$ poetry shell`
    
- (Optional) Load a specific AWS profile

    `$ export AWS_PROFILE=<your profile name>`
    
- Build a jupyter kernel that the notebooks can use

    `$ python -m ipykernel install --user --name mvp-pipeline`
    
- Load up a jupyter notebook

    `$ jupyter notebook`
    
- Add `api_creds.json` file with the following parameters filled:
```
{
    "endpoint": "https://*******.amazonaws.com/prod/",
    "api-key": "******"
}
```
