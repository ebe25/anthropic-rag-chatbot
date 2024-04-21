import os
from getpass import getpass
from langchain_anthropic import ChatAnthropic
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

chat = ChatAnthropic(temperature=0, model_name="claude-3-opus-20240229")

##now will make a review template which our llm will refer 
review_template_str = """Your job is to use patient
reviews to answer questions about their experience at
a hospital. Use the following context to answer questions.
Be as detailed as possible, but don't make up any information
that's not from the context. If you don't know an answer, say
you don't know.

{context}
"""
##Role prompto give to the system
review_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["context"],
        template=review_template_str,
    )
)

##Questions are will be pre defined
review_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["question"],
        template="{question}",
    )
)

#config 

messages = [review_system_prompt, review_human_prompt]



##Review_chat_prompt
##this is the final review chat prompt
review_chat_prompt= ChatPromptTemplate(
  input_variables=["context","question"],
  messages=messages
)



###using the StrOutputFormatter
output_parser = StrOutputParser()

#chainnig process for the review stuff
review_chain =  review_chat_prompt | chat | output_parser
context = "I had a great stay!"
question = "Did anyone have a positive experience?"
response = review_chain.invoke({"context": context, "question": question})

print(response)
