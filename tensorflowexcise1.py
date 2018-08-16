

import tensorflow as tf


# Importing data from a file
with open('feature_columns1.txt') as f:
    feature_columns = f.read()
    f.closed

# Set up a linear classifier.
classifier = tf.estimator.LinearClassifier(feature_columns)

# Train the model on some example data.
classifier.train(input_fn=train_input_fn, steps=2000)

# Use it to predict.
predictions = classifier.predict(input_fn=predict_input_fn)
