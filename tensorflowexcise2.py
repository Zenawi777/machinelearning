import tensorflow as tf
import numpy as np

# Matrix opperation trail
b=np.matrix([[1,2,3],[4,5,6]])
a=np.matrix([[1,1,1],[1,1,1]])

c=a+b


# Tensorflow example

with tf.Session():
  input1 = tf.constant(1.0, shape=[2, 3])
  input2 = tf.constant(np.reshape(np.arange(1.0, 7.0, dtype=np.float32), (2, 3)))
  output = tf.add(input1, input2)
  result = output.eval()

result
