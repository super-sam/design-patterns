class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        self.room.message(self, who, message)


class ChatRoom:
    def __init__(self):
        self.people = []

    def join(self, person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination.name:
                p.receive(source.name, message)


if __name__ == "__main__":
    room = ChatRoom()

    supratim = Person("Supratim")
    sapna = Person("Sapna")

    room.join(supratim)
    room.join(sapna)
    supratim.say("Hi Room!")
    sapna.say("Oh, hey Supratim!")

    joey = Person("Joey")
    room.join(joey)
    joey.say("Hi Everyone!")
    sapna.private_message(joey, "Love to see you here")