import pickle
from sklearn.linear_model import LinearRegression

# Gere dados de exemplo (substitua por seus próprios dados)
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Treine o modelo
model = LinearRegression()
model.fit(X, y)

# Salve o modelo em um arquivo
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
