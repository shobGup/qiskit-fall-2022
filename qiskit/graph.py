class Vertex:
    url = ""
    title = ""
    def __init__(u, t):
        url = u
        title = t
    def get_url():
        return url
    def get_title():
        return title
    def set_url(new_url):
        url = new_url
    def set_title(new_title):
        title = new_title

class Graph:
    vertices = []    
