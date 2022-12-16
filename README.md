# Descripción
El presente proyecto consta del diseño de un sistema para la recolección de envases con un robot UR3e usando un modelo de clasificación de imágenes basado en redes neuronales.

![Imagen de demostración](assets/results.png)

El código del trabajo se encuentra en la carpeta code. A continuación se explicará qué contiene cada archivo y cómo ejecutarlos.

Para correr la mayoría de códigos es necesario contar con las librerías:
* TensorFlow
* TensorFlowHub
* Numpy
* Matplotlib
* Pandas

## WasteDetector.ipynb
Este Jupyter Notebook contiene todo el proceso desde la descarga y separación del dataset hasta el entrenamiento y guardado del modelo de clasificación. 
El correr este código implica que los datos obtenidos previamente serán reemplazados por los obtenidos al correr nuevamente las celdas del notebook.

Se recomienda usar desde GoogleColab. 

## PredictWaste.ipynb
Este Notebook permite probar el modelo de clasificación obtenido de WasteDetector.ipynb con cualquier imagen, para ejecutar este archivo de manera local se debe clonar el repositorio. Si se desea probar con alguna imagen que no esté en la carpeta images, se debe cargar la imagen a dicho directorio y crear una nueva celda en el notebook con la siguiente información:

![Imagen de demostración](assets/new_prediction.png)
