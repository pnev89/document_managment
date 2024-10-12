"""Test adding ingest update dataframe tests."""

import pytest
from src.documents._elasticsearch_interaction import ElasticsearchInteraction

index = "test_index"

class TestElasticsearchInteraction:
    
    def test_index_document_success(self):
        # Create a mock Elasticsearch client
        doc_id_response = {'_id': '1', 'result': 'created'}


        # Create an instance of your ElasticsearchInteraction class
        es = ElasticsearchInteraction()

        # Define the document content and index
        document_content = {
            'title': 'Sample Document',
            'content': 'This is a sample document for Elasticsearch.',
            'date': '2024-10-12'
        }

        # Call the method
        response = es.index_document(content=document_content, index=index)

        

        # Assertions
        assert response['result'] == 'created'

        es.delete_index(index=index)

    def test_delete_document(self):

        # Create document first
        # Create an instance of your ElasticsearchInteraction class
        es = ElasticsearchInteraction()
        documents = []

        # Define the document content and index
        document_content = {
            'title': 'Sample Document',
            'content': 'This is a sample document for Elasticsearch.',
            'date': '2024-10-12'
        }

        # Call the method
        response = es.index_document(content=document_content, index=index)

        documents.append(response['_id'])

        # Define the document content and index
        document_content = {
            'title': 'Sample Document',
            'content': 'This is a sample document for Elasticsearch.',
            'date': '2024-10-12'
        }

        # Call the method
        response = es.index_document(content=document_content, index=index)

        documents.append(response['_id'])

        result = es.delete_document(index=index, doc_ids=documents)

        assert result is not None

        es.delete_index(index=index)
    
    def test_failed_delete_document(self):

        # Create document first
        # Create an instance of your ElasticsearchInteraction class
        es = ElasticsearchInteraction()
        documents = []

        # Define the document content and index
        document_content = {
            'title': 'Sample Document',
            'content': 'This is a sample document for Elasticsearch.',
            'date': '2024-10-12'
        }

        # Call the method
        response = es.index_document(content=document_content, index=index)

        documents.append("test_12345")

        
        result = es.delete_document(index=index, doc_ids=documents)

        assert result is None

        es.delete_index(index=index)
    
    def test_delete_index(self):
        # Create document first
        # Create an instance of your ElasticsearchInteraction class
        es = ElasticsearchInteraction()
        documents = []

        # Define the document content and index
        document_content = {
            'title': 'Sample Document',
            'content': 'This is a sample document for Elasticsearch.',
            'date': '2024-10-12'
        }

        # Call the method
        response = es.index_document(content=document_content, index=index)

        response = es.delete_index(index=index)

        assert response is not None

    

