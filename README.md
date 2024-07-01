## Text Analysis bot

[![Docker Build and Push](https://github.com/a-dubaj/Book.Bot/actions/workflows/docker-build.yml/badge.svg)](https://github.com/a-dubaj/Book.Bot/actions/workflows/docker-build.yml) [![Test and Lint](https://github.com/a-dubaj/Book.Bot/actions/workflows/test-and-lint.yml/badge.svg)](https://github.com/a-dubaj/Book.Bot/actions/workflows/test-and-lint.yml)[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3108/) [![Docker](https://img.shields.io/badge/Docker-latest-blue.svg)](https://hub.docker.com/repository/docker/coffeina/bookbot)


### Description

This project is a simple text analysis tool that reads the text from "Frankenstein" by Mary Shelley, analyzes the number of words, and counts the frequency of each character in the text. The tool then generates a report summarizing these statistics.


### Features

- Reads the text from a specified file.
- Counts the number of words in the text.
- Analyzes the frequency of each character (ignoring case).
- Generates a sorted list of character frequencies.
- Outputs a report with the word count and character frequencies.

### Installation

To run this project, you'll need Docker and pre-commit installed on your machine.

- Clone this repository:
    ```bash
    git clone https://github.com/yourusername/text-analysis-frankenstein.git
    cd text-analysis-frankenstein
    ```

- Set up pre-commit hooks:
    ```bash
    pre-commit install
    ```

- Pull the Docker image from Docker Hub:
    ```bash
    docker pull coffeina/bookbot
    ```

- Run the Docker container:
    ```bash
    docker run --rm coffeina/bookbot
    ```


### Usage

To execute the script within the Docker container, simply follow the installation steps and run the container. The output will be a report printed in the console, showing the number of words and the frequency of each character in the text.

### Code Overview

- `main()`: The main function that orchestrates reading the text, analyzing it, and printing the report.

- `get_book_text(path)`: Reads the text from the specified file and returns it as a string.

- `get_num_words(text)`: Splits the text into words and returns the word count.

- `get_chars_dict(text)`: Counts the frequency of each character in the text and returns a 
dictionary with characters as keys and their frequencies as values.

- `chars_dict_to_sorted_list(num_chars_dict)`: Converts the character frequency dictionary to a sorted list of dictionaries.

- `sort_on(d)`: Helper function for sorting dictionaries by the 'num' key.


### Dockerfile

 ```bash
# Build from a slim Debian/Linux image
FROM debian:stable-slim

# Copy our code into the image
COPY main.py main.py

# Copy our data dependencies
COPY books/ books/

# Update apt
RUN apt update
RUN apt upgrade -y

# Install build tooling
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# Download Python interpreter code and unpack it
RUN wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
RUN tar -xf Python-3.10.*.tgz

# Build the Python interpreter
RUN cd Python-3.10.8 && ./configure --enable-optimizations && make && make altinstall

# Run our Python script
CMD ["python3.10", "main.py"]
```