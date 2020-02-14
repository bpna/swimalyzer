from html.parser import HTMLParser

class SwimParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.results_found = False
        self.raw_results = None

    def handle_starttag(self, tag, attrs):
        if (tag == 'pre'):
            self.results_found = True

    def handle_endtag(self, tag):
        if (tag == 'pre'):
            self.results_found = False

    def handle_data(self, data):
        if self.results_found:
            self.raw_results = data

    def get_results(self):
        return self.raw_results
