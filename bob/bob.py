def hey(query):
    # type: (str) -> str
    """Analyzes a query and returns an appropriate response as per the "bob" algorithm.

    :param query: what's being said to bob
    :return: bob response
    """
    query = query.strip()
    query_filtered = ''.join([c if c.isalnum() else '' for c in query])

    if query_filtered.isupper():
        return bob_response('yell')

    if query.endswith('?'):
        return bob_response('question')

    if query_filtered == '':
        return bob_response('empty')

    return bob_response('default')


def bob_response(query_category):
    # type: (str) -> str
    """ Return a response based on category of query."""
    response = {
        'question': 'Sure.',
        'yell': 'Whoa, chill out!',
        'empty': 'Fine. Be that way!',
        'default': 'Whatever.'
    }

    return response.get(query_category, response['default'])
