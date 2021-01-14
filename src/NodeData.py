class NodeData:

    def __init__(self, key: int, pos: tuple = None):
        self.key = key
        self.weight = float('inf')
        self.pos = pos
        self.tag = 0
        self.info = ""

    def get_key(self):
        return self.key

    def get_pos(self):
        return self.pos

    def set_pos(self, pos: tuple):
        self.pos = pos

    def get_weight(self):
        return self.weight

    def set_weight(self, w):
        self.weight = w

    def get_tag(self):
        return self.tag

    def set_tag(self, t):
        self.tag = t

    def get_info(self):
        return self.info

    def set_info(self, i):
        self.info = i

    def __repr__(self):
        return "key:{} | weight:{} | pos:{} | tag:{} | info:{}".format(self.key, self.weight, self.pos, self.tag, self.info)

    def __lt__(self, other):
        return self.tag < other.tag

    def __eq__(self, other):
        return self.key == other.key and self.weight == other.weight and self.pos == other.pos\
            and self.info == other.info and self.tag == other.tag
