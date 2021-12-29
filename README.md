# keyword_related_questions
## Set-Up
1. Go to the following link: https://archive.org/download/stackexchange
2. Download the following file: "stackoverflow.com-Posts.7z" (17.2G)
3. Now unzip the downloaded file and move the file into the same folder as "convert_xml_to_csv.py"
4. Run the python file above. This converts the xml file into a csv file
5. Go to the following link: https://www.elastic.co/downloads/elasticsearch
6. Choose the platform for your device and download Elasticsearch
7. Go to the following link: https://www.elastic.co/downloads/kibana
8. Choose the platform for your device and download Kibana
9. Unzip both the downloaded Elasticsearch and Kibana
10. Open two console windows. 
11. In the first console window, cd into elastic search folder.
12. Run elasticsearch with "bin/elasticsearch" and check to see if server is running at "http://127.0.0.1:9200/"
13. In the second console window, cd into kibana folder.
14. Run kibana with "bin/kibana" and check to see if server is running at "http://127.0.0.1:5601/"
15. Now run "main.py" to load the csv file into elastic search


## Overall Design
This module will generate a list of the best questions related to some given keyword.

## Functional Design
``` python
def generate_keyword_questions(keyword):
  '''
    This functions generates a list of questions that contains the given keyword.
    keyword: the word/phrase that must be included in the generated list of questions
    This function will return a list of the top 5 questions related to some keyword.
    Utilizes all of the functions defined above.
    keyword: word/phrase that each question must be strongly related to
    
    {keyword_questions_score}: dictionary of questions as described above
  '''
  return {keyword_questions_score}
  
def filter_keyword_questions(keyword, [keyword_questions]):
  '''
    This function filters out questions that are not related to the given keyword 
        from the given list [keyword_questions].
    This relation will be determined primarily by the syntactic position of the 
        given keyword in the dependency tree.
    keyword: word/phrase that each question must be strongly related to
    [keyword_questions]: list of unfitered questions that contain the keyword
    
    [filtered_questions]: list of filtered questions that contain the keyword
  '''
  return [filtered_questions]
  
def best_keyword_questions(keyword):
   '''
    This function will return a list of the top 5 questions related to some keyword.
    Utilizes all of the functions defined above.
    keyword: word/phrase that each question must be strongly related to
    
    top_keyword_questions: top 5 questions related to some keyword.
   '''
   return [top_keyword_questions]
```
## Algorithmic Design
### Load data:
- (Manual) secure copy unzipped data from my machine to machines
- Load XML file into elastic search


### Parse data
#### Generate keyword questions
- For each entry that contains the keyword, add entry to dictionary where the question is key and #upvotes are values
- Return dictionary

#### Filter keyword questions
- For each key in the dictionary, consider the syntactic position of the keyword using dependency parsing
- If the position of the keyword is NOT relatively close to the root, delete entry
- Repeat until each entry is considered
- Return dictionary

#### Best keyword questions
- For every element in dictionary, find the top 5 entries
- Return top 5 entries
