## Prerequisites

- Python 3.6 or higher
- An OpenAI API key
- `dotenv` package to manage environment variables

## Installation

1. Clone the repository to your local machine.

2. Install the required Python packages.
   ```bash
   pip install openai python-dotenv
   ```

3. Create a `.env` file in the root directory of the project and add your OpenAI API key.
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

## Usage

1. Place your lecture transcript text file in the `transcripts` directory. Ensure the file is a `.txt` file.

2. Adjust the script settings as needed:
   - `filename`: Name of your input transcript file.
   - `input_file_path`: Path to the input transcript file.
   - `output_file_path`: Path to save the summarized notes.
   - `max_words`: Maximum number of words per chunk to be processed.
   - `course`: The course name for which the lecture notes are being taken.

3. Run the script.
4. The summarized notes will be saved in the specified `output_file_path`.

## Script Breakdown

### Importing Required Libraries

```python
import openai
from dotenv import load_dotenv
import os
```

### Load API Key

```python
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```

### Read and Process Transcript

```python
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def split_text(text, max_words):
    length = len(text)
    print("preprocess text, character count: ", length)
    text = text.replace(", um,", "").replace(", uh,", "").replace(" um ", ",").replace("right?", ".").replace("Um", ",").replace("like, ","")
    print(f"text preprocessed, character count:{len(text)} , reduced by {100 - (len(text)/length) * 100} %")
    words = text.split()
    chunks = [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return chunks
```

### Summarize Chunks

```python
def get_summary(chunk, previous, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a student taking notes of the lecturer speaking."},
            {"role": "user", "content": f"""Continue from previous note, if any, put the following lecture transcript into detailed intuitive 
             and comprehensive lecture notes, do not miss things mentioned, 
             but when writing notes, be concise and simple in wording.
             Do not include introduction or conclusion, and do not include any form of summary at the end, just cleanly end the note taking, no need for extra words.
             This is a lecture on {course}.
             Remind you that the provided transcript may contain small error or typo.
             When writing notes, use sentences or expressions that were originally appeared in transcripts. 
             structure the note appropriately by section, header, indents etc for better readability. 
             The note should follow closely to the order of the lecturer's speech transcript content. As if "taking down notes as lecturer speaks". Do not go into things not mentioned in the transcription
             If applicable, helpful, or there is coding context mentioned in transcript, include code snippets if appropriate. 
             The transcript provided is a continue of previous note: ## previous note: ``` {previous}``` \n
             Your note is a continuation (Do not repeat content/things already said) from the end of previous note.  \n\n Transcript: {chunk}"""}
        ],
    )
    summary = response.choices[0].message['content'].strip()
    return summary
```

### Summarize Text File

```python
def summarize_text_file(file_path, max_words):
    text = read_text_file(file_path)
    chunks = split_text(text, max_words)
    summaries = []
    previous = ""

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i + 1}/{len(chunks)}")
        hint = f"> Summary start from '{chunk[:100]}' \n\n"
        summary = get_summary(chunk, previous)
        previous = summary
        summaries.append(hint + summary)
        print("Summary:", hint + summary)
    
    return summaries
```

### Save Summaries

```python
def save_summaries(summaries, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for i, summary in enumerate(summaries):
            file.write(f"> Summary of chunk {i + 1}:\n{summary}\n\n")
```

### Main Execution

```python
if __name__ == "__main__":
    filename = "My Recording Tutorial_otter_ai.txt"
    input_file_path = 'transcripts/' + filename
    output_file_path = 'notes/' + filename.removesuffix('.txt') + ' NOTES.md'
    max_words = 1200
    course = "Blockchain"
    summaries = summarize_text_file(input_file_path, max_words)
    save_summaries(summaries, output_file_path)
    
    print("Summarization complete. Summaries saved to", output_file_path)
```
