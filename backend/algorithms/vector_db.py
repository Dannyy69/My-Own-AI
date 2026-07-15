from models.document import Document


class VectorDB:

    def __init__(self):
        self.documents = []

    def add_document(self, document: Document):
        self.documents.append(document)

    def get_documents(self):
        return self.documents

    def count(self):
        return len(self.documents)