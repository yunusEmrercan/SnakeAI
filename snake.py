import pygame
import random


class SnakeGameAI:

    def __init__(self, width=600, height=600, cell_size=20):

        pygame.init()

        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.display = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption("Snake AI")

        self.clock = pygame.time.Clock()

        self.reset()


    def reset(self):

        # Snake başlangıç konumu
        self.snake = [
            [300, 300],
            [280, 300],
            [260, 300]
        ]

        # Başlangıç yönü
        self.direction = [self.cell_size, 0]

        # Score
        self.score = 0

        # Oyun bitti mi?
        self.done = False

        # İlk yemek
        self.food = self.create_food()


    def create_food(self):

        while True:

            x = random.randrange(
                0,
                self.width,
                self.cell_size
            )

            y = random.randrange(
                0,
                self.height,
                self.cell_size
            )

            food = [x, y]

            if food not in self.snake:
                return food


    def play_step(self, action):

        """
        action:

        [1, 0, 0] -> SOL
        [0, 1, 0] -> DÜZ
        [0, 0, 1] -> SAĞ
        """

        # -------------------------
        # PYGAME EVENT
        # -------------------------

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                raise SystemExit


        # -------------------------
        # YÖNÜ DEĞİŞTİR
        # -------------------------

        self.change_direction(action)


        # -------------------------
        # YILANI HAREKET ETTİR
        # -------------------------

        head = self.snake[0]

        new_head = [
            head[0] + self.direction[0],
            head[1] + self.direction[1]
        ]

        self.snake.insert(0, new_head)


        # -------------------------
        # ÇARPIŞMA
        # -------------------------

        if self.is_collision():

            self.done = True

            return -10, self.done, self.score


        # -------------------------
        # YEMEK
        # -------------------------

        if new_head == self.food:

            self.score += 1

            reward = 10

            self.food = self.create_food()

        else:

            reward = 0

            self.snake.pop()


        # -------------------------
        # ÇİZ
        # -------------------------

        self.update_ui()

        return reward, self.done, self.score


    def change_direction(self, action):

        """
        Action:

        [1,0,0] = SOL
        [0,1,0] = DÜZ
        [0,0,1] = SAĞ
        """

        current_x = self.direction[0]
        current_y = self.direction[1]


        # SOL

        if action == [1, 0, 0]:

            self.direction = [
                current_y,
                -current_x
            ]


        # DÜZ

        elif action == [0, 1, 0]:

            self.direction = [
                current_x,
                current_y
            ]


        # SAĞ

        elif action == [0, 0, 1]:

            self.direction = [
                -current_y,
                current_x
            ]


    def is_collision(self, point=None):

        if point is None:

            point = self.snake[0]


        x, y = point


        # Duvar

        if (
            x < 0 or
            x >= self.width or
            y < 0 or
            y >= self.height
        ):

            return True


        # Kendi vücudu

        if point in self.snake[1:]:

            return True


        return False


    def update_ui(self):

        self.display.fill((0, 0, 0))


        # Snake

        for segment in self.snake:

            pygame.draw.rect(
                self.display,
                (0, 200, 0),
                (
                    segment[0],
                    segment[1],
                    self.cell_size,
                    self.cell_size
                )
            )


        # Food

        pygame.draw.rect(
            self.display,
            (200, 0, 0),
            (
                self.food[0],
                self.food[1],
                self.cell_size,
                self.cell_size
            )
        )


        pygame.display.flip()

        self.clock.tick(15)



    def get_state(self):

        head = self.snake[0]

        x = head[0]
        y = head[1]

        # --------------------------------
        # Mevcut yön
        # --------------------------------

        direction_up = self.direction == [0, -self.cell_size]
        direction_right = self.direction == [self.cell_size, 0]
        direction_down = self.direction == [0, self.cell_size]
        direction_left = self.direction == [-self.cell_size, 0]


        # --------------------------------
        # İleri / sağ / sol noktaları
        # --------------------------------

        if direction_up:

            point_straight = [
                x,
                y - self.cell_size
            ]

            point_right = [
                x + self.cell_size,
                y
            ]

            point_left = [
                x - self.cell_size,
                y
            ]


        elif direction_right:

            point_straight = [
                x + self.cell_size,
                y
            ]

            point_right = [
                x,
                y + self.cell_size
            ]

            point_left = [
                x,
                y - self.cell_size
            ]


        elif direction_down:

            point_straight = [
                x,
                y + self.cell_size
            ]

            point_right = [
                x - self.cell_size,
                y
            ]

            point_left = [
                x + self.cell_size,
                y
            ]


        else:  # LEFT

            point_straight = [
                x - self.cell_size,
                y
            ]

            point_right = [
                x,
                y - self.cell_size
            ]

            point_left = [
                x,
                y + self.cell_size
            ]


        # --------------------------------
        # Tehlikeler
        # --------------------------------

        danger_straight = self.is_collision(
            point_straight
        )

        danger_right = self.is_collision(
            point_right
        )

        danger_left = self.is_collision(
            point_left
        )


        # --------------------------------
        # Yemeğin yönü
        # --------------------------------

        food_up = self.food[1] < y
        food_right = self.food[0] > x
        food_down = self.food[1] > y
        food_left = self.food[0] < x


        # --------------------------------
        # STATE
        # --------------------------------

        state = [
            int(danger_straight),
            int(danger_right),
            int(danger_left),

            int(direction_up),
            int(direction_right),
            int(direction_down),
            int(direction_left),

            int(food_up),
            int(food_right),
            int(food_down),
            int(food_left)
        ]


        return state