class TagManipulator():
    def parse_string(self, tags, regex=""):
        result = []

        if len(tags) < 1 or tags == ',':
            return result
        else:
            result = tags.split(',')
            for res in result:
                if res == '':
                    result.remove(res)

        return result