# TODO: Make sure index name is handled
import pinecone
import os

# Initialize Pinecone environment and index
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'),
              environment=os.getenv('PINECONE_ENVIRONMENT'))

# Function to get the Pinecone index


def get_index(index_name):
    # Check if the index exists; if not, create one or handle it accordingly
    # For simplicity, we're assuming the index is already created and available
    return pinecone.Index(index_name=index_name)

# Query the Pinecone index for vectors similar to the input vector


def query_vectors(vector, index_name='your-index-name', top_k=10):
    # Fetch the index
    index = get_index(index_name)

    # Perform the query
    query_results = index.query(
        queries=[vector], top_k=top_k, include_metadata=True)

    # Extract results
    matches = query_results['matches']

    # Here, you would process the 'matches' according to your Pinecone response format
    # and return them. The following line is a placeholder for the structure based on your requirements.
    # You should replace 'score' and 'metadata' with the actual keys from Pinecone's response.
    results = [{'score': match['score'], 'metadata': match['metadata']}
               for match in matches]

    return results

# You may want to add additional functions for batch querying, updating, or deleting vectors if required.
