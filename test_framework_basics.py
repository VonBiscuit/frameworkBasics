import pytest
import object_utils as ou
import random
import string
import json
import toml


def toml_parser(file_name):
    data_to_load = toml.load(file_name)
    data_types = list(data_to_load.keys())
    for data_type in data_types:
        if data_type == "users":
            for entry in data_to_load['users']:
                entry["email"] = generate_random_email()
                test_user = ou.User(entry)
                test_user.create_object()
        elif data_type == "posts":
            for entry in data_to_load['posts']:
                entry["user_id"] = ou.User.user_instances[0].id
                test_post = ou.Post(entry)
                test_post.create_object()
        elif data_type == "comments":
            for entry in data_to_load['comments']:
                entry["email"] = generate_random_email()
                entry["post_id"] = ou.Post.post_instances[0].post_id
                test_comment = ou.Comment(entry)
                test_comment.create_object()
        elif data_type == "todos":
            for entry in data_to_load['todos']:
                entry["user_id"] = ou.User.user_instances[0].id
                test_todo = ou.Todo(entry)
                test_todo.create_object()


def generate_random_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20)) + "@" + \
           ''.join(random.choices(string.ascii_letters + string.digits, k=16)) + ".example.com"


def generate_invalid_id(valid_id_list):
    invalid_id = valid_id_list[-1]
    while invalid_id in valid_id_list:
        invalid_id = valid_id_list[-1] + 10 if valid_id_list[-1] + 10 not in valid_id_list else valid_id_list[-1] + 100
    return invalid_id


class TestUsers:

    def test_correct_status_create(self):

        data_to_load = [
            {
                "name": "Bhaasvan Pilla IV",
                "email": "",
                "gender": "female",
                "status": "inactive"
            }
        ]

        for to_create in data_to_load:
            to_create["email"] = generate_random_email()
            test_user = ou.User(to_create)
            result_first = test_user.create_object()
            assert result_first.status_code == 201

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/small_size_entry.toml")])
    def test_correct_status_update(self, user_info):

        toml_parser(file_name=user_info)
        data_to_load = [
            {"name": "Hornet"},
            {"email": generate_random_email()},
            {"gender": "female"},
            {"status": "inactive"}
        ]

        for to_update in data_to_load:
            if "email" in to_update.keys():
                to_update["email"] = generate_random_email()
            test_user = ou.User.user_instances[0]
            result = test_user.update_object(to_update)
            assert result.status_code == 200

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/standard_entry.toml")])
    def test_correct_status_get(self, user_info):

        toml_parser(file_name=user_info)
        user_to_get = ou.User.user_instances[0]
        result = user_to_get.get_object()
        assert result.status_code == 200

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/standard_entry.toml")])
    def test_correct_status_delete(self, user_info):

        toml_parser(file_name=user_info)
        user_to_delete = ou.User.user_instances[0]
        result = user_to_delete.delete_object()
        assert result.status_code == 204

    def test_correct_info_remote(self):

        data_to_load = [
            {
                "name": "Bhaasvan Pilla IV",
                "email": "",
                "gender": "female",
                "status": "inactive"
            }
        ]

        for user in data_to_load:
            user["email"] = generate_random_email()
            test_user = ou.User(user)
            test_user.create_object()
            user['id'] = test_user.id
            result = test_user.get_object()
            expected = user
            assert result.json() == expected

    def test_no_duplicate_creation(self):

        data_to_load = [
            {
                "name": "Bhaasvan Pilla IV",
                "email": "",
                "gender": "female",
                "status": "inactive"
            }
        ]

        for user in data_to_load:
            user["email"] = generate_random_email()
            test_user = ou.User(user)
            result_first = test_user.create_object()
            assert result_first.status_code == 201
            result_second = test_user.create_object()
            assert result_second.status_code == 422

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/standard_entry.toml")])
    def test_inaccessible_after_delete(self, user_info):

        toml_parser(file_name=user_info)
        user_to_delete = ou.User.user_instances[0]
        user_to_delete.delete_object()
        result = user_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("user_info_to_update", [pytest.param("test_data/users/small_size_entry.toml")])
    def test_correct_data_after_update(self, user_info_to_update):

        toml_parser(file_name=user_info_to_update)
        to_update = [
            {"name": "Hornet"},
            {"email": "test@test.com"},
            {"gender": "female"},
            {"status": "inactive"}
        ]

        for user in to_update:
            if "email" in user.keys():
                user["email"] = generate_random_email()
            user_to_update = ou.User.user_instances[0]
            user_to_update.update_object(user)
            result = user_to_update.get_object()
            expected = json.loads(user_to_update.as_payload())
            expected["id"] = user_to_update.id
            assert result.json() == expected

    def test_correct_data_after_creation(self):

        to_create = [
            {
                "name": "Bhaasvan Pilla IV",
                "email": "",
                "gender": "female",
                "status": "inactive"
            }
        ]

        for user in to_create:
            user["email"] = generate_random_email()
            test_user = ou.User(user)
            test_user.create_object()
            result = test_user.get_object()
            expected = user
            expected["id"] = test_user.id
            assert result.json() == expected

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/standard_entry.toml")])
    def test_get_object_with_invalid_id(self, user_info):

        toml_parser(file_name=user_info)
        valid_id_list = [x.id for x in ou.User.user_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_user = ou.User.user_instances[0]
        proper_id = test_user.id
        test_user.id = invalid_id
        result = test_user.get_object()
        test_user.id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/small_size_entry.toml")])
    def test_update_object_with_invalid_id(self, user_info):

        toml_parser(file_name=user_info)
        to_update = [
            {"name": "Hornet"},
            {"email": "test@test.com"},
            {"gender": "female"},
            {"status": "inactive"}
        ]
        valid_id_list = [x.id for x in ou.User.user_instances]

        for user in to_update:
            invalid_id = generate_invalid_id(valid_id_list)
            test_user = ou.User.user_instances[0]
            proper_id = test_user.id
            test_user.id = invalid_id
            if "email" in user.keys():
                user["email"] = generate_random_email()
            result = test_user.update_object(user)
            test_user.id = proper_id
            assert result.status_code == 404

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/standard_entry.toml")])
    def test_delete_object_with_invalid_id(self, user_info):

        toml_parser(file_name=user_info)
        valid_id_list = [x.id for x in ou.User.user_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_user = ou.User.user_instances[0]
        proper_id = test_user.id
        test_user.id = invalid_id
        # here we just want to check that an invalid id gives 404 but not actually
        # remove the object from the list (so teardown can do that)
        result = test_user.delete_object(from_global_list=False)
        test_user.id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/small_size_entry.toml")])
    def test_update_with_invalid_names(self, user_info):

        toml_parser(file_name=user_info)
        to_update_info = [
            {"name": "Georgina FatimaGeorgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina "
                     "Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima "
                     "Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima "},
            {"name": ""}
        ]

        for update_info in to_update_info:
            test_user = ou.User.user_instances[0]
            result = test_user.update_object(update_info)
            assert result.status_code == 422

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/small_size_entry.toml")])
    def test_gender_invalid(self, user_info):

        toml_parser(file_name=user_info)
        invalid_creation = [
            {
                "name": "Bhaasvan Pilla IV",
                "email": "",
                "gender": "Batman",
                "status": "inactive"
            }
        ]
        invalid_update = [{"gender": "nobinary"}]

        for user_to_create in invalid_creation:
            test_user = ou.User(user_to_create)
            result = test_user.create_object()
            assert result.status_code == 422

        for user_to_update in invalid_update:
            test_user2 = ou.User.user_instances[1]
            result = test_user2.update_object(user_to_update)
            assert result.status_code == 422

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/small_size_entry.toml")])
    def test_status_invalid(self, user_info):

        toml_parser(file_name=user_info)
        invalid_creation = [
            {
                "name": "Bhaasvan Pilla IV",
                "email": "",
                "gender": "female",
                "status": "inactive"
            }
        ]
        invalid_update = [
            {"status": "hoping it doesnt work out"}
        ]

        for user_to_create in invalid_creation:
            test_user = ou.User(user_to_create)
            result = test_user.create_object()
            assert result.status_code == 422

        for user_to_update in invalid_update:
            test_user2 = ou.User.user_instances[1]
            result = test_user2.update_object(user_to_update)
            assert result.status_code == 422

    def test_create_with_invalid_names(self):

        to_create_invalid = [
            {
                "name": "Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina "
                        "Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima "
                        "Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima",
                "email": "",
                "gender": "female",
                "status": "active"
            },
            {
                "name": "",
                "email": "",
                "gender": "female",
                "status": "active"
            }
        ]

        for user in to_create_invalid:
            test_user = ou.User(user)
            result = test_user.create_object()
            assert result.status_code == 422


class TestPosts:

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/create_post.toml")])
    def test_correct_status_create(self, post_info):

        toml_parser(file_name=post_info)
        data_to_create = [
            {
                "user_id": "",
                "title": "Vitiosus voluptate quia sollicito nostrum cibo.",
                "body": "Absconditus uppellex tot. Certe dolor spero. Debitis trans onqueror."
            }
        ]

        for post in data_to_create:
            post["user_id"] = ou.User.user_instances[0].id
            test_post = ou.Post(post)
            result = test_post.create_object()
            assert result.status_code == 201

    @pytest.mark.parametrize("post_update_info", [pytest.param("test_data/posts/small_size_entry.toml")])
    def test_correct_status_update(self, post_update_info):

        toml_parser(file_name=post_update_info)
        to_update = [
            {"title": "Not on my watch."},
            {"user_id": ""},
            {"body": "Cum defigo cattus. Confido inventore delinquo. Assumenda admiratio adhaero. Molestias corrupti "
                     "collum. Antiquus beatae vapulus. Suscipio architecto verecundia. Utroque aut canonicus. "
                     "Abstergo sublime strenuus. "}
        ]

        for post in to_update:
            if "user_id" in post.keys():
                post["user_id"] = ou.User.user_instances[0].id
            test_post = ou.Post.post_instances[0]
            result = test_post.update_object(post)
            assert result.status_code == 200

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/standard_entry.toml")])
    def test_correct_status_get(self, post_info):

        toml_parser(file_name=post_info)
        post_to_get = ou.Post.post_instances[0]
        result = post_to_get.get_object()
        assert result.status_code == 200

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/standard_entry.toml")])
    def test_correct_status_delete(self, post_info):

        toml_parser(file_name=post_info)
        post_to_delete = ou.Post.post_instances[0]
        result = post_to_delete.delete_object()
        assert result.status_code == 204

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/standard_entry.toml")])
    def test_inaccessible_after_delete(self, post_info):

        toml_parser(file_name=post_info)
        post_to_delete = ou.Post.post_instances[0]
        post_to_delete.delete_object()
        result = post_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("post_info_to_update", [pytest.param("test_data/posts/small_size_entry.toml")])
    def test_correct_data_after_update(self, post_info_to_update):

        toml_parser(file_name=post_info_to_update)
        to_update = [
            {"title": "Not on my watch."},
            {"user_id": ""},
            {"body": "Cum defigo cattus. Confido inventore delinquo. Assumenda admiratio adhaero. Molestias corrupti "
                     "collum. Antiquus beatae vapulus. Suscipio architecto verecundia. Utroque aut canonicus. "
                     "Abstergo sublime strenuus. "}
        ]

        for post in to_update:
            if "user_id" in post.keys():
                post["user_id"] = ou.User.user_instances[0].id
            post_to_update = ou.Post.post_instances[0]
            post_to_update.update_object(post)
            result = post_to_update.get_object()
            expected = json.loads(post_to_update.as_payload())
            expected["id"] = post_to_update.post_id
            assert result.json() == expected

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/create_post.toml")])
    def test_correct_data_after_creation(self, post_info):

        toml_parser(file_name=post_info)
        to_create = [
            {
                "user_id": "",
                "title": "Vitiosus voluptate quia sollicito nostrum cibo.",
                "body": "Absconditus uppellex tot. Certe dolor spero. Debitis trans onqueror."
            }
        ]

        for post in to_create:
            post["user_id"] = ou.User.user_instances[0].id
            test_post = ou.Post(post)
            test_post.create_object()
            result = test_post.get_object()
            expected = post
            expected["id"] = test_post.post_id
            assert result.json() == expected

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/standard_entry.toml")])
    def test_get_object_with_invalid_id(self, post_info):

        toml_parser(file_name=post_info)
        valid_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_post = ou.Post.post_instances[0]
        proper_id = test_post.post_id
        test_post.post_id = invalid_id
        result = test_post.get_object()
        test_post.post_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/small_size_entry.toml")])
    def test_update_object_with_invalid_id(self, post_info):

        toml_parser(file_name=post_info)
        to_update = [
            {"title": "Not on my watch."},
            {"user_id": ""},
            {"body": "Cum defigo cattus. Confido inventore delinquo. Assumenda admiratio adhaero. Molestias corrupti "
                     "collum. Antiquus beatae vapulus. Suscipio architecto verecundia. Utroque aut canonicus. "
                     "Abstergo sublime strenuus. "}
        ]
        valid_id_list = [x.post_id for x in ou.Post.post_instances]

        for post in to_update:
            invalid_id = generate_invalid_id(valid_id_list)
            test_post = ou.Post.post_instances[0]
            proper_id = test_post.post_id
            test_post.post_id = invalid_id

            if "user_id" in post.keys():
                post["user_id"] = ou.User.user_instances[0].id

            result = test_post.update_object(post)
            test_post.post_id = proper_id
            assert result.status_code == 404

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/standard_entry.toml")])
    def test_delete_object_with_invalid_id(self, post_info):

        toml_parser(file_name=post_info)
        valid_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_post = ou.Post.post_instances[0]
        proper_id = test_post.post_id
        test_post.post_id = invalid_id
        result = test_post.delete_object()
        test_post.post_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/small_size_entry.toml")])
    def test_create_with_invalid_user_id(self, post_info):

        toml_parser(file_name=post_info)
        post_to_create = [
            {
                "user_id": "",
                "title": "Vitiosus voluptate quia sollicito nostrum cibo.",
                "body": "Absconditus suppellex tot. Certe dolor spero. Debitis trans conqueror."
            }
        ]
        valid_user_id_list = [x.id for x in ou.User.user_instances]

        for post in post_to_create:
            invalid_user_id = generate_invalid_id(valid_user_id_list)
            post["user_id"] = invalid_user_id
            test_post = ou.Post(post)
            result = test_post.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("post_info_to_update", [pytest.param("test_data/posts/small_size_entry.toml")])
    def test_update_with_invalid_user_id(self, post_info_to_update):

        toml_parser(file_name=post_info_to_update)
        data_to_update = [
            {"user_id": ""}
        ]
        valid_user_id_list = [x.id for x in ou.User.user_instances]

        for post in data_to_update:
            invalid_user_id = generate_invalid_id(valid_user_id_list)
            post["user_id"] = invalid_user_id
            test_post = ou.Post.post_instances[0]
            proper_id = test_post.post_id
            result = test_post.update_object(post)
            test_post.post_id = proper_id
            assert result.status_code == 422


class TestComments:

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/create_comment.toml")])
    def test_correct_status_create(self, comment_info):

        toml_parser(file_name=comment_info)
        to_create = [
            {
                "post_id": "",
                "name": "Prasad Ahuja",
                "email": "",
                "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."
            }
        ]

        for comment in to_create:
            comment["email"] = generate_random_email()
            comment["post_id"] = ou.Post.post_instances[0].post_id
            test_comment = ou.Comment(comment)
            result = test_comment.create_object()
            assert result.status_code == 201

    @pytest.mark.parametrize("comment_update_info", [pytest.param("test_data/comments/small_size_entry.toml")])
    def test_correct_status_update(self, comment_update_info):

        toml_parser(file_name=comment_update_info)
        to_update = [
            {"body": "Not on my watch."},
            {"name": "Prof. Xavier"},
            {"email": ""}
        ]

        for comment in to_update:
            if "email" in comment.keys():
                comment["email"] = generate_random_email()
            if "post_id" in comment.keys():
                comment["post_id"] = ou.Post.post_instances[0].post_id

            test_comment = ou.Comment.comment_instances[0]
            result = test_comment.update_object(comment)
            assert result.status_code == 200

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/standard_entry.toml")])
    def test_correct_status_get(self, comment_info):

        toml_parser(file_name=comment_info)
        test_comment = ou.Comment.comment_instances[0]
        result = test_comment.get_object()
        assert result.status_code == 200

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/standard_entry.toml")])
    def test_correct_status_delete(self, comment_info):

        toml_parser(file_name=comment_info)
        test_comment = ou.Comment.comment_instances[0]
        result = test_comment.delete_object()
        assert result.status_code == 204

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/standard_entry.toml")])
    def test_inaccessible_after_delete(self, comment_info):

        toml_parser(file_name=comment_info)
        comment_to_delete = ou.Comment.comment_instances[0]
        comment_to_delete.delete_object()
        result = comment_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("comment_info_to_update", [pytest.param("test_data/comments/small_size_entry.toml")])
    def test_correct_data_after_update(self, comment_info_to_update):

        toml_parser(file_name=comment_info_to_update)
        to_update = [
            {"body": "Not on my watch."},
            {"name": "Prof. Xavier"},
            {"email": ""}
        ]

        for comment in to_update:
            if "email" in comment.keys():
                comment["email"] = generate_random_email()
            if "post_id" in comment.keys():
                comment["post_id"] = ou.Post.post_instances[0].post_id

            comment_to_update = ou.Comment.comment_instances[0]
            comment_to_update.update_object(comment)
            result = comment_to_update.get_object()
            expected = json.loads(comment_to_update.as_payload())
            expected["id"] = comment_to_update.comment_id
            assert result.json() == expected

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/create_comment.toml")])
    def test_correct_data_after_creation(self, comment_info):

        toml_parser(file_name=comment_info)
        to_create = [
            {
                "post_id": "",
                "name": "Prasad Ahuja",
                "email": "",
                "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."
            }
        ]

        for comment in to_create:
            comment["email"] = generate_random_email()
            comment["post_id"] = ou.Post.post_instances[0].post_id
            test_comment = ou.Comment(comment)
            test_comment.create_object()
            result = test_comment.get_object()
            expected = comment
            expected["id"] = test_comment.comment_id
            assert result.json() == expected

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/standard_entry.toml")])
    def test_get_object_with_invalid_id(self, comment_info):

        toml_parser(file_name=comment_info)
        valid_id_list = [x.comment_id for x in ou.Comment.comment_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_comment = ou.Comment.comment_instances[0]
        proper_id = test_comment.comment_id
        test_comment.comment_id = invalid_id
        result = test_comment.get_object()
        test_comment.comment_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/small_size_entry.toml")])
    def test_update_object_with_invalid_id(self, comment_info):

        toml_parser(file_name=comment_info)
        to_update = [
            {"body": "Not on my watch."},
            {"name": "Prof. Xavier"},
            {"email": ""}
        ]
        valid_id_list = [x.comment_id for x in ou.Comment.comment_instances]
        invalid_id = generate_invalid_id(valid_id_list)

        for comment in to_update:
            test_comment = ou.Comment.comment_instances[0]
            proper_id = test_comment.comment_id
            test_comment.comment_id = invalid_id
            result = test_comment.update_object(comment)
            test_comment.comment_id = proper_id
            assert result.status_code == 404

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/standard_entry.toml")])
    def test_delete_object_with_invalid_id(self, comment_info):

        toml_parser(file_name=comment_info)
        valid_id_list = [x.comment_id for x in ou.Comment.comment_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_comment = ou.Comment.comment_instances[0]
        proper_id = test_comment.comment_id
        test_comment.comment_id = invalid_id
        result = test_comment.delete_object()
        test_comment.comment_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/small_size_entry.toml")])
    def test_create_with_invalid_post_id(self, comment_info):

        toml_parser(file_name=comment_info)
        comments_to_create = [
            {
                "post_id": "",
                "name": "Prasad Ahuja",
                "email": "",
                "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."
            }
        ]
        valid_post_id_list = [x.post_id for x in ou.Post.post_instances]

        for to_create in comments_to_create:
            invalid_post_id = generate_invalid_id(valid_post_id_list)
            to_create["post_id"] = invalid_post_id
            to_create["email"] = generate_random_email()
            test_comment = ou.Comment(to_create)
            result = test_comment.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/small_size_entry.toml")])
    def test_update_with_invalid_post_id(self, comment_info):

        toml_parser(file_name=comment_info)
        comments_to_update = [
            {"post_id": ""}
        ]
        valid_post_id_list = [x.post_id for x in ou.Post.post_instances]

        for comment in comments_to_update:
            invalid_post_id = generate_invalid_id(valid_post_id_list)
            comment["post_id"] = invalid_post_id
            test_comment = ou.Comment.comment_instances[0]
            proper_id = test_comment.comment_id
            result = test_comment.update_object(comment)
            test_comment.comment_id = proper_id
            assert result.status_code == 422

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/small_size_entry.toml")])
    def test_create_with_invalid_names(self, comment_info):

        toml_parser(file_name=comment_info)
        to_create = [
            {
                "post_id": "",
                "name": "Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina "
                        "Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima "
                        "Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima Georgina Fatima",
                "email": "",
                "body": "That is one long name but i bet it can get longer."
            },
            {
                "post_id": "",
                "name": "",
                "email": "",
                "body": "Draco dormiens nunquam titilandus."
            }
        ]

        for comment in to_create:
            comment["email"] = generate_random_email()
            comment["post_id"] = ou.Post.post_instances[0].post_id
            test_comment = ou.Comment(comment)
            result = test_comment.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/small_size_entry.toml")])
    def test_update_with_invalid_names(self, comment_info):

        toml_parser(file_name=comment_info)
        to_update = [{"name": "Georgina Fatima" * 16},
                     {"name": ''.join(random.choices(string.ascii_letters + string.digits, k=256))}
                     ]

        for update in to_update:
            test_comment = ou.Comment.comment_instances[0]
            result = test_comment.update_object(update)
            assert result.status_code == 422


class TestTodos:
    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/create_todo.toml")])
    def test_correct_status_create(self, todo_info):

        toml_parser(file_name=todo_info)
        to_create = [
            {
                "user_id": "",
                "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
                "due_on": "2022-08-14T00:00:00.000+05:30",
                "status": "completed"
            }
        ]

        for todo in to_create:
            todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo(todo)
            result = test_todo.create_object()
            assert result.status_code == 201

    @pytest.mark.parametrize("todo_update_info", [pytest.param("test_data/todos/small_size_entry.toml")])
    def test_correct_status_update(self, todo_update_info):

        toml_parser(file_name=todo_update_info)
        to_update = [
            {"title": "Not on my watch."},
            {"due_on": "2022-08-14T00:00:00.000+05:30"},
            {"status": "completed"},
            {"user_id": ""}
        ]

        for todo in to_update:
            if "user_id" in todo.keys():
                todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo.todo_instances[0]
            result = test_todo.update_object(todo)
            assert result.status_code == 200

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_correct_status_get(self, todo_info):

        toml_parser(file_name=todo_info)
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.get_object()
        assert result.status_code == 200

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_correct_status_delete(self, todo_info):

        toml_parser(file_name=todo_info)
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.delete_object()
        assert result.status_code == 204

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_inaccessible_after_delete(self, todo_info):

        toml_parser(file_name=todo_info)
        todo_to_delete = ou.Todo.todo_instances[0]
        todo_to_delete.delete_object()
        result = todo_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("todo_info_to_update", [pytest.param("test_data/todos/small_size_entry.toml")])
    def test_correct_data_after_update(self, todo_info_to_update):

        toml_parser(file_name=todo_info_to_update)
        to_update = [
            {"title": "Not on my watch."},
            {"due_on": "2022-08-14T00:00:00.000+05:30"},
            {"status": "completed"},
            {"user_id": ""}
        ]

        for todo in to_update:
            if "user_id" in todo.keys():
                todo["user_id"] = ou.User.user_instances[0].id
            todo_to_update = ou.Todo.todo_instances[0]
            todo_to_update.update_object(todo)
            result = todo_to_update.get_object()
            expected = json.loads(todo_to_update.as_payload())
            expected["id"] = todo_to_update.todo_id
            assert result.json() == expected

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/create_todo.toml")])
    def test_correct_data_after_creation(self, todo_info):

        toml_parser(file_name=todo_info)
        to_create = [
            {
                "user_id": "",
                "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
                "due_on": "2022-08-14T00:00:00.000+05:30",
                "status": "completed"
            }
        ]

        for todo in to_create:
            todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo(todo)
            test_todo.create_object()
            result = test_todo.get_object()
            expected = todo
            expected["id"] = test_todo.todo_id
            assert result.json() == expected

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_get_object_with_invalid_id(self, todo_info):

        toml_parser(file_name=todo_info)
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_todo = ou.Todo.todo_instances[0]
        proper_id = test_todo.todo_id
        test_todo.todo_id = invalid_id
        result = test_todo.get_object()
        test_todo.todo_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/small_size_entry.toml")])
    def test_update_object_with_invalid_id(self, todo_info):

        toml_parser(file_name=todo_info)
        to_update = [
            {"title": "Not on my watch."},
            {"due_on": "2022-08-14T00:00:00.000+05:30"},
            {"status": "completed"},
            {"user_id": ""}
        ]
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]

        for todo in to_update:
            invalid_id = generate_invalid_id(valid_id_list)
            test_todo = ou.Todo.todo_instances[0]
            proper_id = test_todo.todo_id
            test_todo.todo_id = invalid_id

            if "user_id" in todo.keys():
                todo["user_id"] = ou.User.user_instances[0].id

            result = test_todo.update_object(todo)
            test_todo.todo_id = proper_id
            assert result.status_code == 404

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_delete_object_with_invalid_id(self, todo_info):

        toml_parser(file_name=todo_info)
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_todo = ou.Todo.todo_instances[0]
        proper_id = test_todo.todo_id
        test_todo.todo_id = invalid_id
        result = test_todo.delete_object()
        test_todo.todo_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/small_size_entry.toml")])
    def test_create_todo_with_invalid_user_id(self, todo_info):

        toml_parser(file_name=todo_info)
        to_create = [
            {
                "user_id": "",
                "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
                "due_on": "2022-08-14T00:00:00.000+05:30",
                "status": "completed"
            }
        ]
        valid_user_id_list = [x.id for x in ou.User.user_instances]

        for todo in to_create:
            invalid_id = generate_invalid_id(valid_user_id_list)
            todo["user_id"] = invalid_id
            test_todo = ou.Todo(todo)
            result = test_todo.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/small_size_entry.toml")])
    def test_small_size_entry(self, todo_info):

        toml_parser(file_name=todo_info)
        to_create = [
            {
                "user_id": 3271,
                "title": "Summisse coaegresco totidem trans aut tamquam.",
                "due_on": "2022-08-10T00:00:00.000+05:30",
                "status": "Everything will disappear"
            }
        ]

        for todo in to_create:
            todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo(todo)
            result = test_todo.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/small_size_entry.toml")])
    def test_update_invalid_status(self, todo_info):

        toml_parser(file_name=todo_info)
        to_update = [
            {"status": "Polluted filled skies, trying to think clear."}
        ]

        for todo in to_update:
            if "user_id" in todo.keys():
                todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo.todo_instances[0]
            result = test_todo.update_object(todo)
            assert result.status_code == 422
