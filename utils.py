def add_comment_to_file(comment, file):
  transformed_comment = transform_comment(comment)
  print(transformed_comment)
  append_to_text_file(file, transformed_comment)
  return

def create_dict_from_headers(dict, keys_to_keep):
  dict_values = {}

  for key in keys_to_keep:
    dict_values[key] = dict[key]

  return dict_values

def clean_string(string):
  string = str(string)
  # Remove all ;, since that will be used as csv seperator
  string = string.replace(';', '')
  string = string.replace('\n', '')
  return string

def clean_dict(dict):
  keys = dict.keys()

  for key in keys:
    value = dict[key]
    cleaned_value = clean_string(value)
    dict[key] = cleaned_value
  
  return dict

def append_to_text_file(textfile, elements_list):
  textfile.write(str(elements_list))
  textfile.write('\n')

def transform_comment(comment):
    headers = [ 'id', 'author', 'body', 'can_mod_post', 'created_utc', 'parent_id', 'score', 'author_flair_text']
    headers_dict = create_dict_from_headers(comment, headers)
    cleaned_dict = clean_dict(headers_dict)
    return cleaned_dict

def get_amount_of_comments_by_filepath(filepath):
    file = open(filepath, 'r')
    amount_of_comments = len(file.readlines())
    file.close()
    return amount_of_comments

def is_coin_mentioned(name_and_ticker, text):
    # Implement text.endswith() 
    for string in name_and_ticker:
        if text.endswith(string):
          return True
        if F" {string} " in text:
            return True
        if F" {string}," in text:
            return True
    return False


