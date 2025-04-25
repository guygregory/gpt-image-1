import io
import base64
import os
from dotenv import load_dotenv
from openai import OpenAI, AzureOpenAI
from PIL import Image
import gradio as gr

# Load environment variables from .env file
load_dotenv()

# Set the AI host to Azure, OpenAI, or GitHub Models (coming soon)
AIhost = "AzureOpenAI" # set to "AzureOpenAI" or "OpenAI", based on your requirement

def get_client(host: str):
    """
    Returns the deployment and client based on the specified host.
    Exits the application if an unsupported host is provided.
    """
    if host == "AzureOpenAI":
        deployment = os.environ["AZURE_OPENAI_API_IMAGE_MODEL"]
        client = AzureOpenAI(
            api_key=os.environ["AZURE_OPENAI_API_IMAGE_KEY"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            azure_endpoint=os.environ["AZURE_OPENAI_API_IMAGE_ENDPOINT"]
        )
    elif host == "OpenAI":
        deployment = "gpt-image-1"  # Default deployment for OpenAI
        client = OpenAI()
    else:
        print("Invalid AI host specified. Please set AIhost to 'AzureOpenAI' or 'OpenAI' and provide the configuration in the .env file")
        exit(0)
    return deployment, client

# Set the AI host to Azure or OpenAI, 
deployment, client = get_client(AIhost)


def generate_image(
    prompt: str,
    background: str,
    moderation: str,
    output_compression: int,
    output_format: str,
    quality: str,
    size: str
):
    # Call the images.generate endpoint
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        background=background,                 # transparent, opaque, or auto
        moderation=moderation,                 # low or auto
        output_compression=output_compression, # 0–100
        output_format=output_format,           # png, jpeg, or webp
        quality=quality,                       # auto, high, medium, low
        size=size                              # 1024x1024, 1536x1024, 1024x1536, or auto
    )
    # Decode and return a PIL image
    image_bytes = base64.b64decode(result.data[0].b64_json)
    return Image.open(io.BytesIO(image_bytes))


# Build the Gradio interface
with gr.Blocks(title="OpenAI Image Generator") as demo:
    with gr.Row():
        # Left: generated image only
        with gr.Column():
            img_output = gr.Image(label="Generated Image", type="pil")

        # Right: prompt ➜ submit ➜ parameters
        with gr.Column():
            gr.Markdown("## Prompt")  # Add this line for styled label
            prompt_input = gr.Textbox(
                label="",  # Hide default label
                placeholder="Enter your image prompt here…",
                lines=2,
                max_length=32000,         # Set max length to 32000
                container=False
            )
            submit_btn = gr.Button("Submit")

            gr.Markdown("## Parameters")
            background_input = gr.Radio(
                choices=["transparent", "opaque", "auto"],
                value="auto",
                label="Background"
            )
            moderation_input = gr.Radio(
                choices=["low", "auto"],
                value="auto",
                label="Moderation"
            )
            output_compression_input = gr.Slider(
                minimum=0, maximum=100, step=1,
                value=100,
                label="Output Compression (for jpeg/webp only)",
                interactive=False  # Disabled by default since png is selected
            )
            output_format_input = gr.Radio(
                choices=["png", "jpeg", "webp"],
                value="png",
                label="Output Format"
            )
            quality_input = gr.Radio(
                choices=["auto", "high", "medium", "low"],
                value="auto",
                label="Quality"
            )
            size_input = gr.Dropdown(
                choices=["1024x1024", "1536x1024", "1024x1536", "auto"],
                value="auto",
                label="Size"
            )

    # Wire up the button
    submit_btn.click(
        fn=generate_image,
        inputs=[
            prompt_input,
            background_input,
            moderation_input,
            output_compression_input,
            output_format_input,
            quality_input,
            size_input
        ],
        outputs=img_output
    )

    # If the user selects jpeg or webp, enable the output compression slider
    def update_output_compression_interactive(output_format):
        if output_format in ["jpeg", "webp"]:
            return gr.update(interactive=True)
        else:
            return gr.update(interactive=False)

    output_format_input.change(
        fn=update_output_compression_interactive,
        inputs=output_format_input,
        outputs=output_compression_input
    )

if __name__ == "__main__":
    demo.launch()
