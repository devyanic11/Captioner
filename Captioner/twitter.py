from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def get_instagram(instructions, img_description):
    description = instructions + " The post looks like this: " + img_description
    template = """Here is the description: {description}

    You are given visual description of picture I want to post on twitter. Write me the caption for the post.
    A perfect twitter caption should have the following points:
    Stick to the character limit (280 characters), ensuring your message is concise and to the point.
    Include a hook or an interesting statement that grabs attention. This could be a question, a bold opinion, or a surprising fact.
    Use 1-2 relevant hashtags to increase visibility without cluttering the tweet. Avoid overusing hashtags.
    Encourage interaction by asking a question, inviting replies, or prompting users to retweet, like, or click a link.
    Match the tone to your brand or audience. It can be professional, casual, humorous, or inspirational, depending on your target audience.
    Ensure the content is timely and relevant to current trends or topics of interest in your niche.
    If your message requires more than one tweet, consider creating a thread. This keeps your content organized and allows followers to engage with each part of your message.

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
