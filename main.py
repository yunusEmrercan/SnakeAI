from snake import SnakeGameAI
import random

game = SnakeGameAI()

while True:
    state = game.get_state()
    print("State:", state)
    action = random.choice([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    reward, done, score = game.play_step(action=action)

    print(f"Reward: {reward} - Done: {done} - Score: {score}")

    if done:
        print("Oyun bitti :(")
        print(f"Final Score: {score}")

        game.reset()