from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def get_instagram(instructions, img_description):
    description = instructions + " The post looks like this: " + img_description
    template = """Here is the description: {description}

    You are given visual description of picture I want to post on Instagram. Write me the caption for the post.
    A perfect Instagram caption should have the following points:
    Make the caption seem like written by a human.
    Keep it short and to the point, especially the first few words, as they appear before the "more" button
    Start with an attention-grabbing phrase or question to encourage followers to read further.
    Write in a tone that feels genuine and aligns with your brand’s personality.
    Use emojis to add personality and break up text, making the caption more visually engaging.
    Use spacing and line breaks to improve readability and emphasize key points.
    Use emotion to connect with your audience, whether it’s humor, inspiration, or empathy.
    Share a brief story or anecdote that adds depth to the image or video, making the post more memorable.
    Provide context that enhances the visual content, such as the inspiration behind it or the story of its creation.
    Incorporate relevant hashtags naturally within the caption or at the end to increase discoverability.

    Output: (caption)
    """

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3.1")

    chain = prompt | model

    ans = chain.invoke({"description": description})
    print(ans)
    return ans


instructions = """ she just bought new headphones"""

img_description = """The image depicts a person, likely a young woman or girl, from behind and in profile view. She has long hair that extends to her midsection and is wearing what appears to be a dark-colored top with short sleeves. The background of the image is neutral in color and does not provide any additional context or information about the location or setting."""

get_instagram(instructions, img_description)
