
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Dados de treinamento
x = torch.tensor([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]).reshape(-1, 1)
t = torch.tensor([-0.9602, -0.5770, -0.0729, 0.3771, 0.6405, 0.6600, 0.4609, 0.1336, -0.2013, -0.4344, -0.5000]).reshape(-1, 1)

# Definição da rede
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.hidden = nn.Linear(1, 10)
        self.output = nn.Linear(10, 1)
        
    def forward(self, x):
        x = torch.sigmoid(self.hidden(x))
        x = self.output(x)
        return x

# Instanciação da rede
model = MLP()

# Otimizador e função de perda
optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

# Treinamento
for i in range(100000):
    # Forward pass
    y_pred = model(x)

    # Cálculo da perda
    loss = criterion(y_pred, t)

    # Backward pass e otimização
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Teste
x_test = torch.linspace(0, 1, 10000).reshape(-1, 1)
y_test = model(x_test)

# Plot dos resultados
plt.scatter(x, t)
plt.plot(x_test, y_test.detach().numpy(), 'r')
plt.show()
