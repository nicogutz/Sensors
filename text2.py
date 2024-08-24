import os
import pdfplumber

# Directory containing the PDF files
directory = './'

# Iterate through all files in the directory
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    # Process only PDF files
    if filename.endswith('.pdf'):
        # Initialize a variable to store the extracted text
        all_text = ''
        
        # Full path to the PDF file
        pdf_path = os.path.join(directory, filename)
        
        # Open the PDF file using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            
            # Loop through each page in the PDF and extract the text
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                
                # Add the extracted text to 'all_text' and separate each page's text with a newline
                if single_page_text:  # Only append if the page contains text
                    all_text += '\n' + single_page_text
        
        # Replace '.pdf' with '.txt' for the output file name
        output_filename = filename.replace('.pdf', '.txt')
        
        # Full path for the output text file
        output_path = os.path.join(directory, output_filename)
        
        # Save the extracted text to the new text file
        with open(output_path, 'w', encoding='utf-8') as text_file:
            text_file.write(all_text)
        
        print(f'Text successfully extracted and saved to {output_filename}')
