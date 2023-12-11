# This is the model definition for documents that the app is handling. It maps directly to the metadata.

#TODO: double check the data types for the database.
from app import db

class Document(db.Model):
    __tablename__ = 'documents'  # Use a table name that makes sense for your application

    id = db.Column(db.Integer, primary_key=True)
    vector_id = db.Column(db.String, index=True)  # This could be a string or another type depending on your use case
    chunk_num = db.Column(db.Integer)
    day = db.Column(db.Integer)
    dist_name = db.Column(db.String)
    document_name = db.Column(db.String)
    leaid = db.Column(db.String)
    meeting_name = db.Column(db.String)
    month = db.Column(db.Integer)
    local_source = db.Column(db.String)
    s3_source = db.Column(db.String)
    state = db.Column(db.String)
    text = db.Column(db.Text)
    filetype = db.Column(db.String)
    year = db.Column(db.Integer)
    page_number = db.Column(db.Integer)

    def __repr__(self):
        return f'<Document {self.document_name}>'