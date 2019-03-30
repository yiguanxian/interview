"""
Implement 2D convolution layer forward
including:
	zero padding
	convolution single step:计算一个像素点值
	convolution forward
"""
import numpy as np
def zero_pad(X, pad):
	"""
	X -- numpy array,with shape(m,n_h,n_w,n_c)
	pad -- integer, amount of padding around each image on vertical and horizontal dimensions
    
	"""
	X_pad = np.pad(X, ((0,0), (pad,pad), (pad,pad), (0,0)), "constant", constant_values=0)
	return X_pad

def conv_single_step(a_slice_prev, W, b):
    """
    Apply one filter defined by parameters W(一个filter表示W) on a single slice (a_slice_prev) of the output activation 
    of the previous layer(在前一层的激活或隐藏状态上进行卷积).
    
    Arguments:
    a_slice_prev -- slice of input data of shape (f, f, n_C_prev)
    W -- Weight parameters contained in a window - matrix of shape (f, f, n_C_prev)
    b -- Bias parameters contained in a window - matrix of shape (1, 1, 1)
    
    Returns:
    Z -- a scalar value, result of convolving the sliding window (W, b) on a slice x of the input data
    """
    Z = float(np.sum(a_slice_prev * W) + b)
    return Z

def conv_forward(A_prev, W, b, stride, pad):
    """
    Implements the forward propagation for a convolution function
    
    Arguments:
    A_prev -- output activations of layer(前一层的隐藏或叫激活状态即前一层输出的特征图),the numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    W -- Weights, numpy array of shape (f, f, n_C_prev, n_C)
    b -- Biases, numpy array of shape (1, 1, 1, n_C)
        
    Returns:
    Z -- conv output, numpy array of shape (m, n_H, n_W, n_C).用Z表示没有激活过程，激活了用A
   
    """ 
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    (f, f, n_C_prev, n_C) = W.shape
  
    n_H = int((n_H_prev + 2 * pad - f) / stride) + 1
    n_W = int((n_W_prev + 2 * pad - f) / stride) + 1
	# 因为前面辅助函数可以卷积计算输出中的每一个像素点，现在需要初始化输出，然后填充计算值  
    Z = np.zeros((m, n_H, n_W, n_C))
    # 卷积前先padding，宽高同pad数
    A_prev_pad = np.pad(A_prev, ((0,0), (pad,pad), (pad,pad), (0,0)), "constant", constant_values=0)
 	
 	"""
 	
 	遍历一个batch输入样本的每一个输入块,遍历顺序参考输出维度(m, n_H, n_W, n_C)
 	
 	特点是：
        遍历顺序即为生成维度的顺序，反过来可以根据要生成的维度顺序来执行遍历过程。
    解读是：
    	对于本卷积层的输出维度(m, n_H, n_W, n_C),应该解读为有m个立方体，每个立方体由n_H个平面从下往上摞起来，每个平面由n_W条线构成，每条线由n_C个点构成
    	所以应该先遍历m个立方体，再遍历n_H个平面，再遍历平面中的n_W条线，再遍历线中的n_C个点。
    
    """
    for i in range(m):                               
        a_prev_pad = A_prev_pad[i] # 冒号是切片，一个值是按索引去那个维度上的值。此处表示取第i+1个立方体即第i+1个样本                    
        for h in range(n_H):
            for w in range(n_W):
                for c in range(n_C):
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                  
                    a_slice_prev = a_prev_pad[vert_start : vert_end, horiz_start : horiz_end, :]
                    Z[i, h, w, c] = np.sum(W[:, :, :, c] * a_slice_prev) + b[0, 0, 0, c]
                                         
    # Making sure your output shape is correct
    assert Z.shape == (m, n_H, n_W, n_C),"Z'shape is unexpected!"
    return Z