import ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def get_image_description(img):
    prompt = f"Describe the image. {img}"
    response = ollama.chat(
        model="llava",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
        ],
    )

    content = response["message"]["content"]
    # print(content)
    return content


def get_linkedin(instructions, img_description):
    description = instructions + " The post looks like this: " + img_description
    template = """Here is the description: {description}

    You are given visual description of picture I want to post on linkedin. Write me the content for the post.
    A perfect LinkedIn post should have the following points:
    Clearly state the purpose or main point of your post. Avoid unnecessary jargon or fluff.
    Aim for 150-200 words. Shorter posts get more engagement, but longer ones can work if they provide substantial value.
    Start with a strong hook to grab attention within the first 2-3 lines. LinkedIn truncates longer posts, so make sure the most important part appears before the "see more" link.
    Use a provocative question, bold statement, or interesting fact to draw readers in.
    Encourage interaction with a CTA, such as asking for opinions, inviting comments, or sharing experiences wherever possible.
    Write in a way that reflects your professional personality. Authenticity builds trust.
    Use 3-5 relevant hashtags to increase the reach of your post. Choose industry-specific hashtags for better targeting.
    """

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3.1")

    chain = prompt | model

    ans = chain.invoke({"description": description})
    return ans


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
    return ans


def get_twitter(instructions, img_description):
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
    return ans
