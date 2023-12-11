import openai
from flask import current_app


def generate_embedding(text):
    try:
        # Using an environment variable for the OpenAI API key
        openai.api_key = current_app.config.get('OPENAI_API_KEY')

        # Calling the OpenAI API to generate embeddings for the given text
        embedding_response = openai.Embedding.create(
            input=[text],
            engine="text-search-ada-query-001"  # Change the engine if needed
        )

        # Return the embedding vector
        return embedding_response["data"][0]["embedding"]
    except openai.error.OpenAIError as e:
        # Handle API errors gracefully
        current_app.logger.error(f"OpenAI API error: {e}")
        raise e
