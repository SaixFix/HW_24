from functions import filter_query, map_query, unique_query, sort_query, limit_query


class WorkByFile:
    def read_file(self, file_name: str):
        with open(file_name) as file:
            for row in file:
                yield row

    def query(self, cmd, value):
        gen = self.read_file('./data/apache_logs.txt')
        filtered = list(filter_query(value, gen))
        mapped = list(map_query('0', filtered))
        unique = list(unique_query(mapped))
        sort = sort_query(param='desc', data=unique)
        limited = limit_query(param='1', data=sort)
        return limited
        # while True:
        #     gen = self.read_file(file_name)
        #
        #     try:
        #         data = next(gen)
        #     except StopIteration:
        #         break


# query_builder = WorkByFile()
# print(list(query_builder.query('POST', 'Mozilla')))








