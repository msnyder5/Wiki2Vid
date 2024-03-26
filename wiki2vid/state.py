from wiki2vid.ai import AI
from wiki2vid.scripter.script import Script
from wiki2vid.wiki import Wiki


class State:
    def __init__(self, wiki_url: str):
        self.wiki = Wiki(wiki_url)
        self.script = Script("Outline")
