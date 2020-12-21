from steam.views import SearchByTag

steam_search_by_tag = '/api/steam_search_by_tag'

routes = [
    ("GET", steam_search_by_tag, SearchByTag.get),
]
