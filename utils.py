import io
import re
import requests
from PIL import Image


def parse_descriptions_and_posts(input_text):
    # This regex pattern looks for 'DESCRIPTION' followed by a number (and possibly spaces),
    # capturing all text until it encounters the next 'DESCRIPTION' or 'POST TEXT', or end of the text.
    # It does this by using non-greedy matching and lookahead assertions.
    pattern = r"DESCRIPTION (\d+):\n(.*?)(?=\nDESCRIPTION |\nPOST TEXT \d+|$)"

    # Similarly, this pattern matches 'POST TEXT' that might be followed directly by a number.
    post_text_pattern = r"POST TEXT (\d+):\n(.*?)(?=\nDESCRIPTION |\nPOST TEXT \d+|$)"

    # Finding all matches for descriptions
    descriptions = {f"DESCRIPTION {match.group(1)}": match.group(2).strip()
                    for match in re.finditer(pattern, input_text, re.DOTALL)}

    # Finding all matches for post texts
    post_texts = {f"POST TEXT {match.group(1)}": match.group(2).strip()
                  for match in re.finditer(post_text_pattern, input_text, re.DOTALL)}

    # Combining both dictionaries into one
    descriptions.update(post_texts)

    return descriptions


def save_image_from_url(url, save_path):
    """Save an image from a URL to a specified path using PIL."""
    try:
        # Fetch the image from the URL
        response = requests.get(url)
        # This will raise an exception if the request returned an error status
        response.raise_for_status()

        # Open the image from bytes, convert it to an image file object with PIL
        image = Image.open(io.BytesIO(response.content))

        # Save the image to the specified path
        image.save(save_path)
        print(f"Image successfully saved to {save_path}")
    except requests.RequestException as e:
        print(f"Failed to retrieve the image from URL: {e}")
    except IOError as e:
        print(f"Error saving the image: {e}")
