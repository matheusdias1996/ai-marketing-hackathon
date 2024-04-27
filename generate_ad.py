from openai import OpenAI
from PIL import Image
from IPython.display import Image, display
import base64

import prompts
import utils

# "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"
API_KEY = "sk-proj-6Q8ZvyjEGIvU5wFEoUXUT3BlbkFJhnTyD6745V0BgvKBG9BA"
client = OpenAI(api_key=API_KEY)


def generate_ad_description_and_post(image_url, demographic, original_post_text):
  response = client.chat.completions.create(
      model="gpt-4-turbo",
      temperature=0,
      messages=[
          {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": prompts.AD_DESCRIPTION_SYSTEM_PROMPT,
                }
            ]
          },
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "DEMOGRAPHIC:",
                  }
              ]
          },
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": demographic,
                  }
              ]
          },
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "ORIGINAL POST TEXT:",
                  }
              ]
          },
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": original_post_text,
                  }
              ]
          },
          {
              "role": "user",
              "content": [
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": f"data:image/jpeg;base64,{image_url}",
                      },
                  },
              ],
          }
      ],
  )
  output = response.choices[0].message.content
  parsed_output = utils.parse_descriptions_and_posts(output)
  # ad_description, post_text = output.split(
  #     "POST TEXT:")[0], output.split("POST TEXT:")[1]
  # return ad_description, post_text
  return parsed_output


def generate_ad_image(ad_description):
  response = client.images.generate(
      model="dall-e-3",
      prompt=ad_description,
      size="1024x1024",
      quality="hd",
      n=1,
  )
  return response.data[0].url


def encode_image(image_path, demographic=prompts.TEST_DEMOGRAPHIC):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def main(image_path="meat_picture_original.jpeg", demographic=prompts.TEST_DEMOGRAPHIC, original_post_text=prompts.ORIGINAL_POST_TEXT):
  # TODO: Get image from shared drive and prepare it for OAI API
  image_url = encode_image(image_path)
  # TODO: Input image and text to generate description of ad, caption and hashtags
  ad_description_and_post = generate_ad_description_and_post(
      image_url, demographic, original_post_text)

  for i in range(1, 6):
    description_key = f"DESCRIPTION {i}"
    post_text_key = f"POST TEXT {i}"

    # Retrieve the ad description and post text
    ad_description = ad_description_and_post[description_key]
    post_text = ad_description_and_post[post_text_key]

    # Generate an image from the ad description
    new_image_url = generate_ad_image(ad_description)

    # Save the generated image to a unique file name
    # Ensures the file name is image_001, image_002, etc.
    image_filename = f"image_{i:03}.png"
    utils.save_image_from_url(new_image_url, image_filename)

    # Print the indexed post text
    print(f"{i}: {post_text}")


if __name__ == "__main__":
  main()
