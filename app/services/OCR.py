import os
from dotenv import load_dotenv
import requests

class OCR:
    def __init__(self, env_path: str = None):
        """
        Initialize the OCR client.
        :param env_path: Optional path to .env file; if None, defaults to project root.
        """
        # Load environment variables from .env
        load_dotenv(dotenv_path=env_path)

        # Retrieve API configuration
        self.api_url = os.getenv("API_URL")
        self.api_key = os.getenv("API_KEY")
        if not self.api_url or not self.api_key:
            raise ValueError("API_URL and API_KEY must be set in environment variables.")

    def ocr_image(self, image_path: str, language: str = "eng", overlay: bool = False) -> str:
        """
        Send an image to the OCR.space API and return the recognized text.
        :param image_path: Path to the image or PDF file.
        :param language: Language code for OCR (e.g., 'eng', 'fra').
        :param overlay: Whether to include position data for each word.
        :return: The text parsed from the image.
        """
        payload = {
            'apikey': self.api_key,
            'language': language,
            'isOverlayRequired': overlay
        }

        with open(image_path, 'rb') as image_file:
            response = requests.post(
                self.api_url,
                files={'file': image_file},
                data=payload
            )
            response.raise_for_status()  # Raise an error for bad HTTP status codes

        result = response.json()
        parsed_results = result.get('ParsedResults')
        if not parsed_results or not parsed_results[0].get('ParsedText'):
            raise RuntimeError("No text parsed from the OCR response.")

        return parsed_results[0]['ParsedText']


if __name__ == "__main__":
    # Example usage
    client = OCR()
    text = client.ocr_image(
        r"D:\carrier\stage\stage-global-averroes\ai-web-app-ch\backend\app\services\ORC_Text.png"
    )
    print(text)
