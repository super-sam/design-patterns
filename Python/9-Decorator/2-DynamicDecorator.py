class FileWithLogging:
    def __init__(self, file):
        self.__file = file

    def writelines(self, strings):
        self.__file.writelines(strings)
        print(f'wrote {len(strings)} lines')

    def __iter__(self):
        return self.__file.__iter__()

    def __next__(self):
        return self.__file.__next__()

    def __getattr__(self, item):
        return getattr(self.__dict__['_FileWithLogging__file'], item)

    def __setattr__(self, key, value):
        if key == "_FileWithLogging__file":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__["_FileWithLogging__file"], key)

    def __delattr__(self, item):
        delattr(self.__dict__["_FileWithLogging__file"], item)


if __name__ == '__main__':
  myfile = FileWithLogging(open('hello.txt', 'w'))
  # myfile.writelines(['hello', 'world'])
  myfile.write('testing')
  myfile.close()
