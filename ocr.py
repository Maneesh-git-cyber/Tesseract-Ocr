#you can run this code only in Google Collab if you want in your Editor make proper changes

import pytesseract
from PIL import Image
from google.colab import files

# 1. Prompt you to upload your HW1 image file
print("Please upload your HW1 image:")
uploaded = files.upload()

# Get the exact filename of the image you just uploaded
image_path = list(uploaded.keys())[0]

try:
    # 2. Open the image and run OCR
    img = Image.open(image_path)
    print(f"\nExtracting text from {image_path}...")
    extracted_text = pytesseract.image_to_string(img)
    
    # 3. Print the result
    print("\n--- Extracted Soft Copy ---")
    print(extracted_text)
    
    # Save it to a text file that you can download from the Colab files pane
    with open('HW1_softcopy.txt', 'w') as f:
        f.write(extracted_text)
        print("\n(Text successfully saved to HW1_softcopy.txt. You can download it from the folder icon on the left.)")

except Exception as e:
    print(f"An error occurred: {e}")
