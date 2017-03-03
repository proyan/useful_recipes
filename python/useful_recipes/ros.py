def extractRosBag(filename):
    """Returns the result of a rosbag file as a dictionary
    Input: (string)rosbag filename
    output: (dictionary) content of the bag
    """
    import rosbag
    _bag = rosbag.Bag(filename)
    _topics = _bag.get_type_and_topic_info()[1].keys()
    _msg = []
    for topic, msg, t in _bag.read_messages(topics=_topics):
        _msg.append(msg)

    _output = dict()
    _keys = _msg[0].__slots__
    for key in _keys:
        _output[key] = []

    for msg in _msg:
        for key in _keys:
            _output[key].append(msg.__getattribute__(key))
    _bag.close()
    return _output
