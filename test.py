import tensorflow as tf

a = tf.constant([[1, 2],
                 [3, 4]])
c = tf.constant([[9, 8],
                 [7, 6]])
b = tf.constant([[0, 1, 2],
                 [2, 3, 4]])
with tf.Session() as sess:
    print(tf.tensordot(a, b, axes=1).eval())
    print((a+c).eval())
    print(tf.reduce_sum(a, axis=-1).eval())
    print(())