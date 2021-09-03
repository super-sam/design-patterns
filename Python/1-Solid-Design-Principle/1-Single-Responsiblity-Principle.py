# SRP SOC
# If we have a class if should have a primary responsibility
# It shouldn't take other responsibilities

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # Below methods are secondary responsiblities which make not be responsiblity of
    # Journal.
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

# Instead we will have separate helper to help us with the same
class PersistenceManager:
    @staticmethod
    def save_to_file(text, filename):
        file = open(filename, 'w')
        file.write(text)
        file.close()


if __name__ == '__main__':
    j = Journal()
    j.add_entry('I smiled today')
    j.add_entry('I ate Ice-cream today')
    print(f'Journal entries: \n{j}')
    file = './journal.txt'
    PersistenceManager.save_to_file(str(j), file)

    with open(file) as fh:
        print(fh.read())