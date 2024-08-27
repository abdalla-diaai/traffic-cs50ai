# Traffic

## Optimisations tested:

the parameters have been changed once at a time with the rest of parameters fixed.

1. Different numbers of convolutional and pooling layers:
    - did not have any impact on loss or accuracy of the model.

2. Different numbers and sizes of filters for convolutional layers:
    - did not have any impact on loss or accuracy of the model.

3. Different pool sizes for pooling layers:
    - did not have any impact on loss or accuracy of the model.

4. Different numbers and sizes of hidden layers:
    - higher number of hidden networks increased accuracy significantly. 

5. Dropout:
    - reducing dropout between 0.2-0.4 increased accuracy of the model but is posing a risk of overfitting.

## Summary

The hidden network number will only be increased to boost accuracy and leaving the rest of the parameters fixed.