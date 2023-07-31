import pytest
from hashmap_left_join import HashTable

@pytest.fixture
def hash_table():
    return HashTable()

def test_left_join_empty_tables(hash_table):
    synonyms_data = {}
    antonyms_data = {}
    result = hash_table.left_join(antonyms_data)  
    assert result == []

def test_left_join_all_keys_exist(hash_table):
    synonyms_data = {
        "happy": "joyful",
        "sad": "unhappy",
        "angry": "furious"
    }
    antonyms_data = {
        "happy": "unhappy",
        "sad": "happy",
        "angry": "calm"
    }
    for key, value in synonyms_data.items():
        hash_table.set(key, value)
    result = hash_table.left_join(antonyms_data)  
    assert result == [
        ["happy", "joyful", "unhappy"],
        ["sad", "unhappy", "happy"],
        ["angry", "furious", "calm"]
    ]

def test_left_join_missing_keys(hash_table):
    synonyms_data = {
        "happy": "joyful",
        "sad": "unhappy",
        "angry": "furious",
        "peaceful": "calm"
    }
    antonyms_data = {
        "happy": "unhappy",
        "sad": "happy",
        "angry": "calm",
        "joyful": "worried"
    }
    for key, value in synonyms_data.items():
        hash_table.set(key, value)
    result = hash_table.left_join(antonyms_data)  
    assert result == [
        ["happy", "joyful", "unhappy"],
        ["sad", "unhappy", "happy"],
        ["angry", "furious", "calm"],
        ["peaceful", "calm", "NULL"]
    ]


