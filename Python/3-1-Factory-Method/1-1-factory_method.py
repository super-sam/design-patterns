from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return 'Truck delivery'

class Train(Transport):
    def deliver(self):
        return 'Train delivery'

class Ship(Transport):
    def deliver(self):
        return 'Ship delivery'

class Plane(Transport):
    def deliver(self):
        return 'Plane delivery'


class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    @abstractmethod
    def plan_delivery(self):
        pass

class RoadLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Truck()

    def plan_delivery(self):
        return 'Road delivery'

class SeaLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Ship()

    def plan_delivery(self):
        return 'Sea delivery'

class AirLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Plane()
    
    def plan_delivery(self):
        return "Air delivery"

class LogisticFactory:
    @staticmethod
    def create_logistic(logistic_type: str) -> Logistic:
        if logistic_type == 'road':
            return RoadLogistic()
        elif logistic_type == 'sea':
            return SeaLogistic()
        elif logistic_type == 'air':
            return AirLogistic()
        else:
            raise ValueError('Invalid logistic type')

def client_code(logistic: Logistic):
    transport = logistic.create_transport()
    print(f'{logistic.plan_delivery()} with {transport.deliver()}')
    

class Mail(ABC):
    @abstractmethod
    def create_transport(self):
        pass
    @abstractmethod
    def send(self):
        pass

class AirMail(Mail):
    def create_transport(self):
        return Plane()
    def send(self):
        return 'Air mail'
    
class GroundMail(Mail):
    def __init__(self, mode: str="") -> None:
        self.__mode = mode
    def create_transport(self):
        if self.__mode == 'train':
            return Train()
        elif self.__mode == 'truck':
            return Truck()
        else:
            raise ValueError('Invalid mode')
    
    def send(self):
        return 'Ground mail' 

class MailFactory:
    @staticmethod
    def create_mail_air() -> Mail:
        return AirMail()
    @staticmethod
    def create_mail_ground(mode: str='train') -> Mail:
        return GroundMail(mode)

def client_code_mail(mail: Mail):
    transport = mail.create_transport()
    print(f'{mail.send()} with {transport.deliver()}')

if __name__ == '__main__':
    client_code(LogisticFactory.create_logistic('road'))
    client_code(LogisticFactory.create_logistic('sea'))
    client_code(LogisticFactory.create_logistic('air'))

    client_code_mail(MailFactory.create_mail_air())
    client_code_mail(MailFactory.create_mail_ground('truck'))
    client_code_mail(MailFactory.create_mail_ground('train'))
    client_code_mail(MailFactory.create_mail_ground())