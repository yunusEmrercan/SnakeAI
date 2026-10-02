import random


class Agent:
    def __init__(self):

        # kaç oyun oynandı
        self.n_games = 0



    def get_action(self, state):
        """şimdilik sadece rastgele karar veriyoruz sonrasında Neural network eklenecek
        """

        random_number = random.randint(0, 2)

        if random_number == 0:
            return [1, 0, 0]

        elif random_number == 1:
            return [0, 1, 0]

        else:
            return [0, 0, 1]

        