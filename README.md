# go-cheat-check

go-cheat-check is a tool designed to generate Go code examples and compare them against suspected generated code. This system is particularly useful for technical interview questions and software development learning scenarios.

## Features

- Generate multiple Go code examples based on a given prompt using OpenAI's GPT-4 model.
- Compare a target Go file against a set of reference files to determine code similarity.
- Calculate similarity scores for various aspects of the code, including package names, imports, functions, and comments.

## Installation

To install go-cheat-check, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/referefref/go-cheat-check.git
   ```

2. Change to the project directory:
   ```
   cd go-cheat-check
   ```

3. Install the required Python packages:
   ```
   pip install openai
   ```

4. Set up your OpenAI API key:
   - Create a file named `.env` in the project root directory.
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

### Generating Go Code Examples

To generate Go code examples, use the `generateExamples.py` script:

```
python generateExamples.py "<your_prompt>" <number_of_files> <output_directory>
```

Example:
```
python generateExamples.py "Write a Go function to find the factorial of a number" 5 ./generated_examples
```

This will generate 5 Go files in the `./generated_examples` directory, each containing a function to calculate the factorial of a number.

### Comparing Go Code

To compare a target Go file against a set of reference files, use the `compare.py` script:

```
python compare.py <target_file> <reference_file1> <reference_file2> ...
```

Example:
```
python compare.py ./submitted_code.go ./generated_examples/generated_code_1.go ./generated_examples/generated_code_2.go
```

This will compare `submitted_code.go` against the two generated example files and provide similarity scores for various aspects of the code.

## Contributing

Contributions to go-cheat-check are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational and interview preparation purposes only. Please use responsibly and in accordance with academic integrity policies.
