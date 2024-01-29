import pytest

from models.database.exception import KnowledgeNotFoundException
from models.database.knowledge import KnowledgeDatabaseAccessor, KnowledgeDatabaseInitializer


DUMMY_TENANT_NAME: str = "12345678"
DUMMY_USER_ID: str = "dummy.name"
DUMMY_OTHERS_ID: str = "john.doe"
DUMMY_USER_NAME: str = "Dummy Name"
DUMMY_OTHERS_NAME: str = "John Doe"


@pytest.fixture(scope='function')
def setup():
    with KnowledgeDatabaseInitializer() as database:
        database.create_all_tables()
        database.initialize_master_tables()
        database.upsert_tenant(DUMMY_TENANT_NAME)
        database.upsert_user(DUMMY_USER_ID, DUMMY_USER_NAME, DUMMY_TENANT_NAME)
        database.upsert_user(DUMMY_OTHERS_ID, DUMMY_OTHERS_NAME, DUMMY_TENANT_NAME)
    yield
    with KnowledgeDatabaseInitializer() as database:
        database.truncate_master_tables()
        database.drop_all_tables()

def test_knowledge(setup):
    keywords = [ 'aaa', 'bbb', 'ccc' ]
    knowledge_01 = 'test_test_test_01'
    knowledge_02 = 'test_test_test_02'
    knowledge_03 = 'test_test_test_03'
    knowledge_type = 'text'
    with KnowledgeDatabaseAccessor() as database:
        # insert
        knowledge_id_01 = database.insert_knowledge(DUMMY_USER_ID, keywords, knowledge_01, knowledge_type, True)
        database.insert_knowledges(DUMMY_OTHERS_ID, [
            { 'keywords': keywords, 'knowledge': knowledge_02, 'type': knowledge_type, 'private': False },
        ])
        knowledge_id_03 = database.insert_knowledge(DUMMY_OTHERS_ID, keywords, knowledge_03, knowledge_type, True)

        # fetch
        knowledge_info = database.fetch_knowledge(DUMMY_USER_ID, knowledge_id_01)
        assert knowledge_info['contents'] == knowledge_01

        # fetch for search
        search_result = database.fetch_knowledge_list(DUMMY_USER_ID, keywords[0])
        assert len(search_result) == 2
        assert isinstance(search_result[0]['knowledge_id'], int)
        assert search_result[0]['type'] == knowledge_type
        assert search_result[0]['contents'] == knowledge_01
        assert search_result[0]['private']
        assert search_result[0]['user_id'] == DUMMY_USER_ID
        assert search_result[0]['user_name'] == DUMMY_USER_NAME
        assert isinstance(search_result[1]['knowledge_id'], int)
        assert search_result[1]['type'] == knowledge_type
        assert search_result[1]['contents'] == knowledge_02
        assert not search_result[1]['private']
        assert search_result[1]['user_id'] == DUMMY_OTHERS_ID
        assert search_result[1]['user_name'] == DUMMY_OTHERS_NAME

        # fetch for list
        list_result = database.fetch_knowledge_mappings(DUMMY_OTHERS_ID)
        assert len(list_result) == 2
        assert isinstance(list_result[0]['knowledge']['knowledge_id'], int)
        assert list_result[0]['knowledge']['type'] == knowledge_type
        assert list_result[0]['knowledge']['contents'] == knowledge_03
        assert list_result[0]['knowledge']['private']
        assert list_result[0]['knowledge']['user_id'] == DUMMY_OTHERS_ID
        assert list_result[0]['knowledge']['user_name'] == DUMMY_OTHERS_NAME
        for i, k in enumerate(list_result[0]['keywords']):
            assert k == keywords[i]
        assert isinstance(list_result[1]['knowledge']['knowledge_id'], int)
        assert list_result[1]['knowledge']['type'] == knowledge_type
        assert list_result[1]['knowledge']['contents'] == knowledge_02
        assert not list_result[1]['knowledge']['private']
        assert list_result[1]['knowledge']['user_id'] == DUMMY_OTHERS_ID
        assert list_result[1]['knowledge']['user_name'] == DUMMY_OTHERS_NAME
        for i, k in enumerate(list_result[1]['keywords']):
            assert k == keywords[i]
        for i, k in enumerate(database.fetch_knowledge_keyword_list(DUMMY_USER_ID, knowledge_id_01)):
            assert k['text'] == keywords[i]

        # delete
        delete_result = database.delete_knowledge_and_fetch_knowledge_mappings(DUMMY_OTHERS_ID, knowledge_id_03)
        assert len(delete_result) == 1
        assert isinstance(delete_result[0]['knowledge']['knowledge_id'], int)
        assert delete_result[0]['knowledge']['type'] == knowledge_type
        assert delete_result[0]['knowledge']['contents'] == knowledge_02
        assert not delete_result[0]['knowledge']['private']
        assert delete_result[0]['knowledge']['user_id'] == DUMMY_OTHERS_ID
        assert delete_result[0]['knowledge']['user_name'] == DUMMY_OTHERS_NAME
        for i, k in enumerate(delete_result[0]['keywords']):
            assert k == keywords[i]
        database.delete_knowledge(DUMMY_USER_ID, knowledge_id_01)
        with pytest.raises(KnowledgeNotFoundException) as e:
            database.fetch_knowledge(DUMMY_USER_ID, knowledge_id_01)
        assert e.value.status == 404
        assert e.value.code == '1040'
        assert e.value.message == "Knowledge not found."
