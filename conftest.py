import object_utils as ou
import pytest


@pytest.fixture(scope="function", autouse=True)
def cleanup_created_objects():

    if ou.User.user_instances:
        local_user_list = [user for user in ou.User.user_instances]
        for user in local_user_list:
            user.delete_object()

    if ou.Post.post_instances:
        local_post_list = [post for post in ou.Post.post_instances]
        for post in local_post_list:
            post.delete_object()

    if ou.Comment.comment_instances:
        local_comment_list = [comment for comment in ou.Comment.comment_instances]
        for comment in local_comment_list:
            comment.delete_object()

    if ou.Todo.todo_instances:
        local_todo_list = [todo for todo in ou.Todo.todo_instances]
        for todo in local_todo_list:
            todo.delete_object()