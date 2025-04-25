from openai import AzureOpenAI
import os
import base64
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_IMAGE_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_IMAGE_ENDPOINT"]
    )

output_format = "png" # Optional. Must be one of png, jpeg, or webp. Defaults to png.

result = client.images.generate(
    model=os.environ["AZURE_OPENAI_API_IMAGE_MODEL"],
    prompt="Hyper realistic photo from the point of view of a Formula 1 driver, taken during the 2024 season. The circuit is Spa-Francorchames, Belgium. The car is at the bottom of the hill at the iconic Eau Rouge section of the circuit. Photo quality is consistent with a modern onboard camera", # maximum length is 32000 characters
    output_format=output_format, # Optional. Must be one of png, jpeg, or webp. Defaults to png.
    # background="auto", # Optional. Must be one of transparent, opaque or auto (default value)
    # moderation="low", # Optional. Must be either low for less restrictive filtering or auto (default value)
    # output_compression=100, # Optional. Integer 0-100. Compression level for webp/jpeg. Defaults to 100.
    # quality="high", # Optional. Must be one of auto (default), high, medium, low.
    size="1024x1535", # Optional. Must be one of 1024x1024, 1536x1024, 1024x1536, or auto (default).
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open(f"file.{output_format}", "wb") as f:
    f.write(image_bytes)