from openai import AzureOpenAI
import os
import base64
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_IMAGE_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_IMAGE_ENDPOINT"]
    )


result = client.images.generate(
    model=os.environ["AZURE_OPENAI_API_KEY"],
    prompt="Create a vintage F1 poster for the Silverstone Grand Prix on Sunday July 6th. It features a dynamic illustration of a speeding race car with dramatic motion lines and a vivid red, white and blue color scheme", # maximum length is 32000 characters
    # background="auto", # Optional. Must be one of transparent, opaque or auto (default value)
    # moderation="low", # Optional. Must be either low for less restrictive filtering or auto (default value)
    # output_compression=100, # Optional. Integer 0-100. Compression level for webp/jpeg. Defaults to 100.
    # output_format="png", # Optional. Must be one of png, jpeg, or webp. Defaults to png.
    # quality="auto", # Optional. Must be one of auto (default), high, medium, low.
     size="1024x1536", # Optional. Must be one of 1024x1024, 1536x1024, 1024x1536, or auto (default).
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("f1.png", "wb") as f:
    f.write(image_bytes)