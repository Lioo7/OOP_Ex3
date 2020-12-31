def NodeData():
    def __init__(self):
        self.key = 0
        self.weight = 0
        self.pos = (0, 0, 0)
        self.tag = 0
        self.info = None

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
