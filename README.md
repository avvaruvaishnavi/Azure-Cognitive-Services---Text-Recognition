# Azure-Cognitive-Services-Handwritten-Text-Recognition

## Description

This Python script uses the **Azure Cognitive Services Computer Vision API** to recognize text from an image. It sends a request to the API, checks the status of the operation, and once complete, retrieves the recognized text.

## Setup Instructions

1. **Install Dependencies**:
   Install the required Python libraries by running:
   ```bash
   pip install azure-cognitiveservices-vision-computervision msrest
   ```

2. **Create `cred.py` File**:
   In your project directory, create a file called `cred.py` and store your Azure **API key** and **Endpoint URL** there.
   ```python
   # cred.py
   url = "your-azure-endpoint-url"
   key = "your-azure-api-key"
   ```

3. **Modify the Image URL**:
   Change the `img` variable in the script to the URL of the image you want to analyze.
   ```python
   img = "https://example.com/your-image-url.jpg"  # Replace with your image URL
   ```

4. **Run the Script**:
   After setting up `cred.py` and modifying the image URL, run the Python script:
   ```bash
   python main.py
   ```

## Notes

- The script extracts the text from the image by using the Azure Computer Vision Read API.
-  The script checks the operation status periodically and prints the recognized text once the operation is completed.
