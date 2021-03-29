import paddle
from paddle import fluid
from paddle.fluid import layers
import numpy as np
def mse_loss(pred,label):
    loss = layers.pow((pred-label),2)
    loss = layers.mean(loss)
    return loss
y = fluid.data('y',[2,2],dtype='float32')
y_predict = fluid.data('y_predict',[2,2],dtype='float32')
loss = mse_loss(y_predict,y)
program = fluid.default_main_program()
places = fluid.CPUPlace()
exe = fluid.Executor(places)
y_value = np.array([[1,2],[3,4]],dtype='float32')
y_predict_value = np.array([[5,6],[7,8]],dtype='float32')
loss_value =exe.run(program,feed={'y':y_value,'y_predict':y_predict_value},fetch_list=[loss])
print(loss_value)