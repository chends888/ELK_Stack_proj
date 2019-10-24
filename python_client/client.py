from elasticsearch import Elasticsearch
choice = int(input('Insert query type \n(0: By title, 1: By description or 2: Both): '))
es = Elasticsearch()
if (choice == 0):
    query = input('Insert movie title to match: ')
    res = es.search(index='sakila', size=9999, body={
                                            "query": {
                                                "multi_match" : {
                                                    "fields" : ["title"],
                                                    "query" : query,
                                                    "fuzziness": "AUTO"
                                                }
                                            }
                                        })

elif (choice == 1):
    query = input('Insert movie description to match: ')
    res = es.search(index='sakila', size=9999, body={
                                            "query": {
                                                "multi_match" : {
                                                    "fields" : ["description"],
                                                    "query" : query,
                                                    "fuzziness": "AUTO"
                                                }
                                            }
                                        })

else:
    query = input('Insert movie description or title to match: ')
    res = es.search(index='sakila', size=9999, body={
                                            "query": {
                                                "multi_match" : {
                                                    "fields" : ["title", "description"],
                                                    "query" : query,
                                                    "fuzziness": "AUTO"
                                                }
                                            }
                                        })


print('\n%d movies found:\n' %(res['hits']['total']))
i = 0
total = res['hits']['total']
res = res['hits']['hits']
while True:
    if (i > total):
            break
    for doc in res[i:i+10]:
        # print(total, i)
        # print(res['hits']['total'])
        print('-Score: %s\t \n\tTitle: %s\n\tDescription: %s\n' %(doc['_score'], doc['_source']['title'], doc['_source']['description']))
    test = input('Do you want to view more? (Y/n): ')
    if (test == 'y'):
        i += 10
    else:
        break