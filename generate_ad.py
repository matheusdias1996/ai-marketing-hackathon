from openai import OpenAI
from PIL import Image
from IPython.display import Image, display
import base64

import prompts
import utils

TEST_DEMOGRAPHIC = """
The advertisement targets consumers of a supermarket in Vitória, Espírito Santo, Brazil. The supermarket targets people who value convenience and fresh products in general, but also just people who are looking to make grocery purchases. The supermarket is also famous for being related to local products and supporting the community. It also has a good assortment of Arabic products given owners are Lebanese descendants
"""

ORIGINAL_POST_TEXT = """
Adoramos esse coração de alcatra Maturatta da Friboi.
Carne muito macia, saborosa e com a gordura na medida certa.
Ideal para fazer na chapa ou numa frigideira bem quente.
De acompanhamento batatinhas pequenas, ao azeite e molho chimichurri.
O preço é 59,90 / kg
"""

API_KEY = "sk-proj-7GDtrJLW3lqORNvILNguT3BlbkFJjcFGj5kO98gxIQKWqjxU"
client = OpenAI(api_key=API_KEY)


def generate_ad_description(image_url, demographic, original_post_text):
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
  print(output)
  parsed_output = utils.parse_descriptions_and_posts(output)
  print(parsed_output)
  # ad_description, post_text = output.split(
  #     "POST TEXT:")[0], output.split("POST TEXT:")[1]
  # return ad_description, post_text
  return parsed_output['DESCRIPTION 1'], parsed_output['POST TEXT 1']


def generate_ad_image(ad_description):
  response = client.images.generate(
      model="dall-e-3",
      prompt=ad_description,
      size="1024x1024",
      quality="hd",
      n=1,
  )
  return response.data[0].url


def encode_image(image_path, demographic=TEST_DEMOGRAPHIC):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def main(image_path="meat_picture_original.jpeg", demographic=TEST_DEMOGRAPHIC, original_post_text=ORIGINAL_POST_TEXT):
  # TODO: Get image from shared drive and prepare it for OAI API
  image_url = encode_image(image_path)
  # TODO: Input image and text to generate description of ad, caption and hashtags
  ad_description, post_text = generate_ad_description(
      image_url, demographic, original_post_text)
  # TODO: Generate an image from description
  new_image_url = generate_ad_image(ad_description)
  # TODO: Upload into shared drive
  utils.save_image_from_url(new_image_url, "test.png")
  print(post_text)


if __name__ == "__main__":
  main()
