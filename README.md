# FinanceNewsAnalyzer Crew

The project is scrape data about market news and create a summary in report.md file.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:

```bash
poetry lock
```

```bash
poetry install
```

## Running the Project

Run this from the root folder of your project:

```bash
poetry run finance_news_analyzer
```

This command initializes the finance_news_analyzer Crew, assembling the agents and assigning them tasks as defined in configuration.

This project will create a `report.md` file with the output of a research on LLMs in the root folder.
