import pytest
import object_utils as ou
import random
import string
import json
import toml


# def_entries = toml.load("default_entries.toml")
standard_user_entries = toml.load("test_data/users/standard_entry.toml")
create_user_entries = toml.load("test_data/users/create_user.toml")
update_user_entries = toml.load("test_data/users/update_user.toml")

standard_post_entries = toml.load("test_data/posts/standard_entry.toml")
create_post_entries = toml.load("test_data/posts/create_post.toml")
update_post_entries = toml.load("test_data/posts/update_post.toml")

standard_comment_entries = toml.load("test_data/comments/standard_entry.toml")
create_comment_entries = toml.load("test_data/comments/create_comment.toml")
update_comment_entries = toml.load("test_data/comments/update_comment.toml")

standard_todo_entries = toml.load("test_data/todos/standard_entry.toml")
create_todo_entries = toml.load("test_data/todos/create_todo.toml")
update_todo_entries = toml.load("test_data/todos/update_todo.toml")


def print_test_toml():
    # print(def_entries)
    print(standard_user_entries)

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

    @pytest.mark.parametrize("user_info", standard_user_entries["users"])
    def test_correct_status_create(self,user_info):
        # user_info = {"name": "Bhaasvan Pilla IV", "email": generate_random_email(), "gender": "female",
        #              "status": "inactive"}
        user_info["email"] = generate_random_email()
        test_user = ou.User(user_info)
        result_first = test_user.create_object()
        assert result_first.status_code == 201

    @pytest.mark.parametrize("user_info",update_user_entries["users"])
    def test_correct_status_update(self,user_info):
        # user_info = {"email": generate_random_email()}
        if 'email' in user_info.keys():
            user_info["email"] = generate_random_email()
        test_user = ou.User.user_instances[0]
        result = test_user.update_object(user_info)
        assert result.status_code == 200

    def test_correct_status_get(self):
        user_to_get = ou.User.user_instances[0]
        result = user_to_get.get_object()
        assert result.status_code == 200

    def test_correct_status_delete(self):
        user_to_delete = ou.User.user_instances[0]
        result = user_to_delete.delete_object()
        assert result.status_code == 204

    @pytest.mark.parametrize("test_user_entry", standard_user_entries["users"])
    def test_correct_info_remote(self,test_user_entry):
        # test_user_entry = {"name": "Chatura Nambeesan", "email": generate_random_email(), "gender": "male",
        #                    "status": "active"}
        test_user_entry["email"] = generate_random_email()
        test_user = ou.User(test_user_entry)
        test_user.create_object()
        test_user_entry['id'] = test_user.id
        result = test_user.get_object()

        expected = test_user_entry
        assert result.json() == expected

    @pytest.mark.parametrize("user_info", standard_user_entries["users"])
    def test_no_duplicate_creation(self,user_info):
        # user_info = {"name": "Bhaasvan Pilla IV", "email": generate_random_email(), "gender": "female",
        #              "status": "inactive"}
        user_info["email"] = generate_random_email()
        test_user = ou.User(user_info)
        result_first = test_user.create_object()
        assert result_first.status_code == 201
        result_second = test_user.create_object()
        assert result_second.status_code == 422

    def test_inaccessible_after_delete(self):
        user_to_delete = ou.User.user_instances[0]
        user_to_delete.delete_object()
        result = user_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("user_info_to_update", update_user_entries["users"])
    def test_correct_data_after_update(self,user_info_to_update):
        # user_info_to_update = {"name": "Hornet"}
        if "email" in user_info_to_update.keys():
            user_info_to_update["email"] = generate_random_email()
        user_to_update = ou.User.user_instances[0]
        user_to_update.update_object(user_info_to_update)
        result = user_to_update.get_object()
        expected = json.loads(user_to_update.as_payload())
        expected["id"] = user_to_update.id
        assert result.json() == expected

    @pytest.mark.parametrize("user_info", standard_user_entries["users"])
    def test_correct_data_after_creation(self,user_info):
        # user_info = {"name": "Bhaasvan Pilla IV", "email": generate_random_email(), "gender": "female",
        #              "status": "inactive"}
        user_info["email"] = generate_random_email()
        test_user = ou.User(user_info)
        test_user.create_object()
        result = test_user.get_object()
        expected = user_info
        expected["id"] = test_user.id
        assert result.json() == expected

    def test_get_object_with_invalid_id(self):
        valid_id_list = [x.id for x in ou.User.user_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_user = ou.User.user_instances[0]
        proper_id = test_user.id
        test_user.id = invalid_id
        result = test_user.get_object()
        test_user.id = proper_id
        assert result.status_code == 404

    def test_update_object_with_invalid_id(self):
        valid_id_list = [x.id for x in ou.User.user_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_user = ou.User.user_instances[0]
        proper_id = test_user.id
        test_user.id = invalid_id
        user_info_to_update = {"name": "Hornet"}
        result = test_user.update_object(user_info_to_update)
        test_user.id = proper_id
        assert result.status_code == 404

    def test_delete_object_with_invalid_id(self):
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

    def test_update_with_invalid_names(self):
        to_update_info = {"name": "Georgina Fatima" * 16}
        test_user = ou.User.user_instances[0]
        result = test_user.update_object(to_update_info)
        assert result.status_code == 422

        to_update_info = {"name": ''.join(random.choices(string.ascii_letters + string.digits, k=256))}
        test_user2 = ou.User.user_instances[1]
        result = test_user2.update_object(to_update_info)
        assert result.status_code == 422

    def test_gender_invalid(self):
        user_info = {"name": "Bhaasvan Pilla IV", "email": generate_random_email(), "gender": "nonbinary",
                     "status": "inactive"}
        test_user = ou.User(user_info)
        result = test_user.create_object()
        assert result.status_code == 422
        to_update_info = {"gender": "nonbinary"}
        test_user2 = ou.User.user_instances[1]
        result = test_user2.update_object(to_update_info)
        assert result.status_code == 422

    def test_status_invalid(self):
        user_info = {"name": "Bhaasvan Pilla IV", "email": generate_random_email(), "gender": "female",
                     "status": "sleeping"}
        test_user = ou.User(user_info)
        result = test_user.create_object()
        assert result.status_code == 422
        to_update_info = {"status": "hoping it doesnt work out"}
        test_user2 = ou.User.user_instances[1]
        result = test_user2.update_object(to_update_info)
        assert result.status_code == 422

    def test_create_with_invalid_names(self):
        user_info = {"name": "Georgina Fatima" * 16, "email": generate_random_email(), "gender": "female",
                     "status": "active"}
        test_user = ou.User(user_info)
        result = test_user.create_object()
        assert result.status_code == 422

        user_info = {"name": ''.join(random.choices(string.ascii_letters + string.digits, k=256)),
                     "email": generate_random_email(), "gender": "female", "status": "active"}
        test_user2 = ou.User(user_info)
        result = test_user2.create_object()
        assert result.status_code == 422

    @staticmethod
    def setup_method():
        for entry in default_entries['users']:
            test_user = ou.User(entry)
            test_user.create_object()

    @staticmethod
    def teardown_method():
        local_list = [user for user in ou.User.user_instances]
        for user in local_list:
            user.delete_object()


class TestPosts:
    @pytest.mark.parametrize("post_info", standard_post_entries["posts"])
    def test_correct_status_create(self,post_info):
        # post_info = {"user_id": ou.User.user_instances[0].id,
        #              "title": "Vitiosus voluptate quia sollicito nostrum cibo.",
        #              "body": "Absconditus suppellex tot. Certe dolor spero. Debitis trans conqueror."}
        post_info["user_id"] = ou.User.user_instances[0].id
        test_post = ou.Post(post_info)
        result = test_post.create_object()
        assert result.status_code == 201

    @pytest.mark.parametrize("post_update_info", update_post_entries["posts"])
    def test_correct_status_update(self,post_update_info):
        # post_update_info = {"title": "Not on my watch."}
        if "user_id" in post_update_info.keys():
            post_update_info["user_id"] = ou.User.user_instances[0].id
        test_post = ou.Post.post_instances[0]
        result = test_post.update_object(post_update_info)
        assert result.status_code == 200

    def test_correct_status_get(self):
        post_to_get = ou.Post.post_instances[0]
        result = post_to_get.get_object()
        assert result.status_code == 200

    def test_correct_status_delete(self):
        post_to_delete = ou.Post.post_instances[0]
        result = post_to_delete.delete_object()
        assert result.status_code == 204

    def test_inaccessible_after_delete(self):
        post_to_delete = ou.Post.post_instances[0]
        post_to_delete.delete_object()
        result = post_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("post_info_to_update", update_post_entries["posts"])
    def test_correct_data_after_update(self,post_info_to_update):
        # post_info_to_update = {"title": "Hornet"}
        if "user_id" in post_info_to_update.keys():
            post_info_to_update["user_id"] = ou.User.user_instances[0].id
        post_to_update = ou.Post.post_instances[0]
        post_to_update.update_object(post_info_to_update)
        result = post_to_update.get_object()
        expected = json.loads(post_to_update.as_payload())
        expected["id"] = post_to_update.post_id
        assert result.json() == expected

    @pytest.mark.parametrize("post_info", standard_post_entries["posts"])
    def test_correct_data_after_creation(self,post_info):
        # post_info = {"user_id": ou.User.user_instances[0].id,
        #              "title": "Vitiosus voluptate quia sollicito nostrum cibo.",
        #              "body": "Absconditus suppellex tot. Certe dolor spero. Debitis trans conqueror."}
        post_info["user_id"] = ou.User.user_instances[0].id
        test_post = ou.Post(post_info)
        test_post.create_object()
        result = test_post.get_object()
        expected = post_info
        expected["id"] = test_post.post_id
        assert result.json() == expected

    def test_get_object_with_invalid_id(self):
        valid_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_post = ou.Post.post_instances[0]
        proper_id = test_post.post_id
        test_post.post_id = invalid_id
        result = test_post.get_object()
        test_post.post_id = proper_id
        assert result.status_code == 404

    def test_update_object_with_invalid_id(self):
        valid_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_post = ou.Post.post_instances[0]
        proper_id = test_post.post_id
        test_post.post_id = invalid_id
        post_info_to_update = {"title": "Hornet"}
        result = test_post.update_object(post_info_to_update)
        test_post.post_id = proper_id
        assert result.status_code == 404

    def test_delete_object_with_invalid_id(self):
        valid_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_post = ou.Post.post_instances[0]
        proper_id = test_post.post_id
        test_post.post_id = invalid_id
        result = test_post.delete_object()
        test_post.post_id = proper_id
        assert result.status_code == 404

    def test_create_with_invalid_user_id(self):
        valid_user_id_list = [x.id for x in ou.User.user_instances]
        invalid_user_id = generate_invalid_id(valid_user_id_list)
        post_info = {"user_id": invalid_user_id,
                     "title": "Vitiosus voluptate quia sollicito nostrum cibo.",
                     "body": "Absconditus suppellex tot. Certe dolor spero. Debitis trans conqueror."}
        test_post = ou.Post(post_info)
        result = test_post.create_object()
        assert result.status_code == 422

    def test_update_with_invalid_user_id(self):
        valid_user_id_list = [x.id for x in ou.User.user_instances]
        # invalid_user_id = valid_user_id_list[-1] + 10 if valid_user_id_list[-1] + 10 not in valid_user_id_list else \
        #     valid_user_id_list[-1] + 100
        invalid_user_id = generate_invalid_id(valid_user_id_list)
        post_update_info = {"user_id": invalid_user_id}
        test_post = ou.Post.post_instances[0]
        proper_id = test_post.post_id
        result = test_post.update_object(post_update_info)
        test_post.post_id = proper_id
        assert result.status_code == 422

    @staticmethod
    def setup_method():
        for entry in default_entries['users']:
            test_user = ou.User(entry)
            test_user.create_object()
        for entry in default_entries['posts']:
            entry["user_id"] = ou.User.user_instances[0].id
            test_post = ou.Post(entry)
            test_post.create_object()

    @staticmethod
    def teardown_method():
        local_user_list = [user for user in ou.User.user_instances]
        for user in local_user_list:
            user.delete_object()
        local_post_list = [post for post in ou.Post.post_instances]
        for post in local_post_list:
            post.delete_object()


class TestComments:
    @pytest.mark.parametrize("comment_info", standard_comment_entries["comments"])
    def test_correct_status_create(self,comment_info):
        # comment_info = {"post_id": ou.Post.post_instances[0].post_id, "name": "Prasad Ahuja",
        #                 "email": generate_random_email(),
        #                 "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        comment_info["email"] = generate_random_email()
        comment_info["post_id"] = ou.Post.post_instances[0].post_id
        test_comment = ou.Comment(comment_info)
        result = test_comment.create_object()
        assert result.status_code == 201

    @pytest.mark.parametrize("comment_update_info", update_comment_entries["comments"])
    def test_correct_status_update(self,comment_update_info):
        # comment_update_info = {"body": "Not on my watch."}
        if "email" in comment_update_info.keys():
            comment_update_info["email"] = generate_random_email()
        if "post_id" in comment_update_info.keys():
            comment_update_info["post_id"] = ou.Post.post_instances[0].post_id
        test_comment = ou.Comment.comment_instances[0]
        result = test_comment.update_object(comment_update_info)
        assert result.status_code == 200

    def test_correct_status_get(self):
        test_comment = ou.Comment.comment_instances[0]
        result = test_comment.get_object()
        assert result.status_code == 200

    def test_correct_status_delete(self):
        test_comment = ou.Comment.comment_instances[0]
        result = test_comment.delete_object()
        assert result.status_code == 204

    def test_inaccessible_after_delete(self):
        comment_to_delete = ou.Comment.comment_instances[0]
        comment_to_delete.delete_object()
        result = comment_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("comment_info_to_update", update_comment_entries["comments"])
    def test_correct_data_after_update(self,comment_info_to_update):
        # comment_info_to_update = {"email": generate_random_email()}
        if "email" in comment_info_to_update.keys():
            comment_info_to_update["email"] = generate_random_email()
        if "post_id" in comment_info_to_update.keys():
            comment_info_to_update["post_id"] = ou.Post.post_instances[0].post_id
        comment_to_update = ou.Comment.comment_instances[0]
        comment_to_update.update_object(comment_info_to_update)
        result = comment_to_update.get_object()
        expected = json.loads(comment_to_update.as_payload())
        expected["id"] = comment_to_update.comment_id
        assert result.json() == expected

    @pytest.mark.parametrize("comment_info", standard_comment_entries["comments"])
    def test_correct_data_after_creation(self,comment_info):
        # comment_info = {"post_id": ou.Post.post_instances[0].post_id, "name": "Prasad Ahuja",
        #                 "email": generate_random_email(),
        #                 "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        comment_info["email"] = generate_random_email()
        comment_info["post_id"] = ou.Post.post_instances[0].post_id
        test_comment = ou.Comment(comment_info)
        test_comment.create_object()
        result = test_comment.get_object()
        expected = comment_info
        expected["id"] = test_comment.comment_id
        assert result.json() == expected

    def test_get_object_with_invalid_id(self):
        valid_id_list = [x.comment_id for x in ou.Comment.comment_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_comment = ou.Comment.comment_instances[0]
        proper_id = test_comment.comment_id
        test_comment.comment_id = invalid_id
        result = test_comment.get_object()
        test_comment.comment_id = proper_id
        assert result.status_code == 404

    def test_update_object_with_invalid_id(self):
        valid_id_list = [x.comment_id for x in ou.Comment.comment_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_comment = ou.Comment.comment_instances[0]
        proper_id = test_comment.comment_id
        test_comment.comment_id = invalid_id
        comment_info_to_update = {"name": "Hornet"}
        result = test_comment.update_object(comment_info_to_update)
        test_comment.comment_id = proper_id
        assert result.status_code == 404

    def test_delete_object_with_invalid_id(self):
        valid_id_list = [x.comment_id for x in ou.Comment.comment_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_comment = ou.Comment.comment_instances[0]
        proper_id = test_comment.comment_id
        test_comment.comment_id = invalid_id
        result = test_comment.delete_object()
        test_comment.comment_id = proper_id
        assert result.status_code == 404

    def test_create_with_invalid_post_id(self):
        valid_post_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_post_id = generate_invalid_id(valid_post_id_list)
        comment_info = {"post_id": invalid_post_id, "name": "Prasad Ahuja",
                        "email": generate_random_email(),
                        "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        test_comment = ou.Comment(comment_info)
        result = test_comment.create_object()
        assert result.status_code == 422

    def test_update_with_invalid_post_id(self):
        valid_post_id_list = [x.post_id for x in ou.Post.post_instances]
        invalid_post_id = generate_invalid_id(valid_post_id_list)
        comment_info = {"post_id": invalid_post_id}
        test_comment = ou.Comment.comment_instances[0]
        proper_id = test_comment.comment_id
        result = test_comment.update_object(comment_info)
        test_comment.comment_id = proper_id
        assert result.status_code == 422

    def test_create_with_invalid_names(self):
        comment_info = {"post_id": ou.Post.post_instances[0].post_id, "name": "Georgina Fatima" * 16,
                        "email": generate_random_email(),
                        "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        test_comment = ou.Comment(comment_info)
        result = test_comment.create_object()
        assert result.status_code == 422

        comment_info = {"post_id": ou.Post.post_instances[0].post_id,
                        "name": ''.join(random.choices(string.ascii_letters + string.digits, k=256)),
                        "email": generate_random_email(),
                        "body": "Eveniet facere ea. Quasi est molestias. Et dolore facilis."}
        test_comment2 = ou.Comment(comment_info)
        result = test_comment2.create_object()
        assert result.status_code == 422

    def test_update_with_invalid_names(self):
        to_update_info = {"name": "Georgina Fatima" * 16}
        test_comment = ou.Comment.comment_instances[1]
        result = test_comment.update_object(to_update_info)
        assert result.status_code == 422

        to_update_info = {"name": ''.join(random.choices(string.ascii_letters + string.digits, k=256))}
        test_comment2 = ou.Comment.comment_instances[1]
        result = test_comment2.update_object(to_update_info)
        assert result.status_code == 422

    @staticmethod
    def setup_method():
        for entry in default_entries['users']:
            test_user = ou.User(entry)
            test_user.create_object()
        for entry in default_entries['posts']:
            entry["user_id"] = ou.User.user_instances[0].id
            test_post = ou.Post(entry)
            test_post.create_object()
        for entry in default_entries['comments']:
            entry["post_id"] = ou.Post.post_instances[0].post_id
            test_comment = ou.Comment(entry)
            test_comment.create_object()

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


class TestTodos:
    @pytest.mark.parametrize("todo_info", standard_todo_entries["todos"])
    def test_correct_status_create(self,todo_info):
        # todo_info = {"user_id": ou.User.user_instances[0].id,
        #              "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
        #              "due_on": "2022-08-14T00:00:00.000+05:30", "status": "completed"}
        todo_info["user_id"] = ou.User.user_instances[0].id
        test_todo = ou.Todo(todo_info)
        result = test_todo.create_object()
        assert result.status_code == 201

    @pytest.mark.parametrize("todo_update_info", update_todo_entries["todos"])
    def test_correct_status_update(self,todo_update_info):
        # todo_update_info = {"title": "Not on my watch."}
        if "user_id" in todo_update_info.keys():
            todo_update_info["user_id"] = ou.User.user_instances[0].id
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.update_object(todo_update_info)
        assert result.status_code == 200

    def test_correct_status_get(self):
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.get_object()
        assert result.status_code == 200

    def test_correct_status_delete(self):
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.delete_object()
        assert result.status_code == 204

    def test_inaccessible_after_delete(self):
        todo_to_delete = ou.Todo.todo_instances[0]
        todo_to_delete.delete_object()
        result = todo_to_delete.get_object()
        assert result.status_code == 404

    @pytest.mark.parametrize("todo_info_to_update", update_todo_entries["todos"])
    def test_correct_data_after_update(self,todo_info_to_update):
        # todo_info_to_update = {"title": "Hornet"}
        if "user_id" in todo_info_to_update.keys():
            todo_info_to_update["user_id"] = ou.User.user_instances[0].id
        todo_to_update = ou.Todo.todo_instances[0]
        todo_to_update.update_object(todo_info_to_update)
        result = todo_to_update.get_object()
        expected = json.loads(todo_to_update.as_payload())
        expected["id"] = todo_to_update.todo_id
        assert result.json() == expected

    @pytest.mark.parametrize("todo_info", standard_todo_entries["todos"])
    def test_correct_data_after_creation(self,todo_info):
        # todo_info = {"user_id": ou.User.user_instances[0].id,
        #              "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
        #              "due_on": "2022-08-14T00:00:00.000+05:30", "status": "completed"}
        todo_info["user_id"] = ou.User.user_instances[0].id
        test_todo = ou.Todo(todo_info)
        test_todo.create_object()
        result = test_todo.get_object()
        expected = todo_info
        expected["id"] = test_todo.todo_id
        assert result.json() == expected

    def test_get_object_with_invalid_id(self):
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_todo = ou.Todo.todo_instances[0]
        proper_id = test_todo.todo_id
        test_todo.todo_id = invalid_id
        result = test_todo.get_object()
        test_todo.todo_id = proper_id
        assert result.status_code == 404

    def test_update_object_with_invalid_id(self):
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_todo = ou.Todo.todo_instances[0]
        proper_id = test_todo.todo_id
        test_todo.todo_id = invalid_id
        user_info_to_update = {"title": "Hornet"}
        result = test_todo.update_object(user_info_to_update)
        test_todo.todo_id = proper_id
        assert result.status_code == 404

    def test_delete_object_with_invalid_id(self):
        valid_id_list = [x.todo_id for x in ou.Todo.todo_instances]
        invalid_id = generate_invalid_id(valid_id_list)
        test_todo = ou.Todo.todo_instances[0]
        proper_id = test_todo.todo_id
        test_todo.todo_id = invalid_id
        result = test_todo.delete_object()
        test_todo.todo_id = proper_id
        assert result.status_code == 404

    def test_create_todo_with_invalid_user_id(self):
        valid_user_id_list = [x.id for x in ou.User.user_instances]
        invalid_id = generate_invalid_id(valid_user_id_list)
        todo_info = {"user_id": invalid_id,
                     "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
                     "due_on": "2022-08-14T00:00:00.000+05:30", "status": "completed"}
        test_todo = ou.Todo(todo_info)
        result = test_todo.create_object()
        assert result.status_code == 422

    @pytest.mark.skip(reason="due date can be in past also invalid dates are turned into None type")
    def test_create_invalid_due_date(self):
        todo_info = {"user_id": ou.User.user_instances[0].id,
                     "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
                     "due_on": "1969-12-12", "status": "completed"}
        test_todo = ou.Todo(todo_info)
        result = test_todo.create_object()
        print(test_todo.get_object().json())
        assert result.status_code == 422

    def test_create_invalid_status(self):
        todo_info = {"user_id": ou.User.user_instances[0].id,
                     "title": "Vacuus commodo summisse sopor aut torqueo tabella voluptas vester.",
                     "due_on": "2022-08-14T00:00:00.000+05:30", "status": "macarena"}
        test_todo = ou.Todo(todo_info)
        result = test_todo.create_object()
        assert result.status_code == 422

    def test_update_invalid_status(self):
        todo_info = {"status": "macarena"}
        test_todo = ou.Todo.todo_instances[0]
        result = test_todo.update_object(todo_info)
        assert result.status_code == 422

    @staticmethod
    def setup_method():
        for entry in default_entries['users']:
            test_user = ou.User(entry)
            test_user.create_object()
        for entry in default_entries['todos']:
            entry["user_id"] = ou.User.user_instances[0].id
            test_todo = ou.Todo(entry)
            test_todo.create_object()

    @staticmethod
    def teardown_method():
        local_user_list = [user for user in ou.User.user_instances]
        for user in local_user_list:
            user.delete_object()
        local_todo_list = [todo for todo in ou.Todo.todo_instances]
        for todo in local_todo_list:
            todo.delete_object()
