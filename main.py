from model import Linear_QNet
from snake import SnakeGameAI
import torch

game = SnakeGameAI()

model = Linear_QNet(
    input_size=11,
    hidden_size=256,
    output_size=3
)


state = game.get_state()

state_tensor = torch.tensor(state, dtype=torch.float)

prediction = model(state_tensor)

print("State", state)
print("Q Values", prediction)

