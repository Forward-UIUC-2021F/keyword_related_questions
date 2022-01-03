# Instructions:
# Open two console windows. In the first console window, cd into elastic search folder. In the second console window, cd into kibana folder
# Run elasticsearch with "bin/elasticsearch" and check to see if server is running at "http://127.0.0.1:9200/"
# Run kibana with "bin/kibana" and check to see if server is running at "http://127.0.0.1:5601/"
# Note for reader: Currently, we must convert the xml files into csv files as it is easier to read into ES
import pandas as pd
import requests

import spacy
import networkx as nx

from elasticsearch import Elasticsearch
from elasticsearch import helpers

# Given a xml file, will load in the data into elasticsearch
def load_data(file):
  # Connect to elastic search
  ENDPOINT = "http://localhost:9200/"
  es = Elasticsearch(timeout=600,hosts=ENDPOINT)

  print("elastic search starting...")
  # Load data into dataframe
  df = pd.read_csv(file)
  print("data frame loaded")
  print(df.shape)
  # Convert data into dictionary
  df2 = df.to_dict('records')
  print("converted dataframe to dictionary")
  # Loads in dictionary into elasticsearch
  try:
    res = helpers.bulk(es, generator(df2))
    print("Working")
  except Exception as e:
    print(e)
    pass

# Helper function to convert dictionary into format that elasticsearch understands
# Note: Modify source if want to include more information in "_source"
def generator(df2):
    for c, line in enumerate(df2):
      # print(c)
      yield{
        '_index': 'cs',
        '_type': '_doc',
        '_id': c,
        '_source': {
                'title': line.get("title", ""),
                'score': line.get("score", ""),
        }
      }
    raise StopIteration

def generate_keyword_questions(keyword):
  headers = {
      'Content-Type': 'application/json',
  }

  # Note: The size of data is capped at 10,000. Must implement paging to return reults
  #   See: https://stackoverflow.com/questions/8829468/elasticsearch-query-to-return-all-records
  data = '\n{\n  "_source": ["title","score"],\n  "size": 10000,\n  "query": {\n    "match_phrase": {\n      "title": "keyword"\n    }\n  }\n}'.replace("keyword",keyword)

  # GET request from elasticsearch for a keyword
  req = requests.get('http://localhost:9200/posts/_search', headers=headers, data=data)
  
  # if request is not valid
  if req.status_code != 200:
    # do nothing
    return

  # Otherwise, we got hits!
  hits = req.json()['hits']['hits']

  # Save hits into dictionary
  dict = {}
  for hit in hits:
      source = hit["_source"]
      dict[source["title"]] = source["score"]
  return dict

# filter out questions given a specific keyword
def filter_keyword_questions(keyword, questions):
  # Assuming all questions are in english
  nlp = spacy.load("en_core_web_sm")
  dict = {}
  # We iterate through every question
  for question in questions.keys():
    doc = nlp(question)

    # We check to see if the sentence is valid by checking for presence of verbs
    has_VERB = False
    for token in doc:
      if token.head.pos_ == "VERB":
        has_VERB = True
    if has_VERB == False:
      continue

    # Now we construct a graph
    edges = []
    nodes = []
    for token in doc:
      # FYI https://spacy.io/docs/api/token
      nodes.append('{0}-{1}'.format(token.lower_,token.i))
      for child in token.children:
        edges.append(('{0}-{1}'.format(token.lower_,token.i),
                      '{0}-{1}'.format(child.lower_,child.i)))
    graph = nx.Graph(edges)

    head = ''
    tail = ''
    root = [token for token in doc if token.head == token][0]

    # If the root of the dependency tree is not a verb, we find the sentence invalid
    if root.head.pos_ != "VERB":
      continue
    # Note: this finds the first instance of keyword/root which may affect the desired output
    #   Made choice of picking first instance because it made sense
    
    # Set the head and tail node to determine the syntactic distance
    for node in nodes:
      if keyword == node.split("-")[0] and len(tail) == 0:
        tail = node
      if root.text.lower() == node.split("-")[0] and len(head) == 0:
        head = node
    # https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.shortest_paths.html
    d = nx.shortest_path_length(graph, source=head, target=tail)

    length = len(doc)
    # we modify the score of the sentence to benefit questions that have a keyword close to root
    dict[question] = questions[question] * (1 - (d/length))
  return dict
def main():
  print("Loading in data...")
  # for future self: have a way to auto upload data and not repeat
  load_data("data/Posts.csv")
  print("Done")
  # keyword = "beer"
  # questions = generate_keyword_questions(keyword)
  # filtered_questions = filter_keyword_questions(keyword,questions)
  # sort = sorted(filtered_questions, key=filtered_questions.get, reverse=True)[:10]
  # print(sort)

if __name__ == "__main__":
    main()
