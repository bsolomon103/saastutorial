from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet, generate_keywords
MAX_INPUT_LENGTH = 32

app = FastAPI()


@app.get('/generate_snippet')
async def generate_snippet_api(subject:str):
    snippet = generate_branding_snippet(subject)
    return {f"snippet: {snippet}, keywords: []"}

@app.get('/generate_keyword')
async def generate_keyword_api(subject:str):
    keywords = generate_keywords(subject)
    return {f"snippet: None, keywords: {keywords}"}

@app.get('/generate_response')
async def generate_keyword_api(subject:str):
    if validate_input_length(subject):
        keywords = generate_keywords(subject)
        snippet = generate_branding_snippet(subject)
        return {f"snippet : {snippet}, keywords: {keywords}"}

def validate_input_length(input: str):
    if len(input) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.")
   