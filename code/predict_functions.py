import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image

# process_image
def process_image(image):
    """
    Input:
    @image = Image to be processed in the form of a numpy array
    Return:
    @image = Image in the form of a numpy array with shape (224, 224, 3)
    """
    # 1. Convert to a TensorFlow tensor
    image_tf = tf.convert_to_tensor(image)
    # 2. Resize image with tf.image.resize
    image_resized = tf.image.resize(image_tf, [224, 224])
    # 3. Normalize: Divide pixel values by 255 to get floats in range [0, 1]
    image_resized /= 255
    # 4. Convert back to Numpy using .numpy()
    image_np = image_resized.numpy()
    return image_np

# predict
def predict(image_path, top_k=1):
    """
    Input:
    @image = Image to be classified
    @model = Model that will predict the output
    @top_k = The first top_k numbers of predicted classes
    Return:
    name = Name of the predicted class
    max_pred = Probability of the top predicted class
    """
    classes = ['Can', 'Glass', 'HDPEM', 'PET']

    # 0. Load model
    keras_model = 'waste_detector_model.h5'
    model = tf.keras.models.load_model(keras_model,
                                       custom_objects = {
                                           'KerasLayer': hub.KerasLayer},
                                       compile=False)
    # 1. Load image given image_path using Image.open()
    image = Image.open(image_path)
    # 2. Convert image to numpy array np.asarray()
    image_np = np.asarray(image)
    # 3. process_image()
    image_processed = process_image(image_np)
    # 4. np.expand_dims() to add the extra dimension (1, 224, 224, 3)
    image = np.expand_dims(image_processed, axis = 0)
    # 5. Pass image to model
    predictions = model.predict(image)

    pred_list = list(predictions[0])
    max_pred = max(pred_list)
    predict_index = pred_list.index(max_pred)
    name = classes[predict_index]
    return name, max_pred*100