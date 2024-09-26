from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


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
    print(ans)
    return ans


instructions = """I'm part of organising team for PUNE FOSS 2.1 and so I want to repost its linkedin post which says only 2 days left for Pune FOSS 2.1."""

img_description = """This appears to be a photo of a person sitting down, holding an object in their hand. The image is not very clear, but it looks like the person might be wearing a dark top and the object they are holding could be some sort of remote or controller with buttons visible on its surface. The background is indistinct, which makes it difficult to discern any specific details about the setting. """
