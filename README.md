# gpt-latex-translator
A tool to translate LaTeX documents using OpenAI's GPT-3 API.

The tool is intented for translating academic texts written as LaTeX projects. It takes the directory of the project and traslate every .tex file from English to Spanish (customizable). Commented out lines will not be translated.

# Installation 
Install the package with the following command
```
pip install .
```
Now you should be able to run `gpt-translate` command line tool.

# Usage
### OpenAI API
The tool uses the model [gpt-3.5-turbo](https://platform.openai.com/docs/guides/chat). You'll need to provide your OpenAI API key through the environment variable `OPENAI_API_KEY`. For example, you could call the tool using:

```OPENAI_API_KEY="your-key" gpt-translate args```

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

`--dry-run` is specially helpful to perform a cost estimation based on the number of tokens (see https://openai.com/pricing). Remember that both input and output tokens count for pricing.

## Problems and workarounds

- The translation might not behave well with large blocks of LaTeX text where there is a mayority of LaTeX symbols over natural language words. The main example of this is big tables. One way around this is to comment the whole block to avoid this block being translated.
- From time to time, the translation might remove a closing command such as `\end{example}`. This might be due to the way the tool splits the file into chunks to comply with the token limit imposied by OpenAI's API. Inspecting the compilation output together with the original backup file should help finding this quickly.
