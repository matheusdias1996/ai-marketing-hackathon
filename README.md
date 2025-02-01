# A/B Testing of Generative AI Social Media Marketing Materials

This is an end-to-end application for the A/B testing of social media marketing materials (images and captions) that are automatically generated, based on a reference image and caption, by using GPT-4 and DALL-E and displayed them to the user on a Streamlit interface.

### Background:
Today, only 1% of posts become viral. Most businesses make a post with 1 associated image and text.
However, Meta and other ads providers have the option to allow posting more media at a time, eg. 5+ images with 5+ prompts. With our tool, you can, based on 1 image and 1 text, generate 5 images and texts and input all of them into Meta advertisement, guaranteeing you increase your likelihood of having a higher reach. The tool can also handle multiple languages.
We tested this on the Meta ads platform and found that in our posts, the AI-generated images and texts were selected in 50% of the cases, so 50% of the posts will have a higher reach. Comparing to the baseline of 1 image + text, we found that our tool increases the overall engagement with your material by 30%.

### Example:

---> Model Input

ORIGINAL TEXT

Adoramos esse coração de alcatra Maturatta da Friboi.
Carne muito macia, saborosa e com a gordura na medida certa.
Ideal para fazer na chapa ou numa frigideira bem quente.
De acompanhamento batatinhas pequenas, ao azeite e molho chimichurri.
O preço é 59,90 / kg

ORIGINAL IMAGE
![alt text](https://github.com/matheusdias1996/ai-marketing-hackathon/blob/main/Original.jpeg "Logo Title Text 1")



---> Model Output

Example 1

Descubra o sabor irresistível do coração de alcatra Maturatta da Friboi, agora em destaque no nosso supermercado. Uma carne excepcionalmente macia e suculenta, perfeita para grelhar e servir com nossas batatinhas douradas ao azeite e molho chimichurri. Venha aproveitar o preço especial de R$59,90/kg e experimente o melhor da nossa seleção local e produtos árabes. #CarnesDeQualidade #CompreLocal #SupermercadoVitória
![plot](https://drive.google.com/file/d/1HIJViV4wLzzgvJAqc5aqDzeYTZxTbFgc/view?usp=sharing)


Example 2

Descubra a elegância e o sabor do coração de alcatra Maturatta da Friboi em nosso supermercado. 🌹🥩 Servido com batatinhas ao azeite e chimichurri, por apenas R$59,90/kg. Venha experimentar a diferença de comprar produtos frescos e de qualidade, apoiando a comunidade local. Sua cozinha merece o melhor! #AltaGastronomia #ComprasConscientes
![plot](https://drive.google.com/file/d/1sLt8SB5vWraOm1l9Ia0ZJMDyv1rhVYZT/view?usp=sharing)


Example 3

Venha saborear o melhor da carne com nosso coração de alcatra Maturatta da Friboi! 🌟 Maciez incomparável e sabor que agrada a todos, servido com batatinhas ao azeite e um toque especial de molho chimichurri. Por apenas R$59,90/kg, transforme qualquer refeição em uma ocasião especial. Visite-nos e confira nossa variedade de produtos frescos e locais! #SaboresDaTerra #AlimentaçãoSaudável
![plot](https://drive.google.com/file/d/15hVcs3WdrK_IgzIK2EwfeeD7QK3u6hev/view?usp=sharing)


Example 4

Experimente o excepcional coração de alcatra Maturatta da Friboi, uma escolha perfeita para os amantes de carne! 🍖💖 Acompanhado de batatinhas assadas ao azeite e chimichurri, por apenas R$59,90/kg. Nosso compromisso é oferecer produtos frescos e de alta qualidade, valorizando os produtores locais. Faça-nos uma visita e deixe-nos fazer parte do seu dia a dia! #ComidaDeVerdade #ApoioLocal
![plot](https://drive.google.com/file/d/1ezzLHN2z640DTY0i2r9T67q80Q0arN3p/view?usp=sharing)


Example 5

Não perca a chance de provar nosso delicioso coração de alcatra Maturatta da Friboi, perfeito para o seu próximo churrasco! 🍴🔥 Acompanha batatinhas ao azeite e chimichurri, tudo por R$59,90/kg. Visite nosso supermercado, onde qualidade e frescor são sempre garantidos, e aproveite nossos produtos locais e importados. #ChurrascoPerfeito #ProdutosFrescos
![plot](https://drive.google.com/file/d/1_wmBz6qnrDn-tLQGo81ZWF0xSYpi-Mdq/view?usp=sharing)
