# chatgpt-script
Script to communicate chatgpt with openai pip library

Can be used to make sure generated text is in JSON format

## Note
- get_json_response() parses the response from chatgpt and returns a JSON object
- If the response is not in JSON format, it will perform a recursive call to get_json_response() until it is in JSON format
    - The generated text will be logged to generated_response.json file
- Also if the response is in JSON format, it will return the JSON object

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```
