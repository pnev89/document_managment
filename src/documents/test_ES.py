from src.documents._elasticsearch_interaction import ElasticsearchInteraction

es = ElasticsearchInteraction(
            host="localhost",
            port=9200
            )



es.delete_index(index="text_index")
