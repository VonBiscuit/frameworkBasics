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
            for entry in default_entries['posts']:
                entry["user_id"] = ou.User.user_instances[0].id
                test_post = ou.Post(entry)
                test_post.create_object()
        elif data_type == "comments":
            for entry in default_entries['comments']:
                entry["email"] = generate_random_email()
                entry["post_id"] = ou.Post.post_instances[0].post_id
                test_comment = ou.Comment(entry)
                test_comment.create_object()
        elif data_type == "todos":
            for entry in default_entries['todos']:
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


default_entries = {
    "users": [
        {"name": "test_name", "gender": "male", "email": generate_random_email(), "status": "active"},
        {"name": "Ekaaksh Gowda", "email": generate_random_email(), "gender": "male", "status": "inactive"},
        {"name": "Aagam Chaturvedi", "email": generate_random_email(), "gender": "female", "status": "inactive"},
        {"name": "Aasa Adiga", "email": generate_random_email(), "gender": "female", "status": "inactive"},
        {"name": "Deeptiman Ahuja III", "email": generate_random_email(), "gender": "male", "status": "active"},
        {"name": "Ekalavya Rana", "email": generate_random_email(), "gender": "female", "status": "active"},
        {"name": "Sujata Shukla", "email": generate_random_email(), "gender": "female", "status": "inactive"},
        {"name": "Sher Jain", "email": generate_random_email(), "gender": "female", "status": "active"},
        {"name": "Rohana Butt", "email": generate_random_email(), "gender": "male", "status": "inactive"},
        {"name": "Chitrangada Menon", "email": generate_random_email(), "gender": "female", "status": "active"}],
    "posts": [
        {"user_id": 3274, "title": "Vivo arcus uter veritatis utrimque.", "body": "Non aro vulgo."},
        {"user_id": 3275, "title": "Absum harum decet vinum vulgivagus ut vorago atavus thesis ut vicinus.",
         "body": "Suppellex adnuo reiciendis. Vergo acsi demonstro. Comes placeat delinquo. Trucido error speciosus. "
                 "Caelum sunt asperiores. Vesco traho qui. Quia conor appositus. Amita ex veritas. Ante tergum "
                 "nostrum. Infit illum advoco. Vestigium provident cervus. Officia contigo degusto. Creber caecus "
                 "defessus. Amicitia tracto coerceo. At tumultus eaque. Depono dapifer varius. Vulgivagus enim "
                 "subnecto."},
        {"user_id": 3272, "title": "Id vel desolo sapiente caelestis conduco voluptatem curvus carmen.",
         "body": "Unde conventus tantillus. Ubi cohibeo quas. Adipisci timidus peccatus. Vorago vitium taceo. Curso "
                 "aiunt viduo. Curo tabesco tenetur. Tutis acer occaecati. Deputo vel crinis. Ager trado asper. "
                 "Tepidus conventus currus. Virtus statua canto. Arma nisi tenus. Cruentus depopulo et. Adduco "
                 "impedit vespillo. Laudantium capillus atqui. Aut pecunia comitatus."},
        {"user_id": 3272,
         "title": "Civitas calco ut teres debitis magni canis aut culpa ago adflicto adipiscor apud ipsa "
                  "reprehenderit tero spectaculum depromo.",
         "body": "Acsi volutabrum eum. Barba decet conduco. Virga tumultus articulus. Denuncio tabesco solutio. "
                 "Supplanto maxime adeptio. Titulus subvenio crepusculum. Torrens deporto textor. Synagoga tabella "
                 "defungo. Solitudo aspicio terebro. Credo defero subvenio. Carcer vorax solitudo. Somniculosus est "
                 "terra. Vae confero templum. Decet adduco calculus. Cibus cumque demergo. Clarus tamquam timidus. "
                 "Blandior caput tergum. Stips utique abscido. Tam volubilis bonus."},
        {"user_id": 3271, "title": "Quae deserunt compello vorago utroque cena arguo crapula.",
         "body": "Ciminatio cornu aveho. Supra optio clam. Substantia ut colo. Ullus quo consequatur. Claudeo "
                 "suppellex sed. Quibusdam suffoco theca. Sollicito et consuasor. Soluta consequuntur omnis. "
                 "Atrocitas facilis alioqui. Aut vel administratio. Amaritudo conventus cervus. Comprehendo arx qui. "
                 "Cubitum cruciamentum demitto. Caritas animadverto acervus. Defessus degenero adopto. Illo tutamen "
                 "vel."},
        {"user_id": 3270,
         "title": "Deprimo possimus sit tepidus taedium vulgo deludo complectus sub artificiose veniam dolores "
                  "accusator ultra stultus tunc minima studio.",
         "body": "Blanditiis pectus casus. Laudantium cresco succedo. Voluptas verbum vergo. Valetudo deporto "
                 "conturbo. Theca tremo nihil. Tondeo ambitus acerbitas. Sit umerus vereor. Asper speciosus ancilla. "
                 "Textilis vigilo sponte. Infit sed sublime. Commodi temperantia virtus. Thesis vesper ulterius. "
                 "Audacia adfectus consequatur. Conventus creptio currus. Aperio colloco subseco. Balbus culpa "
                 "patrocinor."},
        {"user_id": 3270,
         "title": "Capillus degenero a comis blanditiis officiis adicio sono sed depulso depraedor.",
         "body": "Collum suffoco optio. Crur defaeco voluptatibus. Vestigium bibo animadverto. Copiose taceo sponte. "
                 "Non conturbo ex. Voluptates voluntarius sursum. Omnis tonsor stabilis. Consectetur ustulo civitas. "
                 "Sodalitas curriculum vicinus. Video aestivus concido. Trans rerum voluptas. Consuasor animus cado. "
                 "Depereo coadunatio vito. Verus conor adimpleo. Vespillo solium aetas. Defigo deduco votum. Admoneo "
                 "tempora aperte. Arceo tamen similique."},
        {"user_id": 3267, "title": "Tricesimus alienus sed placeat copia vinculum vox.",
         "body": "Cum defigo cattus. Confido inventore delinquo. Assumenda admiratio adhaero. Molestias corrupti "
                 "collum. Antiquus beatae vapulus. Carmen repellat placeat. Aliquid sursum esse. Curo talis carcer. "
                 "Trucido thermae voluptatum. Qui eius vinco. Thalassinus tabula colligo. Cupio et audio. Adsidue "
                 "bellum summisse. Suscipio architecto verecundia. Utroque aut canonicus. Abstergo sublime strenuus."},
        {"user_id": 3262,
         "title": "Vitae sunt comes animi tabesco confero officia cursus peior vinculum ut coepi abstergo cena "
                  "articulus cribro.",
         "body": "Neque turpis vulpes. Attollo sonitus compono. Nihil aggero voluptates. Sono perferendis sint. "
                 "Considero somnus constans. Balbus aedificium voluptatem. Solio templum annus. Et alioqui "
                 "comprehendo. Attero conservo tyrannus. Condico crudelis autem. Tandem caelestis civitas. Cui cunae "
                 "doloribus. Commodo veritatis adhuc. Totam tripudio textor. Bellum et sed. Conatus aut "
                 "tergiversatio. Delectatio debilito aliquid."}],
    "comments": [
        {"post_id": 1688, "name": "Prof. Veda Varrier", "email": generate_random_email(),
         "body": "In velitus earum. Velit odit et."},
        {"post_id": 1607, "name": "Tara Iyer II", "email": generate_random_email(),
         "body": "Nostrum qui doloribus."},
        {"post_id": 1607, "name": "Prasad Ahuja", "email": generate_random_email(),
         "body": "Eveniet facere ea. Atque voluptas ut."},
        {"post_id": 1598, "name": "The Hon. Kama Prajapat", "email": generate_random_email(),
         "body": "Distinctio sunt repellendus. Deserunt amet delectus."},
        {"post_id": 1598, "name": "Jagmeet Abbott", "email": generate_random_email(),
         "body": "Soluta consequatur ex. Doloribus vitae modi. Sunt quaerat similique."},
        {"post_id": 1595, "name": "Malti Kaniyar", "email": generate_random_email(),
         "body": "Dolorem praesentium eos. Sed et ducimus. Provident modi rerum. Aliquid maiores maxime."},
        {"post_id": 1594, "name": "Prathamesh Nehru VM", "email": generate_random_email(),
         "body": "Corrupti mollitia dolor. Itaque minima sit. Consequatur ut numquam."},
        {"post_id": 1594, "name": "Dr. Shrishti Nambeesan", "email": generate_random_email(),
         "body": "Possimus modi aut."}],
    "todos": [
        {"user_id": 3304, "title": "Decerno deleo sapiente tepidus talio.",
         "due_on": "2022-07-19T00:00:00.000+05:30", "status": "completed"},
        {"user_id": 3271, "title": "Summisse coaegresco totidem trans aut tamquam.",
         "due_on": "2022-08-10T00:00:00.000+05:30", "status": "completed"},
        {"user_id": 3266, "title": "Contra cena sit testimonium stabilis volo ut abeo vinco.",
         "due_on": "2022-08-01T00:00:00.000+05:30", "status": "completed"},
        {"user_id": 3264, "title": "Textor quis ascisco creator uredo cruciamentum volva vomito minima capillus.",
         "due_on": "2022-08-13T00:00:00.000+05:30", "status": "pending"},
        {"user_id": 3263, "title": "Taedium dolores cena sortitus admoveo depulso ademptio ultra.",
         "due_on": "2022-08-27T00:00:00.000+05:30", "status": "pending"},
        {"user_id": 3261, "title": "Magnam coepi alias sursum amoveo crebro.",
         "due_on": "2022-08-14T00:00:00.000+05:30", "status": "completed"},
        {"user_id": 3259, "title": "Adhaero comburo anser magni assumenda quo est.",
         "due_on": "2022-08-21T00:00:00.000+05:30", "status": "completed"}]}


class TestUsers:

    @pytest.mark.parametrize("user_info", [
        pytest.param("test_data/users/create_user.toml")
    ])
    def test_correct_status_create(self, user_info):
        data_to_load = toml.load(user_info)
        for to_create in data_to_load["to_create"]:
            to_create["email"] = generate_random_email()
            test_user = ou.User(to_create)
            result_first = test_user.create_object()
            assert result_first.status_code == 201

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/update_user.toml")])
    def test_correct_status_update(self, user_info):
        toml_parser(file_name=user_info)
        data_to_load = toml.load(user_info)["to_update"]
        for to_update in data_to_load:
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

    @pytest.mark.parametrize("test_user_entry", [pytest.param("test_data/users/create_user.toml")])
    def test_correct_info_remote(self, test_user_entry):
        data_to_load = toml.load(test_user_entry)["to_create"]
        for user in data_to_load:
            user["email"] = generate_random_email()
            test_user = ou.User(user)
            test_user.create_object()
            user['id'] = test_user.id
            result = test_user.get_object()

            expected = user
            assert result.json() == expected

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/create_user.toml")])
    def test_no_duplicate_creation(self, user_info):
        data_to_load = toml.load(user_info)["to_create"]
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

    @pytest.mark.parametrize("user_info_to_update", [pytest.param("test_data/users/update_user.toml")])
    def test_correct_data_after_update(self, user_info_to_update):
        toml_parser(file_name=user_info_to_update)
        to_update = toml.load(user_info_to_update)["to_update"]
        for user in to_update:
            if "email" in user.keys():
                user["email"] = generate_random_email()
            user_to_update = ou.User.user_instances[0]
            user_to_update.update_object(user)
            result = user_to_update.get_object()
            expected = json.loads(user_to_update.as_payload())
            expected["id"] = user_to_update.id
            assert result.json() == expected

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/create_user.toml")])
    def test_correct_data_after_creation(self, user_info):
        to_create = toml.load(user_info)["to_create"]
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

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/standard_entry.toml")])
    def test_update_object_with_invalid_id(self, user_info):
        toml_parser(file_name=user_info)
        valid_id_list = [x.id for x in ou.User.user_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_user = ou.User.user_instances[0]
        proper_id = test_user.id
        test_user.id = invalid_id
        user_info_to_update = {"name": "Hornet"}
        result = test_user.update_object(user_info_to_update)
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

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/update_invalid_names.toml")])
    def test_update_with_invalid_names(self, user_info):
        toml_parser(file_name=user_info)
        to_update_info = toml.load(user_info)["to_update"]
        for update_info in to_update_info:
            test_user = ou.User.user_instances[0]
            result = test_user.update_object(update_info)
            assert result.status_code == 422


    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/invalid_gender.toml")])
    def test_gender_invalid(self, user_info):
        toml_parser(file_name=user_info)
        invalid_creation = toml.load(user_info)["to_create"]
        invalid_update = toml.load(user_info)["to_update"]
        for user_to_create in invalid_creation:
            test_user = ou.User(user_to_create)
            result = test_user.create_object()
            assert result.status_code == 422
        for user_to_update in invalid_update:
            test_user2 = ou.User.user_instances[1]
            result = test_user2.update_object(user_to_update)
            assert result.status_code == 422

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/invalid_status.toml")])
    def test_status_invalid(self, user_info):
        toml_parser(file_name=user_info)
        invalid_creation = toml.load(user_info)["to_create"]
        invalid_update = toml.load(user_info)["to_update"]
        for user_to_create in invalid_creation:
            test_user = ou.User(user_to_create)
            result = test_user.create_object()
            assert result.status_code == 422
        for user_to_update in invalid_update:
            test_user2 = ou.User.user_instances[1]
            result = test_user2.update_object(user_to_update)
            assert result.status_code == 422

    @pytest.mark.parametrize("user_info", [pytest.param("test_data/users/create_invalid_names.toml")])
    def test_create_with_invalid_names(self, user_info):
        to_create_invalid = toml.load(user_info)["to_create"]
        # user_info = {"name": "Georgina Fatima" * 16, "email": generate_random_email(), "gender": "female",
        #              "status": "active"}
        for user in to_create_invalid:
            test_user = ou.User(user)
            result = test_user.create_object()
            assert result.status_code == 422

        # user_info = {"name": ''.join(random.choices(string.ascii_letters + string.digits, k=256)),
        #              "email": generate_random_email(), "gender": "female", "status": "active"}
        # test_user2 = ou.User(user_info)
        # result = test_user2.create_object()
        # assert result.status_code == 422

    # @staticmethod
    # def setup_method():
    #     for entry in default_entries['users']:
    #         test_user = ou.User(entry)
    #         test_user.create_object()

    @staticmethod
    def teardown_method():
        local_list = [user for user in ou.User.user_instances]
        for user in local_list:
            user.delete_object()


class TestPosts:

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/create_post.toml")])
    def test_correct_status_create(self, post_info):
        toml_parser(file_name=post_info)
        data_to_create = toml.load(post_info)["to_create"]
        for post in data_to_create:
            post["user_id"] = ou.User.user_instances[0].id
            test_post = ou.Post(post)
            result = test_post.create_object()
            assert result.status_code == 201

    @pytest.mark.parametrize("post_update_info", [pytest.param("test_data/posts/update_post.toml")])
    def test_correct_status_update(self, post_update_info):
        toml_parser(file_name=post_update_info)
        to_update = toml.load(post_update_info)["to_update"]
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

    @pytest.mark.parametrize("post_info_to_update", [pytest.param("test_data/posts/update_post.toml")])
    def test_correct_data_after_update(self, post_info_to_update):
        toml_parser(file_name=post_info_to_update)
        to_update = toml.load(post_info_to_update)["to_update"]
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
        to_create = toml.load(post_info)["to_create"]
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

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/standard_entry.toml")])
    def test_update_object_with_invalid_id(self, post_info):
        toml_parser(file_name=post_info)
        valid_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_post = ou.Post.post_instances[0]
        proper_id = test_post.post_id
        test_post.post_id = invalid_id
        post_info_to_update = {"title": "Hornet"}
        result = test_post.update_object(post_info_to_update)
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

    @pytest.mark.parametrize("post_info", [pytest.param("test_data/posts/create_invalid_user_id.toml")])
    def test_create_with_invalid_user_id(self, post_info):
        toml_parser(file_name=post_info)
        post_to_create = toml.load(post_info)["to_create"]
        valid_user_id_list = [x.id for x in ou.User.user_instances]
        for post in post_to_create:
            invalid_user_id = generate_invalid_id(valid_user_id_list)
            post["user_id"] = invalid_user_id
            test_post = ou.Post(post)
            result = test_post.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("post_info_to_update", [pytest.param("test_data/posts/update_invalid_user_id.toml")])
    def test_update_with_invalid_user_id(self, post_info_to_update):
        toml_parser(file_name=post_info_to_update)
        data_to_update = toml.load(post_info_to_update)["to_update"]
        valid_user_id_list = [x.id for x in ou.User.user_instances]
        for post in data_to_update:
            invalid_user_id = generate_invalid_id(valid_user_id_list)
            post["user_id"] = invalid_user_id
            test_post = ou.Post.post_instances[0]
            proper_id = test_post.post_id
            result = test_post.update_object(post)
            test_post.post_id = proper_id
            assert result.status_code == 422

    #     @staticmethod
    #     def setup_method():
    #         for entry in default_entries['users']:
    #             test_user = ou.User(entry)
    #             test_user.create_object()
    #         for entry in default_entries['posts']:
    #             entry["user_id"] = ou.User.user_instances[0].id
    #             test_post = ou.Post(entry)
    #             test_post.create_object()
    #
    @staticmethod
    def teardown_method():
        local_user_list = [user for user in ou.User.user_instances]
        for user in local_user_list:
            user.delete_object()
        local_post_list = [post for post in ou.Post.post_instances]
        for post in local_post_list:
            post.delete_object()


class TestComments:

    # @pytest.mark.parametrize("toml_file",[
    #     pytest.param("test_data/comments/standard_entry.toml")
    # ])
    # def test_toml_function(self,toml_file):
    #     toml_parser(file_name=toml_file)
    #     result_users = ou.User.user_instances[0].get_multiple_objects()
    #     result_posts = ou.Post.post_instances[0].get_multiple_objects()
    #     result_comments = ou.Comment.comment_instances[0].get_multiple_objects()
    #
    #     object_users = []
    #     for user in ou.User.user_instances:
    #         entry = json.loads(user.as_payload())
    #         entry['id'] = user.id
    #         object_users.append(entry)
    #     assert object_users.sort(key=lambda x: x['name'],reverse=False) == result_users.json().sort(key=lambda x: x['name'],reverse=False)
    #
    #     object_posts = []
    #     for post in ou.Post.post_instances:
    #         entry = json.loads(post.as_payload())
    #         entry['id'] = post.post_id
    #         object_posts.append(entry)
    #     assert object_posts.sort(key=lambda x: x['id'], reverse=False) == result_posts.json().sort(
    #         key=lambda x: x['id'], reverse=False)
    #
    #     object_comments = []
    #     for comment in ou.Comment.comment_instances:
    #         entry = json.loads(comment.as_payload())
    #         entry['id'] = comment.comment_id
    #         object_comments.append(entry)
    #     assert object_comments.sort(key=lambda x: x['id'], reverse=False) == result_comments.json().sort(
    #         key=lambda x: x['id'], reverse=False)

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/create_comment.toml")])
    def test_correct_status_create(self, comment_info):
        toml_parser(file_name=comment_info)
        to_create = toml.load(comment_info)["to_create"]
        for comment in to_create:
            comment["email"] = generate_random_email()
            comment["post_id"] = ou.Post.post_instances[0].post_id
            test_comment = ou.Comment(comment)
            result = test_comment.create_object()
            assert result.status_code == 201

    @pytest.mark.parametrize("comment_update_info", [pytest.param("test_data/comments/update_comment.toml")])
    def test_correct_status_update(self, comment_update_info):
        toml_parser(file_name=comment_update_info)
        to_update = toml.load(comment_update_info)["to_update"]
        # comment_update_info = {"body": "Not on my watch."}
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

    @pytest.mark.parametrize("comment_info_to_update", [pytest.param("test_data/comments/update_comment.toml")])
    def test_correct_data_after_update(self, comment_info_to_update):
        toml_parser(file_name=comment_info_to_update)
        to_update = toml.load(comment_info_to_update)["to_update"]
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
        # comment_info = {"post_id": ou.Post.post_instances[0].post_id, "name": "Prasad Ahuja",
        #                 "email": generate_random_email(),
        #                 "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        toml_parser(file_name=comment_info)
        to_create = toml.load(comment_info)["to_create"]
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

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/update_comment.toml")])
    def test_update_object_with_invalid_id(self, comment_info):
        toml_parser(file_name=comment_info)
        to_update = toml.load(comment_info)["to_update"]
        valid_id_list = [x.comment_id for x in ou.Comment.comment_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        for comment in to_update:
            test_comment = ou.Comment.comment_instances[0]
            proper_id = test_comment.comment_id
            test_comment.comment_id = invalid_id
            comment_info_to_update = {"name": "Hornet"}
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

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/create_invalid_post_id.toml")])
    def test_create_with_invalid_post_id(self, comment_info):
        toml_parser(file_name=comment_info)
        comments_to_create = toml.load(comment_info)["to_create"]
        valid_post_id_list = [x.post_id for x in ou.Post.post_instances]
        for to_create in comments_to_create:
            invalid_post_id = generate_invalid_id(valid_post_id_list)
            # comment_info = {"post_id": invalid_post_id, "name": "Prasad Ahuja",
            #                 "email": generate_random_email(),
            #                 "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
            to_create["post_id"] = invalid_post_id
            to_create["email"] = generate_random_email()
            test_comment = ou.Comment(to_create)
            result = test_comment.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/update_invalid_post_id.toml")])
    def test_update_with_invalid_post_id(self, comment_info):
        toml_parser(file_name=comment_info)
        comments_to_update = toml.load(comment_info)["to_update"]
        valid_post_id_list = [x.post_id for x in ou.Post.post_instances]
        for comment in comments_to_update:
            invalid_post_id = generate_invalid_id(valid_post_id_list)
            # comment_info = {"post_id": invalid_post_id}
            comment["post_id"] = invalid_post_id
            test_comment = ou.Comment.comment_instances[0]
            proper_id = test_comment.comment_id
            result = test_comment.update_object(comment)
            test_comment.comment_id = proper_id
            assert result.status_code == 422

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/create_invalid_name.toml")])
    def test_create_with_invalid_names(self, comment_info):
        toml_parser(file_name=comment_info)
        to_create = toml.load(comment_info)["to_create"]
        # comment_info = {"post_id": ou.Post.post_instances[0].post_id, "name": "Georgina Fatima" * 16,
        #                 "email": generate_random_email(),
        #                 "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        for comment in to_create:
            comment["email"] = generate_random_email()
            comment["post_id"] = ou.Post.post_instances[0].post_id
            test_comment = ou.Comment(comment)
            result = test_comment.create_object()
            assert result.status_code == 422

        # comment_info = {"post_id": ou.Post.post_instances[0].post_id,
        #                 "name": ''.join(random.choices(string.ascii_letters + string.digits, k=256)),
        #                 "email": generate_random_email(),
        #                 "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        # test_comment2 = ou.Comment(comment_info)
        # result = test_comment2.create_object()
        # assert result.status_code == 422

    @pytest.mark.parametrize("comment_info", [pytest.param("test_data/comments/update_invalid_name.toml")])
    def test_update_with_invalid_names(self, comment_info):
        toml_parser(file_name=comment_info)
        to_update = toml.load(comment_info)["to_update"]
        # to_update_info = {"name": "Georgina Fatima" * 16}
        for update in to_update:
            test_comment = ou.Comment.comment_instances[0]
            result = test_comment.update_object(update)
            assert result.status_code == 422

            # to_update_info = {"name": ''.join(random.choices(string.ascii_letters + string.digits, k=256))}
            # test_comment2 = ou.Comment.comment_instances[1]
            # result = test_comment2.update_object(to_update_info)
            # assert result.status_code == 422
    #
    #     # @staticmethod
    #     # def setup_method():
    #     #     for entry in default_entries['users']:
    #     #         test_user = ou.User(entry)
    #     #         test_user.create_object()
    #     #     for entry in default_entries['posts']:
    #     #         entry["user_id"] = ou.User.user_instances[0].id
    #     #         test_post = ou.Post(entry)
    #     #         test_post.create_object()
    #     #     for entry in default_entries['comments']:
    #     #         entry["post_id"] = ou.Post.post_instances[0].post_id
    #     #         test_comment = ou.Comment(entry)
    #     #         test_comment.create_object()
    #
    @staticmethod
    def teardown_method():
        local_user_list = [user for user in ou.User.user_instances]
        for user in local_user_list:
            user.delete_object()
        local_post_list = [post for post in ou.Post.post_instances]
        for post in local_post_list:
            post.delete_object()
        local_comment_list = [comment for comment in ou.Comment.comment_instances]
        for comment in local_comment_list:
            comment.delete_object()

        local_todo_list = [todo for todo in ou.Todo.todo_instances]
        for todo in local_todo_list:
            todo.delete_object()


class TestTodos:
    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/create_todo.toml")])
    def test_correct_status_create(self,todo_info):
        toml_parser(file_name=todo_info)
        to_create = toml.load(todo_info)["to_create"]
        for todo in to_create:
            todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo(todo)
            result = test_todo.create_object()
            assert result.status_code == 201

    @pytest.mark.parametrize("todo_update_info", [pytest.param("test_data/todos/update_todo.toml")])
    def test_correct_status_update(self,todo_update_info):
        toml_parser(file_name=todo_update_info)
        to_update = toml.load(todo_update_info)["to_update"]
        for todo in to_update:
            if "user_id" in todo.keys():
                todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo.todo_instances[0]
            result = test_todo.update_object(todo)
            assert result.status_code == 200

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_correct_status_get(self,todo_info):
        toml_parser(file_name=todo_info)
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.get_object()
        assert result.status_code == 200

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_correct_status_delete(self,todo_info):
        toml_parser(file_name=todo_info)
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.delete_object()
        assert result.status_code == 204

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_inaccessible_after_delete(self,todo_info):
        toml_parser(file_name=todo_info)
        todo_to_delete = ou.Todo.todo_instances[0]
        todo_to_delete.delete_object()
        result = todo_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("todo_info_to_update", [pytest.param("test_data/todos/update_todo.toml")])
    def test_correct_data_after_update(self,todo_info_to_update):
        toml_parser(file_name=todo_info_to_update)
        to_update = toml.load(todo_info_to_update)["to_update"]
        # todo_info_to_update = {"title": "Hornet"}
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
    def test_correct_data_after_creation(self,todo_info):
        # todo_info = {"user_id": ou.User.user_instances[0].id,
        #              "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
        #              "due_on": "2022-08-14T00:00:00.000+05:30", "status": "completed"}
        toml_parser(file_name=todo_info)
        to_create = toml.load(todo_info)["to_create"]
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

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_update_object_with_invalid_id(self,todo_info):
        toml_parser(file_name=todo_info)
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_todo = ou.Todo.todo_instances[0]
        proper_id = test_todo.todo_id
        test_todo.todo_id = invalid_id
        user_info_to_update = {"title": "Hornet"}
        result = test_todo.update_object(user_info_to_update)
        test_todo.todo_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/standard_entry.toml")])
    def test_delete_object_with_invalid_id(self,todo_info):
        toml_parser(file_name=todo_info)
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_todo = ou.Todo.todo_instances[0]
        proper_id = test_todo.todo_id
        test_todo.todo_id = invalid_id
        result = test_todo.delete_object()
        test_todo.todo_id = proper_id
        assert result.status_code == 404

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/create_invalid_user_id.toml")])
    def test_create_todo_with_invalid_user_id(self,todo_info):
        toml_parser(file_name=todo_info)
        to_create = toml.load(todo_info)["to_create"]
        valid_user_id_list = [x.id for x in ou.User.user_instances]
        for todo in to_create:
            invalid_id = generate_invalid_id(valid_user_id_list)
            todo["user_id"]=invalid_id
            # todo_info = {"user_id": invalid_id,
            #              "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
            #              "due_on": "2022-08-14T00:00:00.000+05:30", "status": "completed"}
            test_todo = ou.Todo(todo)
            result = test_todo.create_object()
            assert result.status_code == 422


    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/create_invalid_status.toml")])
    def test_create_invalid_status(self,todo_info):
        # todo_info = {"user_id": ou.User.user_instances[0].id,
        #              "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
        #              "due_on": "2022-08-14T00:00:00.000+05:30", "status": "macarena"}
        toml_parser(file_name=todo_info)
        to_create = toml.load(todo_info)["to_create"]
        for todo in to_create:
            todo["user_id"]= ou.User.user_instances[0].id
            test_todo = ou.Todo(todo)
            result = test_todo.create_object()
            assert result.status_code == 422

    @pytest.mark.parametrize("todo_info", [pytest.param("test_data/todos/update_invalid_status.toml")])
    def test_update_invalid_status(self,todo_info):
        toml_parser(file_name=todo_info)
        to_update = toml.load(todo_info)["to_update"]
        # todo_info = {"status": "macarena"}
        for todo in to_update:
            if "user_id" in todo.keys():
                todo["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo.todo_instances[0]
            result = test_todo.update_object(todo)
            assert result.status_code == 422

#     @staticmethod
#     def setup_method():
#         for entry in default_entries['users']:
#             test_user = ou.User(entry)
#             test_user.create_object()
#         for entry in default_entries['todos']:
#             entry["user_id"] = ou.User.user_instances[0].id
#             test_todo = ou.Todos(entry)
#             test_todo.create_object()
#
    @staticmethod
    def teardown_method():
        local_user_list = [user for user in ou.User.user_instances]
        for user in local_user_list:
            user.delete_object()
        local_todo_list = [todo for todo in ou.Todo.todo_instances]
        for todo in local_todo_list:
            todo.delete_object()
