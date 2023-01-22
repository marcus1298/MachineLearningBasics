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

# Inicializando lista de perda
loss_history = []

# Treinar a rede
def train(model, train_loader, criterion, optimizer, n_epochs=10):
    model.train()
    for epoch in range(n_epochs):
        for i, (images, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss_history.append(loss.item())
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

# Plotando a evolução da perda durante o treinamento
def plot_loss_history(loss_history):
    plt.plot(loss_history)
    plt.xlabel('Iteration')
    plt.ylabel('Loss')
    plt.title('Training loss history')
    plt.show()

# Plotando exemplos de dígitos classificados incorretamente
def plot_misclassified(model, test_loader):
    model.eval()
    misclassified_idx = []
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        misclassified_idx += list(np.where(predicted != labels)[0])
    if len(misclassified_idx) == 0:
        print("Não há exemplos classificados incorretamente.")
        return
    plt.figure(figsize=(20, 4))
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    for i, idx in enumerate(misclassified_idx[:20]):
        plt.subplot(2, 10, i + 1)
        plt.imshow(x_test[idx].reshape(28, 28), cmap='gray')
        plt.title("True: %s, Pred: %s" % (y_test[idx].item(), y_pred[idx].item()))
    plt.show()

# Treinar a rede
train(model, train_loader, criterion, optimizer, n_epochs=10)

# Testar a rede
accuracy = test(model, test_loader)

# Plotando a evolução da perda durante o treinamento
plot_loss_history(loss_history)

# Plotando exemplos de dígitos classificados incorretamente
plot_misclassified(model, test_loader)
