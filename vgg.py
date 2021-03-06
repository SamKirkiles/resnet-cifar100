import tensorflow as tf
import numpy as np
from data_loader import Loader
import matplotlib.pyplot as plt



class VGG:
 
	def __init__(self):

		loader = Loader()
		iterator = loader.get_dataset()

		def build_model():

			with tf.device("/device:GPU:0"):
				x_loaded,y_loaded = iterator.get_next()

				x = tf.placeholder_with_default(x_loaded,(None,32,32,3),name="x_placeholder")
				y = tf.placeholder_with_default(y_loaded,(None),name="y_placeholder")

				training = tf.placeholder_with_default(True,name="training_bool",shape=())

				#Layer1 - 64 channels
				conv1 = tf.layers.conv2d(x, filters=64,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_1 = tf.contrib.layers.batch_norm(conv1,activation_fn=tf.nn.relu,is_training=training)


				# Layer2 - 64 channels
				conv2 = tf.layers.conv2d(bn_1, filters=64,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())

				bn_2 = tf.contrib.layers.batch_norm(conv2,activation_fn=tf.nn.relu,is_training=training)
				
				pool2 = tf.layers.max_pooling2d(bn_2, (2,2), (2,2), padding='SAME')
				dropout_2 = tf.layers.dropout(pool2,training=training,rate=0.5)
				#Layer 3 - 128 channels
				conv3 = tf.layers.conv2d(dropout_2, filters=128,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())

				bn_3 = tf.contrib.layers.batch_norm(conv3,activation_fn=tf.nn.relu,is_training=training)

				# Layer 4 - 128 channels
				conv4 = tf.layers.conv2d(bn_3, filters=128,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_4 = tf.contrib.layers.batch_norm(conv4,activation_fn=tf.nn.relu,is_training=training)
				pool4 = tf.layers.max_pooling2d(bn_4, (2,2), (2,2), padding='SAME')
				dropout_4 = tf.layers.dropout(pool4,training=training,rate=0.5)

				#Layer 5 - 256 channels
				conv5 = tf.layers.conv2d(dropout_4, filters=256,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_5 = tf.contrib.layers.batch_norm(conv5,activation_fn=tf.nn.relu,is_training=training)
				# Layer 6 - 256 channels
				conv6 = tf.layers.conv2d(bn_5, filters=256,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_6 = tf.contrib.layers.batch_norm(conv6,activation_fn=tf.nn.relu,is_training=training)
				# Layer 7 - 256 channels
				conv7 = tf.layers.conv2d(bn_6, filters=256,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_7 = tf.contrib.layers.batch_norm(conv7,activation_fn=tf.nn.relu,is_training=training)
				pool7 = tf.layers.max_pooling2d(bn_7, (2,2), (2,2), padding='SAME')
				dropout_7 = tf.layers.dropout(pool7,training=training,rate=0.5)

				# Layer 8 - 512 channels
				conv8 = tf.layers.conv2d(dropout_7, filters=512,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_8 = tf.contrib.layers.batch_norm(conv8,activation_fn=tf.nn.relu,is_training=training)
				# Layer 9 - 512 channels
				conv9 = tf.layers.conv2d(bn_8, filters=512,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_9 = tf.contrib.layers.batch_norm(conv9,activation_fn=tf.nn.relu,is_training=training)
				# Layer 10 - 512 channels
				conv10 = tf.layers.conv2d(bn_9, filters=512,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_10 = tf.contrib.layers.batch_norm(conv10,activation_fn=tf.nn.relu,is_training=training)
				pool10 = tf.layers.max_pooling2d(bn_10, (2,2), (2,2), padding='SAME')
				dropout_7 = tf.layers.dropout(pool10,training=training,rate=0.5)

				# Layer 11 - 512 channels
				conv11 = tf.layers.conv2d(dropout_7, filters=512,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_11 = tf.contrib.layers.batch_norm(conv11,activation_fn=tf.nn.relu,is_training=training)
				# Layer 12 - 512 channels
				conv12 = tf.layers.conv2d(bn_11, filters=512,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_12 = tf.contrib.layers.batch_norm(conv12,activation_fn=tf.nn.relu,is_training=training)
				# Layer 13 - 512 channels
				conv13 = tf.layers.conv2d(bn_12, filters=512,kernel_size=(3,3),padding='SAME',
					use_bias=True,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_13 = tf.contrib.layers.batch_norm(conv13,activation_fn=tf.nn.relu,is_training=training)

				pool13 = tf.layers.max_pooling2d(bn_13, (2,2), (2,2), padding='SAME')

				dropout_13 = tf.layers.dropout(pool13,training=training,rate=0.5)

				flattened = tf.contrib.layers.flatten(dropout_13)

				dense14 = tf.layers.dense(inputs=flattened, units=4096,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_14 = tf.contrib.layers.batch_norm(dense14,activation_fn=tf.nn.relu,is_training=training)
				dropout_14 = tf.layers.dropout(bn_14,training=training,rate=0.5)
				dense15 = tf.layers.dense(inputs=dropout_14, units=4096,kernel_initializer=tf.contrib.layers.xavier_initializer())
				bn_15 = tf.contrib.layers.batch_norm(dense15,activation_fn=tf.nn.relu,is_training=training)
				dense16 = tf.layers.dense(inputs=bn_15, units=100,activation=None,kernel_initializer=tf.contrib.layers.xavier_initializer())
				
				tf.summary.scalar("dense16_mean",tf.reduce_mean(dense16))

				# Predict
				outputs = tf.nn.softmax(dense16)
				prediction = tf.argmax(outputs,axis=1)

				equality = tf.equal(prediction, y)
				accuracy = tf.reduce_mean(tf.cast(equality, tf.float32))

				# Train
				softmax = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y,logits=dense16,name="softmax")

				loss = tf.reduce_mean(softmax)

				update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS) 
				
				with tf.control_dependencies(update_ops):
					step = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(loss)
				


			self.loss = loss
			self.x_placeholder = x
			self.y_placeholder = y
			self.training = training
			self.accuracy = accuracy
			self.outputs = outputs
			self.prediction = prediction
			self.step = step

			tf.summary.scalar("Loss", loss)
			tf.summary.scalar("Train Accuracy", accuracy)

		build_model()


	def train(self,restore=False):

		saver = tf.train.Saver()


		with tf.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=False)) as sess:
			try:

				run_id = np.random.randint(0,1e7)

				train_writer = tf.summary.FileWriter(logdir="logs/" + str(run_id), graph=sess.graph)

				if restore:
					saver.restore(sess, tf.train.latest_checkpoint('./saves'))
				else:
					sess.run(tf.global_variables_initializer())

				counter = 0

				train_loader = Loader(batch_size=256)
				val_x,val_y = sess.run(train_loader.get_dataset(train=False).get_next())
				
				merge = tf.summary.merge_all()

				while True:

						counter += 1

						_, summary = sess.run([self.step,merge],feed_dict={})

						train_writer.add_summary(summary,counter)

						if counter%1000 == 0:

							# Check validation accuracy on 10 batches

							acc = sess.run([self.accuracy],feed_dict={self.x_placeholder:val_x,self.y_placeholder:val_y,self.training:False})

							accuracy_summary = tf.Summary(value=[tf.Summary.Value(tag='Validation Accuracy',simple_value=acc)])
							train_writer.add_summary(accuracy_summary,counter)

						if counter%10000 == 0:
							# Save model
							print("Periodically saving model...")
							save_path = saver.save(sess, "./saves/model.ckpt")

			except KeyboardInterrupt:
				print("Interupted... saving model.")
			
			save_path = saver.save(sess, "./saves/model.ckpt")


	def test(self,restore=True):
		saver = tf.train.Saver()

		with tf.Session() as sess:

			if restore:
				saver.restore(sess, tf.train.latest_checkpoint('./saves'))
			else:
				sess.run(tf.global_variables_initializer())

			train_loader = Loader(batch_size=64)
			val_x,val_y = sess.run(train_loader.get_dataset(train=False).get_next())

			with open('fine_label_names.txt', 'r') as fp:
				lines = fp.readlines()
				lines = [line.rstrip('\n') for line in lines]

			idx = 61

			acc,outputs = sess.run([self.accuracy,self.outputs],feed_dict={self.x_placeholder:val_x,self.y_placeholder:val_y,self.training:False})
			
			

			

			for img in [0,1,2,3,4,5,12,13,21,23,24,25,26,28,29,30,31,32,34,37,39,40,41,42,44,45,48,50,51,52,53,54,55,56,57,58,61,62]:

				choices = np.flip(np.argsort(outputs[img], axis=-1, kind='quicksort', order=None),axis=0)[0:5]
				names = [lines[x] for x in choices]
				fig = plt.figure(1)
				fig.add_subplot(121)
				
				image = ((val_x[img] * 255) + 121.936059453125)
				image = image.astype(np.uint8)
				plt.imshow(image)
				fig.add_subplot(122)
				y = outputs[img][choices]
				x = [0,1,2,3,4]
				plt.yticks(np.arange(5), names)
				plt.barh(x,y)
				plt.show()
				print(img)

	

			# 0,3, 63, 61

			




	def softmax(self,z):
		return np.exp(z)/np.sum(np.exp(z),axis=1,keepdims=True)


