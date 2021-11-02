# keyword_related_questions

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
- (Manual) Send data from my own machine to machines
- Load XML file into elastic search


### Parse data
Generate
- Looking at each entry
- Check if the entry contains the given keyword
- If it contains the keyword, add it to dictionary where the question is key and #upvotes are values
- Repeat until each entry is considered
- Return dictionary

- Considering the elements in the dictionary
- For each element,
- Consider the syntactic position in the question using SpaCy (Dependency parsing)
- If the syntactic position is low, delete entry
- Repeat until each entry is considered
- Return dictionary

- For every element in dictionary, find the top 5 entries
- Return top 5 entries
