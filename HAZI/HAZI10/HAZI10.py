# %%
import tensorflow as tf
import numpy as np

# %%
'''
Készíts egy metódust ami a mnist adatbázisból betölti a train és test adatokat. (tf.keras.datasets.mnist.load_data())
Majd a tanitó, és tesztelő adatokat normalizálja, és vissza is tér velük.


Egy példa a kimenetre: train_images, train_labels, test_images, test_labels
függvény neve: mnist_digit_data
'''

# %%
def mnist_digit_data():
    digits= tf.keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = digits.load_data()
    return  (train_images/ 255.0, train_labels), (test_images/ 255.0, test_labels)
#d=mnist_digit_data()
#print(d[0][0])


# %%
'''
Készíts egy neurális hálót, ami képes felismerni a kézírásos számokat.
A háló kimenete legyen 10 elemű, és a softmax aktivációs függvényt használja.
Hálon belül tetszőleges számú réteg lehet.


Egy példa a kimenetre: model,
return type: keras.engine.sequential.Sequential
függvény neve: mnist_model
'''

# %%
def  mnist_model():
    model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),# 28*28 vektor lesz belőle
    tf.keras.layers.Dense(128, activation='relu'), # 128 neuron
    tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model
#model=mnist_model()

# %%
'''
Készíts egy metódust, ami a bemeneti hálot compile-olja.
Optimizer: Adam
Loss: SparseCategoricalCrossentropy(from_logits=False)

Egy példa a bemenetre: model
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_compile
'''

# %%
def model_compile(model) -> tf.keras.Sequential:
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])
    return model
#complied_m=model_compile(model)

# %%
'''
Készíts egy metódust, ami a bemeneti hálót feltanítja.

Egy példa a bemenetre: model,epochs, train_images, train_labels
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_fit
'''

# %%
def model_fit(model,epochs,train_images,train_labels):
    model.fit(train_images, train_labels, epochs=epochs)
    return model
#fit_m=model_fit(complied_m,10,d[0][0],d[0][1])

# %%
'''
Készíts egy metódust, ami a bemeneti hálót kiértékeli a teszt adatokon.

Egy példa a bemenetre: model, test_images, test_labels
Egy példa a kimenetre: test_loss, test_acc
return type: float, float
függvény neve: model_evaluate
'''

# %%
def model_evaluate(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    return (test_loss,test_acc)
#print(model_evaluate(fit_m,d[1][0],d[1][1]))

