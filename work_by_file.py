from functions import filter_query, map_query, unique_query, sort_query, limit_query

CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
}

class WorkByFile:
    def read_file(self, file_name: str):
        with open(file_name) as file:
            for row in file:
                yield row

    def query(self, cmd, value):
        gen = self.read_file('./data/apache_logs.txt')

        result = CMD_TO_FUNCTION[cmd](param=value, data=gen)
        return list(result)

        # filtered = list(filter_query(value, gen))
        # mapped = list(map_query('0', filtered))
        # unique = list(unique_query(mapped))
        # sort = sort_query(param='desc', data=unique)
        # limited = limit_query(param='1', data=sort)
        # return limited








