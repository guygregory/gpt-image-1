# Azure OpenAI Image Generation Demos

This repository contains Python samples demonstrating how to generate images using Azure OpenAI's DALL·E (gpt-image-1) API, both with a simple script and an interactive Gradio web app.

## Contents

- [`generate-aoai.py`](GPT-image-1/generate-aoai.py): Minimal script to generate an image from a prompt and save it to disk using Azure OpenAI.
- [`generate-gradio.py`](GPT-image-1/generate-gradio.py): Interactive Gradio web app for generating images with customizable parameters.

## Requirements

- Python 3.8+
- Azure OpenAI resource with image generation enabled
- `.env` file with required environment variables (see `.env.sample` for details)
- Install dependencies:
  ```sh
  pip install openai python-dotenv gradio pillow
