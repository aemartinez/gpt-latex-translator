# gpt-latex-translator
A tool to translate LaTeX documents using OpenAI's ChatGPT API.

gpt-latex-translator is a tool that uses OpenAI's ChatGPT API to translate LaTeX documents (by default, from English to Spanish). This tool is intended for academic texts written in LaTeX projects.

# Installation 
Install the package with the following command:
```
pip install .
```
After installation, you should be able to run the `gpt-translate` command-line tool.

# Usage
### OpenAI API
The tool uses the [gpt-3.5-turbo](https://platform.openai.com/docs/guides/chat) model from OpenAI's API. You'll need to provide your OpenAI API key through the `OPENAI_API_KEY` environment variable. For example, you could call the tool using:

```OPENAI_API_KEY="your-key" gpt-translate args```

### Command-Line Tool

The `gpt-translate` command-line tool has the following options:

```
gpt-translate [-h] [-v] [--dry-run] [--source-language source_language] 
              [--target-language target_language] [-m model] [--ignore-comments]
              path
```

The `gpt-translate` command-line tool allows you to translate all corresponding `.tex` files from `source_language` to `target_language`. It also creates a backup of each file that is translated.


### arguments/options:
- `-h, --help`: show this help message and exit
- `-v, --verbose`: print verbose output
- `--dry-run`: do not translate, just print the files that would be translated and the number of tokens that would be sent to the API
- `--source-language source_language`: the name of the source language (default: English)
- `--target-language target_language`: the name of the target language (default: Spanish)
- `-m model`: indicates which OpenAI's model to use, from the set `{"gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k"}` (default: `"gpt-3.5-turbo-16k"`)
- `--ignore-comments`: leave commented lines untranslated
- `path`: the path of the directory or file to translate

The `--dry-run` option is especially helpful to estimate costs based on the number of tokens (see https://openai.com/pricing). Note that both input and output tokens count towards pricing.

## Problems and workarounds

- The translation might not work well with large blocks of LaTeX text where there is a majority of LaTeX symbols over natural language words. An example of this is big tables. One workaround is to comment out the entire block and use the `--ignore-comments` option to avoid it being translated.
- Occasionally, the translation might remove a closing command such as `\end{example}`. This could be due to the way the tool splits the file into chunks to comply with the token limit imposed by OpenAI's API. Inspecting the compilation output together with the original backup file should help solve the issue quickly.
