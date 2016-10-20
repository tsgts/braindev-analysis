import tensorflow as tf

matrix = tf.constant([[3., 3.]])

# Initializing the variables
init = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init)
	print(matrix)
