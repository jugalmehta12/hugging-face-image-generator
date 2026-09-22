from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="auto"
)

# Get prompt from user
prompt = input("Enter your image prompt: ")

# Check if prompt is empty
if not prompt.strip():
    print("Error: Prompt cannot be empty.")
    exit()

print("\nGenerating image...")

image = client.text_to_image(
    prompt,
    model="black-forest-labs/FLUX.1-schnell"
)

image.save("generated_image.png")

print("Image generated successfully!")
print("Saved as: generated_image.png")