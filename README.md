# keyword_related_questions

## Overall Design
This module will generate a list of the best questions related to some given keyword.

## Functional Design
```
def generate_keyword_questions(keyword):
  '''
    This functions generates a list of questions that contains the given keyword.
    keyword: the word/phrase that must be included in the generated list of questions
    
    [keyword_question]: list of generated questions that contain keyword
  '''
  return [keyword_questions]
  
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
  
def score_keyword_questions([keyword_questions]):
  '''
    This function creates a dictionary where each:
        key: element of [keyword_questions]
        value: score of given element from stackexchange
    [keyword_questions]: list of questions that contain some keyword
    
    {keyword_questions_score}: dictionary of questions as described above
  '''
  return {keyword_questions_score}
  
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
