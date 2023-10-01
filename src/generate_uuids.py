import uuid


def generate_random_uuid():
    """
    Generate random uuid
    @return: uuid
    """
    # Generate a random UUID (version 4)
    random_uuid = uuid.uuid4()
    print("Random UUID (version 4):", random_uuid)
    return random_uuid


def generate_time_based_uuid():
    """
    geterating time base uuid

    @return: uuid
    """
    # Generate a UUID based on the host's MAC address and the current time (version 1)
    time_based_uuid = uuid.uuid1()
    print("Time-based UUID (version 1):", time_based_uuid)
    return time_based_uuid


def generate_namespace_based_uuid(namespace, name):
    """
    Generate namespace based uuid

    @param namespace:str
    @name str

    @return: uuid
    """
    # Generate a UUID based on a namespace and a name (version 5)
    # namespace = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    # name = "example.com"
    namespace_based_uuid = uuid.uuid5(namespace, name)
    print("Namespace-based UUID (version 5):", namespace_based_uuid)
    return namespace_based_uuid
