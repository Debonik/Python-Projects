# Matrix Factorization for Movie Recommendations in PyTorch

## Import Libraries

```python
import torch
import torch.nn as nn
import torch.optim as optim
```
- `torch` : Imports the PyTorch library for tensor computations and neural networks.
- `nn`: Neural network module from PyTorch.
- `optim`: Optimization algorithms from PyTorch.

---

## Data Preparation

```python
ratings = torch.tensor([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
], dtype=torch.float32)
```
- Initializes a `5x4 tensor` to represent ratings from 5 users for 4 movies.

```python
movies = ["Movie_A", "Movie_B", "Movie_C", "Movie_D"]
```
- Creates a list of movie names corresponding to the columns in the `ratings` tensor.

---

## Hyperparameters

```python
num_users, num_movies = ratings.shape
embedding_dim = 3
num_epochs = 1000
learning_rate = 0.01
```
- `num_users, num_movies`: Extracts dimensions of the `ratings` tensor.
- `embedding_dim`: Dimensionality of the latent factors.
- `num_epochs`: Number of training epochs.
- `learning_rate`: Learning rate for the optimizer.

---

## Model Definition

```python
class MatrixFactorization(nn.Module):
    def __init__(self, num_users, num_movies, embedding_dim):
        super(MatrixFactorization, self).__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.movie_embedding = nn.Embedding(num_movies, embedding_dim)
```
- Defines the `MatrixFactorization` class, inheriting from `nn.Module`.
- Initializes embeddings for users and movies.

```python
    def forward(self, user, movie):
        user_embedded = self.user_embedding(user)
        movie_embedded = self.movie_embedding(movie)
        return (user_embedded * movie_embedded).sum(1)
```
- Defines the forward propagation method.

---

## Model, Loss, and Optimizer Initialization

```python
model = MatrixFactorization(num_users, num_movies, embedding_dim)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)
```
- Initializes the model, the loss function as `Mean Squared Error`, and the optimizer as `SGD`.

---

## Training Loop

```python
for epoch in range(num_epochs):
    for i in range(num_users):
        for j in range(num_movies):
            if ratings[i][j] > 0:
                optimizer.zero_grad()
                prediction = model(torch.tensor([i]), torch.tensor([j]))
                loss = criterion(prediction, torch.tensor([ratings[i][j]]))
                loss.backward()
                optimizer.step()
```
- Implements the training loop, performing forward and backward propagation and model parameter updates.

---

## Predictions and Recommendations

```python
target_users = [0, 2]
for user_idx in target_users:
    test_user = torch.tensor([user_idx]*num_movies)
    test_movies = torch.tensor(list(range(num_movies)))
    predictions = model(test_user, test_movies).detach().numpy()
    recommendations = dict(zip(movies, predictions))
    sorted_recommendations = {k: v for k, v in sorted(recommendations.items(), key=lambda item: item[1], reverse=True)}
```
- Makes predictions for users and sorts the movies based on predicted ratings.

```python
    print(f"Recommended movies for user {user_idx}:")
    for movie, rating in sorted_recommendations.items():
        print(f"{movie}: Predicted rating {rating:.2f}")
```
- Prints out the recommended movies for each target user.
