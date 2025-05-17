from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import requests
from bs4 import BeautifulSoup
import PyPDF2
import io

def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return ' '.join(str(sentence) for sentence in summary)

def get_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return ' '.join([para.get_text() for para in paragraphs])
    except Exception as e:
        return f"Error fetching content from URL: {e}"

def get_text_from_pdf_url(pdf_url):
    try:
        response = requests.get(pdf_url)
        pdf_file = io.BytesIO(response.content)
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

if __name__ == "__main__":
    while True:
        print("\nChoose an input option:")
        print("1. Enter custom text")
        print("2. Enter article URL")
        print("3. Enter research paper (PDF) URL")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == "1":
            print("\nEnter the text to summarize (press ENTER twice to end):")
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            input_text = '\n'.join(lines)

        elif choice == "2":
            url = input("Enter the article URL: ").strip()
            input_text = get_text_from_url(url)

        elif choice == "3":
            pdf_url = input("Enter the PDF URL: ").strip()
            input_text = get_text_from_pdf_url(pdf_url)

        elif choice == "4":
            print("Exiting summarizer. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
            continue

        print("\nSummarized Output:\n")
        print(summarize_text(input_text, 3))
