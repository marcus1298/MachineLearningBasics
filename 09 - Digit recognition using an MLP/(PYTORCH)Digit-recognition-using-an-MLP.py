import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt

# Define a classe da rede neural
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(28*28, 512)
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = torch.sigmoid(self.fc1(x))
        x = self.fc2(x)
        return x

# Carregar dados de treinamento e teste
train_dataset = torchvision.datasets.MNIST(root="./data", train=True, transform=transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.MNIST(root="./data", train=False, transform=transforms.ToTensor(), download=True)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=100, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=100, shuffle=False)

# Criar modelo, loss e optimizer
model = MLP()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Treinar a rede
def train(model, train_loader, criterion, optimizer, n_epochs=10):
    model.train()
    for epoch in range(n_epochs):
        for i, (images, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

# Testar a rede
def test(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
          outputs = model(images)
          _, predicted = torch.max(outputs.data, 1)
          total += labels.size(0)
          correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print(f"Accuracy: {accuracy:.2f}%")
    return accuracy

# Treinar a rede
train(model, train_loader, criterion, optimizer, n_epochs=10)

# Testar a rede
accuracy = test(model, test_loader)

#Plotando os digitos classificados corretamente
x_test, y_test = next(iter(test_loader))
y_pred = model(x_test).argmax(dim=1)

fig, axs = plt.subplots(2, 5, figsize=(15, 6))
axs = axs.ravel()
for i in range(10):
  # Selecionar apenas os dígitos classificados corretamente para aquela classe
  correct_class_indices = np.where((y_test == i) & (y_pred == i))
  x_class = x_test[correct_class_indices]
# Plotar cada dígito na sua respectiva subfigura
for j, img in enumerate(x_class[:5]):
  axs[i].imshow(img.reshape(28,28), cmap='gray')
  axs[i].axis('off')
  axs[i].set_title(f"Classe: {i}")

plt.suptitle("Digitos classificados corretamente - Acurácia: {:.2f}%".format(accuracy))
plt.show()
