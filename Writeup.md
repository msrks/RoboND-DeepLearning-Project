https://review.udacity.com/#!/rubrics/1155/view

# Project: Follow Me

## Writeup

### 1. Provide a write-up / README document including all rubric items addressed in a clear and concise manner. The document can be submitted either in either Markdown or a PDF format.

You're reading it!

### 2. The write-up conveys the an understanding of the network architecture.

>The student clearly explains each layer of the network architecture and the role that it plays in the overall network.

- encoder network w/  separable convolution layers
- 1x1 conv network
- decoder network

>The student can demonstrate the benefits and/or drawbacks different network architectures pertaining to this project and can justify the current network with factual data. Any choice of configurable parameters should also be explained in the network architecture.

>The student shall also provide a graph, table, diagram, illustration or figure for the overall network to serve as a reference for the reviewer.

### 3. The write-up conveys the student's understanding of the parameters chosen for the the neural network.

>The student explains their neural network parameters including the values selected and how these values were obtained (i.e. how was hyper tuning performed? Brute force, etc.) Hyper parameters include, but are not limited to:
>
- Epoch
- Learning Rate
- Batch Size
- Etc.

>All configurable parameters should be explicitly stated and justified

### 4. The student has a clear understanding and is able to identify the use of various techniques and concepts in network layers indicated by the write-up.

>The student is demonstrates a clear understanding of 1 by 1 convolutions and where/when/how it should be used.

1x1 conv enables `fully convolutional network` (`FCN`) by replacing `fully connected layer`. `FCN` can take input with various size (with, height), and save positional information through passing network.

>The student demonstrates a clear understanding of a fully connected layer and where/when/how it should be used.

`fully connected layer` can utilize all information from input layer. Usually `fully connected layer` is used as the last few layers of CNN.

### 5. The student has a clear understanding of image manipulation in the context of the project indicated by the write-up.

>The student is able to identify the use of various reasons for encoding / decoding images, when it should be used, why it is useful, and any problems that may arise.

`encoder network` can extract abstract features. `decoder network` can use them to generate another image for semantic segmention, image generation, image transformation.

### 6. The student displays a solid understanding of the limitations to the neural network with the given data chosen for various follow-me scenarios which are conveyed in the write-up.

>The student is able to clearly articulate whether this model and data would work well for following another object (dog, cat, car, etc.) instead of a human and if not, what changes would be required.

this network can recognize other objects instead of a human.
but more difficult than human because human has more indivizuality.

## Model
