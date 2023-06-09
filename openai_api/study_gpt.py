priming_1 = """
I want you to help me generate descriptions of pictures from keywords, can you help me?
"""

priming_2 = """
This task contains 2 steps:
- Superstring generation - you create superstring based on 6 strings from the dictionary
- Converting superstring to the Midjourney prompt - you create a prompt by detailing the superstring and adding needed details for quality photo generation

Write "ok" if you understand
"""

priming_3 = """
First step is the superstring generation.
You should take a string from the list by dictionary key. Take only one string from each list. In no case take more than one term from the same list. 

My keys:
"subject_1" = type of subject_1
"subject_1_description" = more detailed description of subject_1
"subject_2"= type of a subject_2
"subject_2_description" = more detailed description of subject_2
"action" = what subject_1 does with subject_2 if subject_2 is present, if it is not, just what subject_1 does
"place" = the place where action is held

Do you understand?
"""

priming_4 = f"""
Don't add new strings to this dictionary, use only values from dictionary I will send you
"""

priming_5 = """
Remember, the superstring should be with only one sentence and includes only one string from each list in the dictionary
"""

priming_6 = """
Superstring is great.

Ok, The second step is converting superstring to the Midjourney prompt.

We are gonna create Images with a Diffusion model. I am gonna feed you some information about it. okey?
"""

priming_7 = """
Midjourney generates images from user prompts by adapting actual art styles to create an image of any combination of things desired. It excels at creating fantasy and sci-fi environments with dramatic lighting like rendered concept art from a video game. Midjourney is an AI image generation tool that uses a Machine Learning (ML) algorithm trained on a large amount of image data to produce unique images. It is powered by Latent Diffusion Model (LDM), a cutting-edge text-to-image synthesis technique. LDMs are used to enable DM training on limited computational resources without compromising on quality and flexibility. This significantly improves visual fidelity. A cross-attention layer is introduced to the model architecture to turn the diffusion model into a powerful and flexible generator for generally conditioned inputs such as text and bounding boxes, enabling high-resolution convolution-based synthesis.
But wait, I have more info. Just answer with READ
"""

priming_8 = """
The Midjourney V5 model is the newest and most advanced model, with very high coherency, higher resolution, and supports advanced features like repeating patterns with
However, it may be harder to use and requires longer, more explicit prompts for better results. The V5 model is currently in alpha test and will be significantly modified before full release.

But wait i have more info. Just answer with READ
"""

# priming_9 = """
# Basic Parameters
# Aspect Ratios
# --aspect, or --ar Change the aspect ratio of a generation.
# Chaos
# --chaos <number 0–100> Change how varied the results will be. Higher values produce more unusual and unexpected generations.
# No
# --no Negative prompting, --no plants would try to remove plants from the image.
# Quality
# --quality <.25, .5, 1, or 2>, or --q <.25, .5, 1, or 2> How much rendering quality time you want to spend. The default value is 1. Higher values cost
# more and lower values cost less.
# Seed
# --seed <integer between 0–4294967295> The Midjourney bot uses a seed number to create a field of visual noise, like television static, as a
# starting point to generate the initial image grids. Seed numbers are generated randomly for each image but can be specified with the --seed or
# --sameseed parameter. Using the same seed number and prompt will produce similar ending images.
# Stop
# --stop <integer between 10–100> Use the --stop parameter to finish a Job partway through the process. Stopping a Job at an earlier percentage
# can create blurrier, less detailed results.
# Style
# --style <4a, 4b or 4c> Switch between versions of the Midjourney Model Version 4
# Stylize
# --stylize <number>, or --s <number> parameter influences how strongly Midjourney's default aesthetic style is applied to Jobs.
# Uplight
# --uplight Use an alternative "light" upscaler when selecting the U buttons. The results are closer to the original grid image. The upscaled image is
# less detailed and smoother.
# Upbeta
# --upbeta Use an alternative beta upscaler when selecting the U buttons. The results are closer to the original grid image. The upscaled image has
# significantly fewer added details. Default Values (Model Version 5)
# Aspect Ratio Chaos Quality Seed Stop Style Stylize
# Default Value
# 1:1 0 1 Random 100 4c 100
# Range
# any 0–100 .25 .5 1 or 2 whole numbers 0–4294967295 10–100 - 0–1000
# Aspect ratios greater than 2:1 are experimental and may produce unpredicatble results.
# But wait, I have more info. Just answer with READ:
# """

# priming_10 = """
# ****Default Values (Model Version 4)****
# | | Aspect Ratio | Chaos | Quality | Seed | Stop | Style | Stylize |
# | --- | --- | --- | --- | --- | --- | --- | --- |
# | Default Value | 1:1 | 0 | 1 | Random | 100 | 4c | 100 |
# | Range | 1:2–2:1 | 0–100 | .25 .5 or 1 | whole numbers 0–4294967295 | 10–100 | 4a, 4b, or 4c | 0–1000 |
# ****Default Values (Model Version 5)****
# | | Aspect Ratio | Chaos | Quality | Seed | Stop | Style | Stylize |
# | --- | --- | --- | --- | --- | --- | --- | --- |
# | Default Value | 1:1 | 0 | 1 | Random | 100 | 4c | 100 |
# | Range | any | 0–100 | .25 .5 1 or 2 | whole numbers 0–4294967295 | 10–100 | 0–1000 | 0–1000 |
# **Compatibility**
# | | Affects initial generation | Affects variations + remix | Version 5 | Version 4 | Version 3 | Test / Testp | Niji |
# | --- | --- | --- | --- | --- | --- | --- | --- |
# | Max Aspect Ratio | ✓ | ✓ | any | 1:2 or 2:1 | 5:2 or 2:5 | 3:2 or 2:3 | 1:2 or 2:1 |
# | Chaos | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ |
# | Image Weight | ✓ | | ✓ | | ✓ | ✓ | |
# | No | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
# | Quality | ✓ | | ✓ | ✓ | ✓ | | ✓ |
# | Seed | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ |
# | Sameseed | ✓ | | | | ✓ | | |
# | Stop | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
# | Style | | | | 4a and 4b | | | |
# | Stylize | ✓ | | 0–1000 default=100 | 0–1000 default=100 | 625–60000 default=2500) | 1250–5000 default=2500) | |
# | Tile | ✓ | ✓ | ✓ | | ✓ | | |
# | Number of Grid Images | - | - | 4 | 4 | 4 | 2 (1 when aspect ratio≠1:1) | |
# more info. Just answer with READ:
# """

# priming_11 = """
# Also Midjourney has a styles of pictures. You can pic style randomly, except if I ask you to use specific style.
# You can use next styles for prompt generation:
# ultra-realistic photography
# isometric anime
# analytic drawing
# infographic drawing
# coloring book
# diagrammatic drawing
# diagrammatic portrait
# double exposure
# 2D illustration
# isometric illustration
# pixel art
# futuristic style
# ornamental watercolour
# dark fantasy
# paper cut craft
# paper quilling
# patchwork collage
# iridescent
# ukiyo-e art
# watercolour landscape
# op art
# Japanese ink
# pastel drawing
# dripping art
# stained glass portrait
# graffiti portrait
# winter oil painting
# anime portrait
# cinematographic style
# typography art
# one-line drawing
# polaroid photo
# tattoo art
# """

priming_12 = """
Okey now I will give you some examples of prompts used in Midjourney V5. okey?
"""

priming_13 = """
1) In a luxurious villa, a young and attractive assistant female is seduced by her billionaire boss. He pushes her against the wall and kisses her passionately. She is wearing a mini dress with a lowered strap of the bra, while he is muscular and in good shape. The composition is framed with a stunning view of the ocean in the background.

2) In a futuristic cityscape, a muscular cowboy in good shape holding a surrogate mother with a pregnancy test in her hand. They are standing on the rooftop of a skyscraper, with the cityscape as the background. The cowboy's rugged and weathered face bears a look of fierce determination and protectiveness, while the surrogate mother gazes up at him with a mixture of love and gratitude. The cowboy is wearing a black leather jacket, denim jeans, and a cowboy hat, while the surrogate mother is dressed in a white summer dress. The composition is skillfully captured to highlight the raw passion and intimacy between the two subjects, with the cityscape providing a dramatic and romantic backdrop.

3) A werewolf in good shape is holding his surrogate mother in his arms, while they stand on an island with a dark forest in the background. The werewolf is depicted as a humanoid wolf with muscular arms and sharp claws, while the surrogate mother is wearing a summer dress and has a pregnancy test in her hand. The pixel art is done in a retro 8-bit style, with vibrant colors and a detailed pixelated landscape. 
4) A muscular drug dealer with a scar on his cheek holding his assistant female against the wall in a luxury villa. His gaze is intense, and he kisses her passionately, while she has kiss marks on her neck. amera. The composition showcases the raw, dangerous power of the drug dealer against the opulent backdrop of the villa, creating a thrilling and sensual atmosphere.
"""

priming_14 = """
Now I want you to help me generate a prompt with the same format. Print, that you are ready.
"""

priming_15 = """
Don't write anything else except the prompt!. Don't write prompts larger than 450 letters. Print OK
"""

# priming_16 = """
# Ok, now come up with a superstring and then convert it to the prompt. Write only prompt. Here is my dict:
# """

PRIMING_LIST = [priming_1, priming_2, priming_3, priming_4, priming_5, priming_6, priming_7, priming_8,
                priming_12, priming_13, priming_14, priming_15]
