class EdgeData:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = 0
        self.info = None

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        self.info = tag

    def __repr__(self):
        return "{} | {} | {} | {} | {}".format(self.src, self.dest, self.weight, self.tag, self.info)
