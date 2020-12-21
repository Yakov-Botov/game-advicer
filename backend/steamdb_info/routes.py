from steamdb_info.views import AllTags_View

all_tags = '/api/all_tags'

routes = [
    ("GET", all_tags, AllTags_View.get),
]
