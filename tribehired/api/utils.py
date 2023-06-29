from typing import List, Dict


def filter_comments(comments, name=None, email=None, body=None):
    filtered_comments: List[Dict] = []
    for comment in comments:
        if (name is None or name.lower() in comment['name'].lower()) and \
           (email is None or email.lower() in comment['email'].lower()) and \
           (body is None or body.lower() in comment['body'].lower()):
            filtered_comments.append(comment)
    return filtered_comments
