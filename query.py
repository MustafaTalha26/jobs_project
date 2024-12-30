from infra.mongodb_connector import get_database

def simple_query():
    # get_database() connects to the mongodb database.
    database = get_database()

    #'jobs' is the collection name that exists in the database.
    jobs_collection = database['jobs']

    # Printing data with state : Texas value. 
    documents = jobs_collection.find({"state":"Texas"})
    for document in documents:
        print(document)

simple_query()