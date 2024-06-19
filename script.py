
import openai

# import key from .env
from dotenv import load_dotenv
load_dotenv()
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def split_text(text, max_words):
    # preprocess, remove all ", um,", ", Um," and ", uh," in the text
    text = text.replace(", um,", " ").replace(", uh,", " ").replace(" um ", " ").replace("right?", ".").replace("Um", "").replace("like, ","")
    words = text.split()
    chunks = [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return chunks

def get_summary(chunk, previous, model="gpt-4o"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a student taking notes of the lecturer speaking."},
            {"role": "user", "content": f"""Continue from your previous response or note, if any, put the following lecture transcript into detailed intuitive 
             and comprehensive lecture notes, do not miss things mentioned, 
             but when writing notes, be concise and simple in wording.
             Do not include introduction or conclusion, and do not include a summary or finalword section at the end.
             This is a lecture on {course}.
             Remind you that the provided transcript may contain small error or typo due to the nature of the lecture recording and transcription.
             When writing notes, use or reference sentences or expressions that was appeared in transcripts originally. 
             structure the note appropriately by section, header, indents etc for better readability. 
             If applicable, helpful, or there is coding context mentioned in transcript, include code snippets if appropriate. Your note should continue (but not repeat) from the end of previous note: {previous} \n\n Transcript: {chunk}"""}
        ],
        #max_tokens=150  # Adjust this value based on how detailed you want the summary
    )
    summary = response.choices[0].message['content'].strip()
    return summary

def summarize_text_file(file_path, max_words):
    text = read_text_file(file_path)
    chunks = split_text(text, max_words)
    summaries = []
    previous = ""

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i + 1}/{len(chunks)}")
        # summary start with...
        # add a summary start with the first 100 char of the chunk
        hint = f"Summary start from '{chunk[:100]}' \n"
        # get summary and pass the last 100 char of the previous
        print("previous: "+ previous + "\n")
        summary = get_summary(chunk, previous)
        previous = summary[-500:]
        summaries.append(hint + summary)
        print("Summary:", hint + summary)
    
    return summaries

def save_summaries(summaries, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for i, summary in enumerate(summaries):
            file.write(f"Summary of chunk {i + 1}:\n{summary}\n\n")

if __name__ == "__main__":
    input_file_path = 'COMP3141 Lecture 1UG-transcript 4.txt'  # Replace with your input file path
    output_file_path = input_file_path.removesuffix('.txt') + ' NOTES.md'  # Replace with your desired output file path
    max_words = 1700  # Adjust the number of words per chunk
    course = "Haskell Programming"
    summaries = summarize_text_file(input_file_path, max_words)
    save_summaries(summaries, output_file_path)
    
    print("Summarization complete. Summaries saved to", output_file_path)
