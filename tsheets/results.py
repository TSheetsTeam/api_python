from helpers import class_to_endpoint
import repos


class Results(object):
    def __init__(self, url, options, repo, bridge, is_singleton=False, mode="list"):
        self.url = url
        self.options = options
        self.repo = repo
        self.model = repo.model
        self.name = class_to_endpoint(self.model.__name__) + ('' if is_singleton else 's')
        self.index = -1
        self.loaded = []
        self.bridge = bridge
        self.has_more = True
        self.is_singleton = is_singleton
        self.mode = mode
        self.page = 0

    def __iter__(self):
        return self

    def next(self):
        if (self.index+1) < len(self.loaded) or (self.has_more and self._load_next_batch()):
            self.index += 1
            next_value = self.loaded[self.index]
            return next_value
        else:
            raise StopIteration

    def first(self):
        return self.next()

    def all(self):
        return list(self)

    def _load_next_batch(self):
        # Because LastModifiedTimestamps can't deal with pagination, we have
        # to exclude it here.
        if not isinstance(self.repo, repos.LastModifiedTimestamps):
            if self.repo.filters.get('page', False):
                self.options.update({'page': self.page})
        response = self.bridge.next_batch(self.url, self.name, self.options, self.is_singleton, self.mode)

        batch = response['items']
        self.has_more = not self.is_singleton and self.mode == 'list' and response['has_more']
        if self.is_singleton:
            self.loaded = [ self.model.from_raw(batch) ]
        else:
            self.loaded += [self.model.from_raw(o) for o in batch]
        self.page += 1
        return batch

