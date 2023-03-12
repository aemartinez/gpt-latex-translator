# gpt-latex-translator
A tool to translate LaTeX documents using OpenAI's GPT-3 API.

The tool is intented for translating academic texts written as LaTeX projects. It takes the directory of the project and traslate every .tex file from English to Spanish (this is configurable). 

# Installation 
Install the package with the following command
```
pip install .
```
Now you should be able to run `gpt-translate` command line tool.

# Usage
### OpenAI API
The tool uses the model [gpt-3.5-turbo](https://platform.openai.com/docs/guides/chat). You'll need to provide your OpenAI API key through the environment variable `OPENAI_API_KEY`. For example, you could call the tool using `OPENAI_API_KEY="your-key" gpt-translate args`. 

### Command line tool
```
gpt-translate [-h] [-s] [-v] [--dry-run] [--source-language source_language]
              [--target-language target_language]
              path
```

### arguments/options:
- `path`: the path of the directory or file to translate
- `-h, --help`: show this help message and exit
- `-s, --single`: treat path as a single file
- `-v, --verbose`: print verbose output
- `--dry-run`: do not translate, just print the files that would be translated and the number of tokens that would be sent to the API
- `--source-language source_language`: the name of the source language (default: English)
- `--target-language target_language`: the name of the target language (default: Spanish)