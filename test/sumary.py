import os
from openai import OpenAI

client = OpenAI(api_key='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')

# Set your OpenAI API key

def summarize_text_with_assistant(text):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes Engineering text into concise markdown format. The details are important, so make sure you don't skip on the critical sections required to understand the content."},
        {"role": "user", "content": text}
    ])
    return response.choices[0].message.content

def process_files_in_directory():
    # Get all .txt files in the current directory
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename, 'r') as file:
                content = file.read()

            # Summarize the content
            summary = summarize_text_with_assistant(content)

            # Create the .md filename
            md_filename = filename.replace('.txt', '.md')

            # Save the summary to the .md file
            with open(md_filename, 'w') as md_file:
                md_file.write(summary)
            print(f"Summary saved to {md_filename}")

if __name__ == "__main__":
    process_files_in_directory()
