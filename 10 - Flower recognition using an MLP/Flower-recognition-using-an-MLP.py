# Downloading and loading the data
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
filename = "iris.data"
urllib.request.urlretrieve(url, filename)
iris_data = pd.read_csv(filename, header=None)
iris_data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Divide the data into training and test sets
X = iris_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = iris_data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Encode class values as integers
encoder = LabelEncoder()
encoder.fit(y_train)
encoded_y_train = encoder.transform(y_train)

# Convert integers to dummy variables (i.e. one hot encoded)
y_train_categorical = to_categorical(encoded_y_train)

# Create the MLP model
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train_categorical, epochs=100, batch_size=10)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Convert class probabilities to class labels
y_pred = np.argmax(y_pred, axis=1)

# Convert integers to original class labels
y_pred = encoder.inverse_transform(y_pred)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: %.2f' % accuracy)


# Plot the dataset using Seaborn
iris = sns.load_dataset("iris")
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.show()

# Use the model to make predictions on new data
new_data = [[5.1, 3.5, 1.4, 0.2]]
predictions = model.predict(new_data)
predicted_class = encoder.inverse_transform(predictions.argmax(axis=1))
print("Predicted class for new data:", predicted_class)
