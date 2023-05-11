# VPC CLI Tool

This Python script provides a command-line interface (CLI) program that helps with managing Virtual Private Clouds (VPCs) in AWS. The script utilizes the `argparse` library for command-line argument parsing and the `boto3` library to interact with the AWS EC2 service. The script allows you to create a VPC, create an Internet Gateway (IGW), and attach the IGW to a VPC.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system
- AWS credentials properly configured for programmatic access

## Installation

To use the script, follow these steps:

1. Install the required Python libraries by running the following command:

    ```bash
    pip install boto3
    pip install botocore
2. Save the script to a file, for example, main.py.
## Usage
Run the script with the desired command and arguments to perform specific actions related to VPC management.
  
    python main.py [command] [options]

# Commands
The script supports the following commands:
vpc: Create a new VPC.
igw: Create a new Internet Gateway.
attach: Attach an existing IGW to an existing VPC.

## Options
The script accepts the following options:

--vpc_name: Name of the VPC (required for the vpc command).
--igw_name: Name of the Internet Gateway (required for the igw command).
--vpc_id: ID of the VPC (required for the attach command).
--igw_id: ID of the Internet Gateway (required for the attach command).

## Examples
# Create a VPC
To create a new VPC, use the vpc command along with the --vpc_name option:

    python main.py vpc --vpc_name my-vpc

This will create a new VPC with the specified name.

# Create an Internet Gateway
To create a new Internet Gateway, use the igw command along with the --igw_name option:

    python main.py igw --igw_name my-igw
This will create a new Internet Gateway with the specified name.

# Attach an Internet Gateway to a VPC
To attach an existing Internet Gateway to an existing VPC, use the attach command along with the --vpc_id and --igw_id options:

    python main.py attach --vpc_id vpc-12345678 --igw_id igw-12345678
This will attach the specified Internet Gateway to the specified VPC.

## License
This script is licensed under the MIT License.
