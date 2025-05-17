# Azure OpenAI Image Generation Demos

This repository contains Python samples demonstrating how to generate images using OpenAI's gpt-image-1 model, both with a simple script and an interactive Gradio web app.

## Contents

- [`generate-aoai.py`](generate-aoai.py): Minimal script to generate an image from a prompt and save it to disk using Azure OpenAI.
- [`generate-gradio.py`](generate-gradio.py): Interactive Gradio web app for generating images with customisable parameters. Compatible with Azure OpenAI, and OpenAI's API.

![437320676-8df46135-e429-4f11-9f1f-1a7d949be717](https://github.com/user-attachments/assets/1cec1413-d99d-476e-be47-e7beff6b4ff8)


## Requirements

- Python 3.8+
- Azure OpenAI resource with gpt-image-1 deployed (OpenAI is also supported for the Gradio app)
- `.env` file with required environment variables (see `.env.sample` for details)
- Install dependencies:
  ```sh
  pip install openai python-dotenv gradio pillow
  ```
## Known issues
- There's a bug when downloading the file in the Gradio app - it always downloads as a .webp, despite what output format the user requests
- C2PA Content Credentials don't work reliably right now

## Further reading
- [Microsoft Learn Documentation](https://learn.microsoft.com/en-gb/azure/ai-services/openai/how-to/dall-e?tabs=gpt-image-1)
- [Apply for access](http://aka.ms/oai/gptimage1access)
- [Model availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#image-generation-models)
- [Model card](https://ai.azure.com/explore/models/gpt-image-1/version/2025-04-15/registry/azure-openai)
- [Microsoft announcement blog](http://aka.ms/GPT-image-1)
