import paddle
from paddle import fluid
from paddle.fluid import layers
import numpy as np
from paddle.fluid.layers import elementwise_add, elementwise_mul, elementwise_sub, log, fill_constant, cast, clip, pow


def focal_loss(pred, label, alpha=0.25, gamma=2, epsilon=1e-6):
    '''
        alpha 变大，对前景类惩罚变大，更加重视
        gamma 变大，对信心大的例子更加忽略，学习难的例子
    '''
    pred = clip(pred, epsilon, 1 - epsilon)
    label = clip(label, epsilon, 1 - epsilon)
    loss = -1 * (alpha * layers.pow((1 - pred), gamma) * label * layers.log(pred) + (1 - alpha) * layers.pow(pred,
                                                                                                             gamma) * (
                             1 - label) * log(1 - pred))
    return loss


y = fluid.data('y', [2, 1], dtype="float32")
y_predict = fluid.data('y_predict', [2, 1], dtype="float32")

program = fluid.default_main_program()
places = fluid.CPUPlace()
exe = fluid.Executor(places)
exe.run(fluid.default_startup_program())

y_value = np.array([[1], [0]], dtype="float32")
y_predict_value = np.array([[0], [1]], dtype="float32")
loss = focal_loss(y_predict, y)

loss_value = exe.run(program, feed={'y': y_value, "y_predict": y_predict_value}, fetch_list=[loss])
print(loss_value)