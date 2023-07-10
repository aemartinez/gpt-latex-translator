import argparse
import os
import shutil
from typing import List
from gptlatextranslator.GPTTranslator import GPTTranslator, MODELS

def collect_tex_files(dir_path: str) -> List[str]:
    tex_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".tex") and not "macro" in file:
                tex_files.append(os.path.join(root, file))
    return tex_files

def backup_files(files: List[str]):
    for file in files:
        shutil.copy(file, file + ".bak")

def dry_run(tex_files: List[str], translator: GPTTranslator):
    print(f"Would translate {len(tex_files)} files:")
    total_tokens = 0
    for file in tex_files:
        with open(file, "r") as f:
            text_eng = f.read()
            tokens_number = translator.compute_translation_tokens(text_eng)
            print(f"  {file}: {tokens_number} tokens.")
            total_tokens += tokens_number
    print()
    print(f"Total number of tokens that would be sent to the API: {total_tokens}.")

def real_run(tex_files: List[str], translator: GPTTranslator):
    backup_files(tex_files)
    for file in tex_files:
        with open(file, "r") as f:
            text_eng = f.read()
            text_spa = translator.translate(text_eng)
        with open(file, "w") as f:
            f.write(text_spa)

def main():
    parser = argparse.ArgumentParser(description="""Translate .tex files using OpenAI's GPT-3 API.
                                                    Backups of the original files are created with the extension .bak.""")
    parser.add_argument("path", metavar="path", type=str, help="the path of the directory or file to translate")
    parser.add_argument("-v", "--verbose", action="store_true", help="print verbose output")
    parser.add_argument("--dry-run", 
                        action="store_true", 
                        help="do not translate, just print the files that would be translated and the number of tokens that would be sent to the API")
    parser.add_argument("--source-language", metavar="source_language", 
                        type=str, default="English", help="the name of the source language (default: English)")
    parser.add_argument("--target-language", metavar="target_language",
                        type=str, default="Spanish", help="the name of the target language (default: Spanish)")
    parser.add_argument("-m", "--model", metavar="model",
                        type=str, default="gpt-3.5-turbo-16k", help="the name of the OpenAI model to use for translation.",
                        choices=MODELS)
    parser.add_argument("--ignore-comments",
                        action="store_true",
                        help="do not translate Latex comments")
    args = parser.parse_args()

    # Check if the path exists
    if not os.path.exists(args.path):
        print(f"Path '{args.path}' does not exist.")
        return
    
    # Check if the path is a file or a directory
    if os.path.isfile(args.path):
        tex_files = [args.path]
    else:
        tex_files = collect_tex_files(args.path)
    
    if args.dry_run:
        translator = GPTTranslator(verbose=args.verbose,
                                   model_name=args.model,
                                   ignore_commented_blocks=args.ignore_comments)
        dry_run(tex_files, translator)
    else:
        # Check if the API key is set
        if not "OPENAI_API_KEY" in os.environ:
            print("The environment variable OPENAI_API_KEY is not set.")
            return
        
        openai_api_key = os.environ["OPENAI_API_KEY"]
        translator = GPTTranslator(openai_api_key=openai_api_key,
                                   verbose=args.verbose,
                                   ignore_commented_blocks=args.ignore_comments,
                                   model_name=args.model,
                                   lang_from=args.source_language, 
                                   lang_to=args.target_language)
        real_run(tex_files, translator)
