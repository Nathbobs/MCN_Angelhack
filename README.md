# Coupang Vendor Insight

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About

This is about 

## Features

- Sentimental Analysis
- Text-to-SQL
- LLM-RAG

## Installation

### Prerequisites

In other to start you'd need to install the following packages.

- SinglestoreDB 
- python3.8+

### Steps

SingleStoreDB installation on Linux (Centos)

```bash
yum install -y yum-utils
sudo yum-config-manager --add-repo https://release.memsql.com/production/rpm/x86_64/repodata/memsql.repo

sudo yum install -y singlestore-client singlestoredb-toolbox singlestoredb-studio

sdb-deploy cluster-in-a-box --license <input-Licence-from-the-website> --password PASSW0RD

# Navigate into the project directory
cd text-summarization-LLM-RAG

# Install the dependencies
python -m pip install -r requirements.txt

