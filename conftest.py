import object_utils as ou
import pytest


@pytest.fixture(scope="function", autouse=True)
def cleanup_created_objects():

    object_list = []
    object_list += ou.User.user_instances
    object_list += ou.Post.post_instances
    object_list += ou.Comment.comment_instances
    object_list += ou.Todo.todo_instances

    for api_object in object_list:
        api_object.delete_object()
