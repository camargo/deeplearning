import numpy as np

layer_output = np.array(
    [
        [22.0, 33.0, 44.0, 55.0, 66.0],
        [22.0, 33.0, 44.0, 55.0, 66.0],
    ]
)

print(layer_output.shape)
print(layer_output)
layer_output *= np.random.randint(0, high=2, size=layer_output.shape)
print(layer_output)
layer_output /= 0.5
print(layer_output)
