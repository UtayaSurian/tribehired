from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .utils import filter_comments
from .enums import Endpoint
from typing import List, Dict, Union


@api_view(['GET'])
def top_posts(request) -> Response:
    comments = requests.get(Endpoint.comments.value).json()
    posts = requests.get(Endpoint.all_posts.value).json()

    post_comment_count = {}
    for comment in comments:
        post_id = comment['postId']
        post_comment_count[post_id] = post_comment_count.get(post_id, 0) + 1

    # Sort posts by comment count
    sorted_posts: List[Dict] = sorted(posts, key=lambda p: post_comment_count.get(p['id'], 0), reverse=True)
    # Generate API response
    response_data: List[Dict] = []
    for post in sorted_posts:
        post_id = post['id']
        post_title = post['title']
        post_body = post['body']
        total_comments = post_comment_count.get(post_id, 0)

        response_data.append({
            'post_id': post_id,
            'post_title': post_title,
            'post_body': post_body,
            'total_number_of_comments': total_comments
        })

    return Response(response_data)


@api_view(['POST'])
def search_comments(request) -> Response:
    # Get the filter parameters from the request query parameters
    name: Union[str | None] = request.GET.get('name', None)
    email: Union[str | None] = request.GET.get('email', None)
    body: Union[str | None] = request.GET.get('body', None)

    # Fetch comments
    comments = requests.get(Endpoint.comments.value).json()

    # Apply filters based on provided parameters
    filtered_comments = filter_comments(comments, name, email, body)
    if not filtered_comments:
        return Response("Ops, no match found!")
    return Response(filtered_comments)


@api_view(['GET'])
def home(request):
    return Response("Kindly use endpoints to get results instead home url.")


