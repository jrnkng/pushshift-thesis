from pmaw import PushshiftAPI
from utils import add_comment_to_file, get_amount_of_comments_by_filepath

## Python read file!
file = open('./files/all_comment_ids.txt')
line_of_ids = file.readlines()
ids = line_of_ids[0].split(',')
file.close()


api = PushshiftAPI()
filepath = './transformed_comments_dict.txt'
transformed_comments_file = open(filepath, 'a')

comments_processed = get_amount_of_comments_by_filepath(filepath)

chunk_size = 3000
failed_attempts = 0
try:
    while comments_processed < len(ids): 
        print(comments_processed)
        try:
            comments = api.search_comments(ids=ids[comments_processed: comments_processed + chunk_size])
            for comment in list(comments):
                add_comment_to_file(comment, transformed_comments_file)
            failed_attempts = 0
        except:
            print('error occured, attempts that have failed:', failed_attempts)
            failed_attempts += 1
            if failed_attempts == 10:
                break
        finally:
            comments_processed = get_amount_of_comments_by_filepath(filepath)
finally:
    print(comments_processed, 'have been processed')
    transformed_comments_file.close()
