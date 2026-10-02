from snake import SnakeGameAI
from agent import Agent
import random

game = SnakeGameAI()
agent = Agent()


while True:

    state_old = game.get_state()

    action = agent.get_action(state_old)

    reward, done, score = game.play_step(action=action)

    print(f"Reward: {reward} - Done: {done} - Score: {score}")

    if done:
        agent.n_games +=1 

        print("Oyun bitti :( Toplam Oynanan Oyun:", agent.n_games)
        print(f"Final Score: {score}")

        game.reset()