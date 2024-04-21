# Notes

## Components of Langchain

    -Chat_Models: while you can directly talk to llms but what langchain does is oprovide a abstraction such as chat_messages which are comman to users.they interface with chat messages rather than raw text.
        -All messages have role and content properties. The role tells the LLM who is sending the message, and the content is the message itself.
        -Here are the most commonly used messages:
            1.<code>HumanMessage</code>: A message from the user interacting with the language model.
            2.<code>AIMessage</code>: A message from the language model.
            3. <code>SystemMessage</code>: A message that tells the language model how to behave. Not all providers support the SystemMessage.
        -Always keep in mind while doing RAG=> Review_System_prompt, Human_review_prompt, review_chat_prompt(LLM)
            -- to create prompttemplates- u pass input_vars and templates
            -- in review_chat_prompt- combine the systme and huma review prompts
            ---Requirement of a review_template/prompt is just like saying a prompt before the original prompt to make the response has some credibility.

## RAG(Reality-Augmented generation)

    -basically llms are still generating text and chatting but they have source of truth. Instead of saying juptier has the most moons, which is not true acoording to recnet discories now the model will resopnse i dk or as of last knowledge it is moon. If it will find some source of truth to back its response then it will say it is saturn, as we now have nasa's 'data to back/validate their responses

        1. For this we use somwthing called vector stores to store our data as passing the context to the model manually would never scale
        2.To overcome this, you need a retriever. The process of retrieving relevant documents and passing them to a language model to answer questions is known as retrieval-augmented generation (RAG).

    - Embeddings -> way of represtning the meaning of text, data, images, audios any unstructured data in a high level dimensiion vectors
    - Vecotr db-> Db's that stores the cluster of closest embeddings together in a non traditional way unline a table(rw,col) and doocuments, for fast retrivals and wirtes. they basically give the llms long lasting memory. Many use cases -> making agents, recomdendation systems and working with unstructred data that has no textual context lik with audio, videos or media in general.

## -- One of the most common ways to store and search over unstructured data is to embed it and store the resulting embedding vectors, and then at query time to embed the unstructured query and retrieve the embedding vectors that are 'most similar' to the embedded query. A vector store takes care of storing embedded data and performing vector search for you

![alt text](https://python.langchain.com/assets/images/vector_stores-125d1675d58cfb46ce9054c9019fea72.jpg)
