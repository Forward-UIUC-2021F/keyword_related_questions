# Keyword related Questions
The purpose of this module to efficiently generate a list of the best questions related to some given keyword.

## About the Data
- The questions are derived from the posts of StackExchange. More specifically, the titles.
- This data is then indexed into Elasticsearch and Kibana is used to retrieve the results.

## Set-Up
1. Go to the following link: https://archive.org/download/stackexchange
2. Download the following file: "stackoverflow.com-Posts.7z" (17.2G)
3. Now unzip the downloaded file and move the file into the folder "data"
4. Rename `.env.template` to `.env` and specify the path to the data directory
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
15. Now run "main.py" to load the csv file into elastic search (ONLY DO THIS ONE TIME)
16. Now comment line 134 in main.py and uncomment the rest of the code below line 134
17. You may now change the keyword to whatever query you desire

## File structure
```
matt-ho-keyword-related-questions/
    - requirements.txt
    - data/ 
        -- Posts.csv (Create by conversion of xml to csv)
        -- Posts.xml
    - Elasticsearch/
    - Kibana/
    - src/
        -- main.py
        -- convert_xml_to_csv.py
    - README.md
```
- Posts.csv is a file created by the conversion of Posts.xml
- Posts.xml is the file downloaded from the archive.org linked above
- main.py is the main file that will load the csv file into elastic search
- convert_xml_to_csv.py is the file that converts the xml file into a csv file

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

## Demo Video
https://user-images.githubusercontent.com/47504662/148722490-171b7275-a815-4eb8-8411-5f8d56a2182f.mp4

## Sample output
### tree
- Given two directory trees, how can I find out which files differ by content?
- Explain Merkle Trees for use in Eventual Consistency
- What are Expression Trees, how do you use them, and why would you use them?
- Creating JSON arrays in Boost using Property Trees
- How do I compare two source trees in Linux?
- What should I use Clojure's finger trees for?
- Help Understanding Cross Validation and Decision Trees
- Understanding Ukkonen's algorithm for suffix trees
- The possible number of binary search trees that can be created with N keys is given by the Nth catalan number. Why?
- Why DB indexes use balanced trees, not hashtables?

### data
- Passing data between view controllers
- Combine a list of data frames into one data frame by row
- Sending POST data in Android
- Saving an Object (Data persistence)
- HttpServletRequest get JSON POST data
- Read data from SqlDataReader
- Setting a WebRequest's body data
- Using R to download zipped data file, extract, and import data pass post data with window.location.href
- How to write data with FileOutputStream without losing old data?

### string
- Converting string into datetime
- Convert bytes to a string
- Generate random string/characters in JavaScript
- How to check if a string "StartsWith" another string?
- Reverse a string in Python
- How do I check if a string contains another string in Objective-C?
- Trim string in JavaScript?
- Converting 'ArrayList<String> to 'String[]' in Java
- Converting integer to string in Python
- Java string to date conversion

## Issues and Future Work
- The inclusion of additional features could help for a better evaluation of a given question.
- The inclusion described above would require another read-in to Elasticsearch which is costly.
- The number of queries into elastic search is capped at 10,000 results. Need additional code to get # results > 10,000
- More advanced queries built-in to Elasticsearch could be considered to evaluate better questions
- The evaluation process for questions could be tinkered with (i.e. creating a classifier for good and bad questions)
- The list of keywords is not currently pipelined into our main function (Solve by looping through keywords)
- Consideration of answers to evaluate the question posed in the title but will require additional data
- The subtitle for each post is also not considered

## Built with
- Elasticsearch
- Kibana

## References
- https://aclanthology.org/P08-1082.pdf
- https://www.iosrjournals.org/iosr-jce/papers/Vol17-issue4/Version-1/C017411728.pdf
- https://www.youtube.com/watch?v=C-JKcMM6IXE&list=LL&index=3
