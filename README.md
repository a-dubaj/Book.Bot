## Text Analysis bot

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