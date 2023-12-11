# app/search/views.py

from flask import Blueprint, request, jsonify, render_template
from app.services.pinecone_service import query_vectors
from app.services.openai_service import generate_embedding
from app.utils.helpers import format_results_for_display

# Create a new Blueprint for the search functionality
search_blueprint = Blueprint('search', __name__)

# Define a route for the search feature, allowing only POST requests to avoid exposing sensitive data via URL parameters


@search_blueprint.route('/search', methods=['POST'])
def search():
    # Parse the JSON data sent in the request body
    search_data = request.json
    # Extract the search query from the parsed JSON data
    search_query = search_data.get('query')
    # Optionally, extract additional metadata from the search data if provided
    metadata = search_data.get('metadata', {})

    # Return an error if no search query was provided in the request
    if not search_query:
        return jsonify({'error': 'Empty search query'}), 400

    # Generate an embedding for the search query using OpenAI's API, passing along any metadata that needs to be included
    embedding = generate_embedding(search_query, metadata)

    # Perform a query against the Pinecone index using the generated embedding, specifying the number of top results to return
    # Top_k can be adjusted as per requirement
    results = query_vectors(embedding, top_k=20)

    # Apply a threshold to filter out results with a score less than 0.8 to ensure only relevant results are returned
    relevant_results = [result for result in results if result['score'] > 0.8]

    # Format the filtered results for display using a helper function that prepares them for the frontend
    display_results = format_results_for_display(relevant_results)

    # If using React or other frontend frameworks, send the results back as JSON
    return jsonify(display_results), 200
