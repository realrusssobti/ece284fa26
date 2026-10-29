
For this assignment, you should inspect the architectures of **VGGNet16** and **ResNet20** (defined in models/vgg.py and models/resnet.py, respectively) and create two Jupyter notebooks, one for each model, completing both parts of the assignment in each notebook.

**Part I: Training VGGNet16 and ResNet20 (20 points)**

* Train ResNet20 and VGGNet16 on the CIFAR-10 dataset to achieve greater than 90% classification accuracy on the test set.
* Use the template provided in [Code7]_CNN_Training_for_CIFAR10.ipynb. You can make two copies of this notebook and rename them for VGGNet16 and ResNet20 and change the model initialization in each notebook to VGG16() and resnet20_cifar(), respectively. (If your copies are not in the same directory as the original [Code7], remember to update the model import path.)
* The training process is similar for both models, but achieving the required accuracy may require some hyperparameter tuning. You are allowed to modify training-related hyperparameters as well as the optimizer and learning-rate scheduler, just don't modify the original model architectures.

**Note:** For your final submission, please remove the training logs (intermediate loss values, epoch-by-epoch outputs, etc.) from your notebooks. Only the final evaluation results on the test set should be displayed. To do so:

1. Save your trained models in the result/ folder. (The save_checkpoint() function in [Code7] demonstrates how to save model checkpoints. For more details about saving and loading trained models, refer to the PyTorch documentation: [https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html**Links to an external site.**](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html) )
2. Restart and clear the notebook outputs by selecting Kernel → Restart & Clear Output in Jupyter Notebook.
3. Reload your saved model checkpoints for VGGNet16 and ResNet20, switch the models to evaluation mode using model.eval(), and evaluate them on the test set to display the final accuracy. You do not need to retrain the models after restarting the kernel.

**Part II: Manual Calculation of Layers (20 points)**

* Investigate the internal structure and computations of both models by extracting intermediate activations and manually reproducing selected layer operations.
* Refer to the example provided in [Code6]_CNN_for_MNIST.ipynb to register forward pre-hooks on the target layers. (In [Code6], forward pre-hooks are registered on all convolutional layers, the register_forward_pre_hook() method registers a function that is called before a module's forward() method executes, allowing you to capture the input tensor of that module, you can adapt this example to register hooks on other layer types. For more details, refer to the PyTorch documentation: [https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_forward_pre_hook **Links to an external site.**](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_forward_pre_hook))
* **For VGGNet16:** Capture the input of the first ReLU layer and manually reproduce the operations required to compute the input of the first MaxPool2d layer. (By "manually reproduce," we mean that you should not treat the entire model as a black box by simply calling model(input) to obtain the target output. Instead, you should inspect the model architecture and explicitly apply the required operations in the correct order. You do not need to implement individual operations from scratch, you may access the corresponding layers and their trained parameters directly from the model, or use equivalent PyTorch functions such as torch.nn.functional.relu() for simple activation operations. The purpose of this task is to help you become familiar with the model architecture and understand which operations the input activation passes through. )
* **For ResNet20:** Capture the input of the conv1 layer in BasicBlock0 and manually reproduce the operations required to compute the input of the conv1 layer in BasicBlock1. (You may consider the residual connection of the ResNet architecture.)
* **For both models:** Compare your manually computed results with the corresponding reference activations captured using forward pre-hooks. You may use any reasonable method to demonstrate whether the results match. (Small numerical differences due to floating-point precision are acceptable.)
* You only need to perform the manual computation and comparison for one test case (one input image or one item from a batch) for each model.

**Deliveries: 2 PDF Files and 1 ZIP File**

* Submit two PDF files, one for VGGNet16 and one for ResNet20. Remove intermediate training logs from the PDF submissions as instructed in Part I.
* Compress both completed .ipynb files into one ZIP file and submit it along with the two PDF files.

**Frequently Asked Questions (FAQ)**

**Q1. For Part I, can the models achieve the required accuracy by only changing training hyperparameters, such as the learning rate, number of epochs, and momentum?**

Yes. Both models can achieve the required accuracy by tuning the training parameters. You may adjust the learning rate, number of epochs, momentum, batch size, optimizer, and learning-rate scheduler. There is no need to modify the model architectures.

**Q2. Can I train a different model, such as VGGNet10, instead of VGGNet16 or ResNet20?**

No. You must train the two specified models, VGGNet16 and ResNet20, to receive full credit.

**Q3. Should we use vgg_quant.py or resnet_quant.py for this assignment?**

No. Please use the original, unquantized models defined in models/vgg.py and models/resnet.py.
