class NodeData:
    key_id = 0 # TODO: Is it necessary?

    def __init__(self, key: int = key_id, weight: float = 0.0, pos: tuple = None, tag: int = 0, info: str = "a"):
        self.key_id += 1
        self.key = key
        self.weight = weight
        self.pos = pos
        self.tag = tag
        self.info = info

    def get_key(self):
        return self.key

    def get_pos(self):
        return self.pos

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
        return "{} | {} | {} | {} | {}".format(self.key, self.weight, self.pos, self.tag, self.info)
