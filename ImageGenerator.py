import openai
import requests
from PIL import Image
from io import BytesIO

openai.api_key = "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"

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def download_image(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # Save the image as a JPG file
    image_name = "image" + str(i) + ".jpg"
    img.save(image_name, "JPEG")
i=0
while True:
    prompt = input("Enter the deatils of the image: ")
    print()
    print("Generating image...")
    download_image(generate_image(prompt))
    print("---------------------------------")
    print("Image generated")
    print("---------------------------------")
    i += 1

