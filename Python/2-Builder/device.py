from abc import ABC, abstractmethod


class DeviceAbstract(ABC):
    def __init__(self):
        self._ip_address = None
        self._hostname = None
        self._username = None
        self._password = None

    def __str__(self):
        return 'ip: %s(%s) is connected by %s with %s' % (self._ip_address, self._hostname, self._username, self._password)

    def


class DeviceBuilder:
    def __init__(self, device=None):
        if device is None:
            self.device = DeviceAbstract()
        else:
            self.device = device

    @property
    def info(self):
        return DeviceInfoBuilder(self.device)

    @property
    def connect(self):
        return DeviceConnectionBuilder(self.device)

    def build(self):
        return self.device


class DeviceInfoBuilder(DeviceBuilder):
    def __init__(self, device):
        super().__init__(device)

    def has_ip(self, ip_address):
        self.device._ip_address = ip_address
        return self

    def mapped_to(self, hostname):
        self.device._hostname = hostname
        return self


class DeviceConnectionBuilder(DeviceBuilder):
    def __init__(self, device):
        super().__init__(device)

    def as_user(self, username):
        self.device._username = username
        return self

    def with_pwd(self, password):
        self.device._password = password
        return self


if __name__ == '__main__':
    db = DeviceBuilder()
    router = db\
            .info\
                .has_ip('192.168.0.1')\
                .mapped_to('www.localhost.com')\
            .connect\
                .as_user('ssamantray')\
                .with_pwd('simplepwd')\
            .build()

    print(router)
