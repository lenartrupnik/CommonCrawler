import eventregistry
from eventregistry import *
from preferences import EVENT_REGISTRY_API_KEY

er = EventRegistry(apiKey= EVENT_REGISTRY_API_KEY, allowUseOfArchive=False)

q = QueryArticlesIter(
    keywords=QueryItems.AND(["start-up", "artificial intelligence"]),
    minSentiment=0.4,
    dataType= ["news", "blog"]
)

for art in q.execQuery(er, sortBy="date", maxItems=10):
    print(art)