class Store:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        keys = key.split('.')
        cur_data = self.data
        for i, k in enumerate(keys):
            if k not in cur_data:
                if i == len(keys) - 1:
                    cur_data[k] = value
                else:
                    cur_data[k] = {}
            cur_data = cur_data[k]

    def get(self, key):
        keys = key.split('.')
        cur_data = self.data
        for k in keys:
            if k in cur_data:
                cur_data = cur_data[k]
            else:
                return None
        return cur_data

    def update(self, key, value):
        exist_data = self.get(key)
        if exist_data is not None:
            exist_data.update(value)
            