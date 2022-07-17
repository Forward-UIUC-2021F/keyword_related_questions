import xml.sax
import csv
import time
start_time = time.time()

import os

# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv('../.env')

data_root_dir = os.getenv('DATA_DIR')


# Reads the xml file using Simple API for XML (SAX)
class PostsHandler(xml.sax.ContentHandler):  
  def startElement(self, tag, attributes):
    # Guarantee that each post has a title
    if tag == "row" and "Title" in attributes.getNames():

      # gets the relevant attributes
      id = attributes["Id"]
      score = attributes["Score"]
      title = attributes["Title"]

      # creates row to be added
      row = [id, score, title]
      
      # Append row to our csv file
      with open(f"{data_root_dir}/Posts.csv",'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)

  def endElement(self, tag):
    pass

  def characters(self, content):
    pass
    
def load_data(file):
  parser = xml.sax.make_parser()
  parser.setFeature(xml.sax.handler.feature_namespaces,0)
  handler = PostsHandler()
  parser.setContentHandler(handler)
  parser.parse(file)

def main():
  load_data(f"{data_root_dir}/Posts.xml")
  print("--- %s seconds ---" % (time.time() - start_time))
main()
