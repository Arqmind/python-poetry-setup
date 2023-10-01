import uuid
from src import generate_uuids as gu


def test_generate_random_uuid():
    random_uuid = gu.generate_random_uuid()
    assert uuid.UUID(random_uuid.hex).version == 4


def test_generate_time_based_uuid():
    time_based_uuid = gu.generate_time_based_uuid()
    assert uuid.UUID(time_based_uuid.hex).version == 1


def test_generate_namespace_based_uuid():
    namespace = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    name = "example.com"
    namespace_based_uuid = gu.generate_namespace_based_uuid(namespace, name)
    assert uuid.UUID(namespace_based_uuid.hex).version == 5
