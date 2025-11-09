import os
import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

#select device
device = "mps" if torch.backends.mps.is_available() else "cpu"
pipe = pipe.to(device)

#prompt
prompt = input("Enter a text prompt for the image: ")

with torch.autocast("cpu" if device == "cpu" else "mps"):
    image = pipe(prompt).images[0]

# save file
base_name = "generated_image_"
extension = ".png"
i = 1
while os.path.exists(f"{base_name}{i}{extension}"):
    i += 1

output_path = f"{base_name}{i}{extension}"
image.save(output_path)
print(f"Image saved as {output_path}")
