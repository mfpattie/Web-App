
def format_results_for_display(results):
    """
    Takes a list of result objects and formats them to a list of dictionaries
    for frontend display.

    Parameters:
    - results: A list of result dicts with 'metadata' and 'score' keys.

    Returns:
    - A list of formatted result dicts ready to be converted to JSON.
    """
    formatted_results = []
    for result in results:
        # Assume each result has 'metadata' as a nested dictionary with relevant keys
        metadata = result.get('metadata', {})

        # Create a formatted result with the desired structure
        formatted_result = {
            'vector_id': metadata.get('vector_id'),   # ID of the vector
            # Chunk number within the document
            'chunk_num': metadata.get('chunk_num'),
            # Day when the document was generated/recorded
            'day': metadata.get('day'),
            'dist_name': metadata.get('dist_name'),   # Distribution name
            # Document title or name
            'document_name': metadata.get('document_name'),
            # Local Education Agency ID, if applicable
            'leaid': metadata.get('leaid'),
            # Name of the meeting or event
            'meeting_name': metadata.get('meeting_name'),
            'month': metadata.get('month'),           # Month of the year
            # Local source identifier
            'local_source': metadata.get('local_source'),
            # S3 source path, if applicable
            's3_source': metadata.get('s3_source'),
            'state': metadata.get('state'),           # State information
            # Associated text or excerpt
            'text': metadata.get('text'),
            'filetype': metadata.get('filetype'),     # Type of file
            'year': metadata.get('year'),             # Year of the document
            # Page number in the PDF
            'page_number': metadata.get('page_number'),
            'score': result.get('score'),             # The similarity score
        }
        formatted_results.append(formatted_result)

    return formatted_results
