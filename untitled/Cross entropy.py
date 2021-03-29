import paddle
from paddle import fluid
from paddle.fluid import layers
import numpy as np


def bce(pred, label, epsilon=1e-05):
    label = layers.clip(label, epsilon, 1 - epsilon)
    pred = layers.clip(pred, epsilon, 1 - epsilon)

    loss = -1 * (label * layers.log(pred) + (1 - label) * layers.log(1 - pred))
    return loss


y = fluid.data("y", [2, 1], "float32")
y_predict = fluid.data("y_predict", [2, 1], "float32")
y_predict = layers.sigmoid(y_predict)
loss = bce(y, y_predict)

program = fluid.default_main_program()
places = fluid.CPUPlace()
exe = fluid.Executor(places)

y_value = np.array([[1], [0]], dtype="float32")
y_predict_value = np.array([[0], [1]], dtype="float32")

loss_value = exe.run(program, feed={'y': y_value, "y_predict": y_predict_value}, fetch_list=[loss])
print(loss_value)