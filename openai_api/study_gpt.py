priming_1 = """
Hello :) Today we are gonna create Images with a Diffusion model. I am gonna feed you some information about it. okey?
"""

priming_2 = """
Midjourney generates images from user prompts by adapting actual art styles to create an image of any combination of things desired. It excels at creating fantasy and sci-fi environments with dramatic lighting like rendered concept art from a video game. Midjourney is an AI image generation tool that uses a Machine Learning (ML) algorithm trained on a large amount of image data to produce unique images. It is powered by Latent Diffusion Model (LDM), a cutting-edge text-to-image synthesis technique. LDMs are used to enable DM training on limited computational resources without compromising on quality and flexibility. This significantly improves visual fidelity. A cross-attention layer is introduced to the model architecture to turn the diffusion model into a powerful and flexible generator for generally conditioned inputs such as text and bounding boxes, enabling high-resolution convolution-based synthesis.
But wait, I have more info. Just answer with READ
"""

priming_3 = """
Midjourney routinely releases new model versions to improve efficiency, coherency, and quality. The latest model is the default, but other models can be used using the --version or --v parameter or by using the /settings command and selecting a model version. Different models excel at different types of images.
The Midjourney V5 model is the newest and most advanced model, with very high coherency, higher resolution, and supports advanced features like repeating patterns with --tile. It was released on March 15th, 2023.
To use the V5 model, add the --v 5 parameter to the end of a prompt, or use the /settings command and select MJ Version 5. It has a much wider stylistic range, higher image quality with 2x resolution increase, and more detailed images. It also supports --ar aspect ratios greater than 2:1 and --iw for weighing image prompts versus text prompts.
However, it may be harder to use and requires longer, more explicit prompts for better results. The V5 model is currently in alpha test and will be significantly modified before full release.
More about V5:
V5 is our second model trained on our AI supercluster and has been in the works for 5 months. It uses significantly different neural architectures
and new aesthetic techniques.
But wait i have more info. Just answer with READ:
"""

priming_4 = """
Basic Parameters
Aspect Ratios
--aspect, or --ar Change the aspect ratio of a generation.
Chaos
--chaos <number 0–100> Change how varied the results will be. Higher values produce more unusual and unexpected generations.
No
--no Negative prompting, --no plants would try to remove plants from the image.
Quality
--quality <.25, .5, 1, or 2>, or --q <.25, .5, 1, or 2> How much rendering quality time you want to spend. The default value is 1. Higher values cost
more and lower values cost less.
Seed
--seed <integer between 0–4294967295> The Midjourney bot uses a seed number to create a field of visual noise, like television static, as a
starting point to generate the initial image grids. Seed numbers are generated randomly for each image but can be specified with the --seed or
--sameseed parameter. Using the same seed number and prompt will produce similar ending images.
Stop
--stop <integer between 10–100> Use the --stop parameter to finish a Job partway through the process. Stopping a Job at an earlier percentage
can create blurrier, less detailed results.
Style
--style <4a, 4b or 4c> Switch between versions of the Midjourney Model Version 4
Stylize
--stylize <number>, or --s <number> parameter influences how strongly Midjourney's default aesthetic style is applied to Jobs.
Uplight
--uplight Use an alternative "light" upscaler when selecting the U buttons. The results are closer to the original grid image. The upscaled image is
less detailed and smoother.
Upbeta
--upbeta Use an alternative beta upscaler when selecting the U buttons. The results are closer to the original grid image. The upscaled image has
significantly fewer added details. Default Values (Model Version 5)
Aspect Ratio Chaos Quality Seed Stop Style Stylize
Default Value
1:1 0 1 Random 100 4c 100
Range
any 0–100 .25 .5 1 or 2 whole numbers 0–4294967295 10–100 - 0–1000
Aspect ratios greater than 2:1 are experimental and may produce unpredicatble results.
But wait, I have more info. Just answer with READ:
"""

priming_5 = """
****Default Values (Model Version 4)****
| | Aspect Ratio | Chaos | Quality | Seed | Stop | Style | Stylize |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Default Value | 1:1 | 0 | 1 | Random | 100 | 4c | 100 |
| Range | 1:2–2:1 | 0–100 | .25 .5 or 1 | whole numbers 0–4294967295 | 10–100 | 4a, 4b, or 4c | 0–1000 |
****Default Values (Model Version 5)****
| | Aspect Ratio | Chaos | Quality | Seed | Stop | Style | Stylize |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Default Value | 1:1 | 0 | 1 | Random | 100 | 4c | 100 |
| Range | any | 0–100 | .25 .5 1 or 2 | whole numbers 0–4294967295 | 10–100 | 0–1000 | 0–1000 |
**Compatibility**
| | Affects initial generation | Affects variations + remix | Version 5 | Version 4 | Version 3 | Test / Testp | Niji |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Max Aspect Ratio | ✓ | ✓ | any | 1:2 or 2:1 | 5:2 or 2:5 | 3:2 or 2:3 | 1:2 or 2:1 |
| Chaos | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ |
| Image Weight | ✓ | | ✓ | | ✓ | ✓ | |
| No | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Quality | ✓ | | ✓ | ✓ | ✓ | | ✓ |
| Seed | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sameseed | ✓ | | | | ✓ | | |
| Stop | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Style | | | | 4a and 4b | | | |
| Stylize | ✓ | | 0–1000 default=100 | 0–1000 default=100 | 625–60000 default=2500) | 1250–5000 default=2500) | |
| Tile | ✓ | ✓ | ✓ | | ✓ | | |
| Number of Grid Images | - | - | 4 | 4 | 4 | 2 (1 when aspect ratio≠1:1) | |
more info. Just answer with READ:
"""

priming_6 = """
Okey Now i will give you some examples of prompts used in Midjourney V5. okey?
"""

priming_7 = """
Prompt 1: ultra wide shot, modern photo of beautiful 1970s woman in hawaii. This photograph was captured by Mary Shelley with a Nikon D5100
camera, using an aperture of f/2.8, ISO 800, and a shutter speed of 1/100 sec. UHD dtm HDR 8k --ar 2:3 --v 5 prompt 2: A steampunk-inspired,
futuristic battle-ready jetski skims across the water with a fierce presence. Intricate gears and brass fittings adorn its hull, showcasing the perfect
blend of advanced technology and Victorian aesthetics. This realistic masterpiece glistens under the sun, ready for action. --ar 16:10 --s 50 --v 5
--q 2 prompt3: epic background art, simple hacker
theme, divine color scheme, mystical codes, alphanumeric sequence, magic, high quality 4k, render in octane --v 5 --ar 9:16 prompt 5: Pov Highly
defined macrophotography of a realistic cat wearing reflective sunglasses relaxing at the tropical island, dramatic light --ar 2:3 --s 750 --v 5
Thank you for providing the examples of prompts used in Midjourney V5. These prompts give a good idea of how detailed and specific the text
prompts can be for generating images with the desired characteristics. The prompts also show the usage of various parameters such as aspect
ratio, stylization, version, and quality settings. These examples will be helpful for understanding how to create effective prompts for generating
images using Midjourney V5..
"""

priming_9 = """
Great. Here are some more examples of Midjourney prompts. Prompt 1: conjoined twins attched at the side, dirty, tattered, cinematic light, ultra
realistic, high contrast, hdr, dark rich colors, photography, powerful, stare, weathered face, 30 - megapixel, 4k, 85 - mm - lens, sharp - focus,
intricately - detailed, long exposure time, f/ 8, ISO 100, shutter - speed 1/ 125, diffuse - back - lighting, award - winning photograph, facing -
camera, High - sharpness, depth - of - field, ultra - detailed photography --ar 3:2 --q 2 --v 5. Prompt 3: Full Body beautiful blonde, wearing a
brown jacket, photography, Canon EOS 5D Mark IV DSLR camera, EF 50mm f/1.8 STM lens, Resolution 30.4 megapixels, ISO sensitivity:
32,000, Shutter speed 8000 second --ar 9:16 --upbeta --v 5. Prompt 4: hasselblad 24mm full body shot photography of gorgeous satisfied looking
african woman, detailed natural skin, no makeup, detailed eyes, long dreadlocks --ar 2:3 --q 5 --v 5 --v 4. Prompt 5: Beautiful dark red sunset
over the sea shore at night, intricate, amazing, beautiful, realistic, ultra high resolution, wide angle, depth of field, π dynamic lighting --ar 1:2 --v 5
Thank you for providing more examples of Midjourney prompts. These examples further demonstrate the level of detail and specificity that can be
used in text prompts to generate desired images. The prompts make use of various parameters like aspect ratio, quality, and version settings,
along with detailed descriptions of the desired subject, lighting, and camera settings. These examples will be useful for understanding the range
of possibilities when generating images using Midjourney
"""

priming_10 = """
Here are some more prompt examples: Prompt 1: A stunning, ultra-realistic photograph of a fierce Viking warrior meticulously sharpening his
formidable blade amidst the rugged, untamed wilderness of the Scandinavian landscape. The scene is captured with a Nikon D850 camera using
a 70-200mm f/2.8 lens, highlighting every intricate detail of the Viking's weathered face, war-worn armor, and expert craftsmanship of his weapon.
The settings used are an aperture of f/4, ISO 400, and a shutter speed of 1/200 sec, balancing the natural light and shadows to emphasize the
intensity and determination in the Viking's eyes. The composition juxtaposes the raw power of the warrior against the serene beauty of the
surrounding environment, capturing the very essence of the Viking spirit in a breathtaking, high-resolution image that transports viewers back to a
time of legendary battles and untold stories. --ar 16:9 --q 1.5 --v 5.
Prompt 2: A stunning and atmospheric 1970's New York street cafe captured in a nostalgic and cinematic style, reminiscent of the golden age of
film photography. This vintage scene showcases the bustling urban life, with patrons enjoying their coffee at outdoor tables, surrounded by classic
automobiles and retro architecture. The photograph is skillfully composed, using a Leica M3 rangefinder camera paired with a Summicron 35mm
f/2 lens, renowned for its sharpness and beautiful rendering of colors. The image is shot on Kodak Portra 400 film, imparting a warm and timeless
color palette that enhances the overall ambiance. The photographer masterfully employs a shallow depth of field with an aperture of f/2.8,
isolating the cafe and its patrons from the bustling city background. The ISO is set to 400, and the shutter speed is 1/125 sec, capturing the
perfect balance of light and movement. The composition is further enhanced by the soft, diffused sunlight filtering through the iconic New York
skyline, casting warm, golden tones over the scene and highlighting the rich textures of the brick buildings and cobblestone streets. --ar 3:2 --q 2.
Prompt 3: A breathtaking and dynamic portrait of a majestic German Shepherd, captured in its prime as it races through a shallow, crystal-clear
river. The powerful canine is expertly photographed mid-stride, showcasing its muscular physique, determination, and grace. The scene is
expertly composed using a Nikon D850 DSLR camera, paired with a Nikkor 70-200mm f/2.8 VR II lens, known for its exceptional sharpness and
ability to render vivid colors. The camera settings are carefully chosen to freeze the action, with an aperture of f/4, ISO 800, and a shutter speed
of 1/1000 sec. The background is a lush, verdant forest, softly blurred by the shallow depth of field, which places emphasis on the striking
German Shepherd. The natural sunlight filters through the trees, casting dappled light onto the rippling water, highlighting the droplets of water
kicked up by the dog's powerful stride. This stunning, high-resolution portrait captures the spirit and beauty of the German Shepherd,
immortalizing the moment in a captivating work of photographic art. --ar 4:5 --q 2 --v 5.
Just answer with READ:
"""
priming_11 = """
create a prompt with the same format.
"""

priming_12 = """ 
Don't write the version at the end of the promt (--ar 4:5 --q 2 --v 5)! Don't use sedducive words, don't write promts larger then 450 letters.  Just write prompt with no hints and don't thank me, write everything in 1 sentence
"""
PRIMING_LIST = [priming_1, priming_2, priming_3, priming_4, priming_5, priming_6, priming_7, priming_9,
                priming_11, priming_12]
