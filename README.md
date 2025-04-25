# Azure OpenAI Image Generation Demos

This repository contains Python samples demonstrating how to generate images using Azure OpenAI's gpt-image-1 model, both with a simple script and an interactive Gradio web app.

## Contents

- [`generate-aoai.py`](GPT-image-1/generate-aoai.py): Minimal script to generate an image from a prompt and save it to disk using Azure OpenAI.
- [`generate-gradio.py`](GPT-image-1/generate-gradio.py): Interactive Gradio web app for generating images with customisable parameters.

![image](https://github.com/user-attachments/assets/8df46135-e429-4f11-9f1f-1a7d949be717)

## Requirements

- Python 3.8+
- Azure OpenAI resource with image generation enabled (OpenAI is also supported for the Gradio app)
- `.env` file with required environment variables (see `.env.sample` for details)
- Install dependencies:
  ```sh
  pip install openai python-dotenv gradio pillow

## Known issues
- There's a bug when downloading the file in the Gradio app - it always downloads as a .webp, despite what output format the user requests
- C2PA Content Credentials don't work reliably right now
