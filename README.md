# Coupang Vendor Insight

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Technologies](#Technologies)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About

Coupang’s current business model demands that it places the burden of quality assurance on its vendors. Although coupang has been able to leverage this to offer its users  extremely fast and affordable delivery, the quality of such products could certainly be better. 

### Goal
We propose leveraging Coupang’s vast review data on product reviews in addition to  recent AI technologies to implement a Vendor evaluation pipeline and tool.

## Technologies
- LLM model gpt-3.5-turbo
- SinglestoreDB vector database
- python3.8+
- Natural Language Processing (NLP)
- Responsive Design <Html, javascript, css> 

### Prerequisites

In other to start you'd need to install the following packages.

- SinglestoreDB 
- python3.8+

### installation

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

## Features

- Review sentiment analysis
  This feature processes product reviews and determines the overall sentiment (positive, negative, or neutral) expressed by customers.

- LLM based on Review summarization
  This uses text to sql technique to query from the database and makes a summarization with RAG

- Vendor evaluation tool
  This tool aggregates the sentiment analysis and  review summarisation across vendor reeviews to evaluate them


