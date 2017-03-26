from .NetAPI import NetInterface


class Progress:

    def __init__(self, ships):
        self.interface = NetInterface()
        self.ships = ships

    def start_progress(self):
        self.interface.start_listen()

    def get_name(self):
        return self.interface.get()

    def send_name(self, name):
        self.interface.send(name)

    def get_step(self):
        return self.interface.get()

    def send_step(self, step):
        self.interface.send(step)
        return self.interface.get()

    def update_my_ships(self, answer, step):
        pass

    def finish_progress(self):
        self.interface.send_finish()
