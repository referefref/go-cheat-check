from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that generates Go code based on the user's request. Your responses should include only the Go code, without any explanations, markdown formatting, comments, or additional content. The code must be ready to use directly as an example file, with inline documentation where requested."
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_go_code(prompt, num_files, output_dir):
    """Generate Go code files from a given prompt using OpenAI API."""
    os.makedirs(output_dir, exist_ok=True)

    for i in range(num_files):
        code = chat_gpt(prompt)
        file_name = os.path.join(output_dir, f'generated_code_{i + 1}.go')
        with open(file_name, 'w') as f:
            f.write(code)

        print(f"Generated file: {file_name}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate Go code files from a query.')
    parser.add_argument('query', type=str, help='The query to generate Go code')
    parser.add_argument('num_files', type=int, help='Number of Go files to generate')
    parser.add_argument('output_dir', type=str, help='Directory to save the generated Go files')

    args = parser.parse_args()

    generate_go_code(args.query, args.num_files, args.output_dir)

if __name__ == '__main__':
    main()
