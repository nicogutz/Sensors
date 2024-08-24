import os
from openai import OpenAI

client = OpenAI(api_key='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')

# Set your OpenAI API key

def summarize_text_with_assistant(text):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Your job is to make multiple choice questions of everything in markdown format from the following engineering course transcript. You have to make sure to be very detailed and write every possible question that you can. Be detailed and write as many as possible. The questions should have 4 possible answers, and at the end, inside a spoiler, the correct answer. Make sure you use only things that are part of the text and nothing else. Remember to do so in markdown."},
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
            md_filename = filename.replace('.txt', '_questions.md')

            # Save the summary to the .md file
            with open(md_filename, 'w') as md_file:
                md_file.write(summary)
            print(f"Summary saved to {md_filename}")
        return

if __name__ == "__main__":
    process_files_in_directory()
