def hello_world():
    print("hello world!")


def delete_lobby():
    return "DELETE", "/lol-lobby/v2/lobby"

def create_lobby(queueId):
    return "POST", "/lol-lobby/v2/lobby", {"queueId":queueId}

def set_roles(first, second):
    return "PUT", "/lol-lobby/v1/lobby/members/localMember/position-preferences", {"firstPreference":first, "secondPreference":second}

def search_match():
    return "POST", "/lol-lobby/v2/lobby/matchmaking/search"

def ready_check_accept():
    return 'POST', '/lol-matchmaking/v1/ready-check/accept'

def play_again():
    return 'POST', '/lol-lobby/v2/play-again'

def get_phase():
    return 'GET', '/lol-gameflow/v1/gameflow-phase'

def get_search_match():
    return 'GET', '/lol-matchmaking/v1/search'
