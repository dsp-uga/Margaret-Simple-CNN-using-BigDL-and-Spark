# Project Title

## Descriptions of Files here - 

NW_architecture.png (basic png architecture of a simple network which can easily give around 97% acc)
X_test1,X_train1,y_train1 are numpy arrays containing the 32x32 image files (we can directly use them for now and then later on just add a preprocess files)
Modular Preprocess reads from the X_train hash file and the Y_train has files provided
Modular Preprocess_test reads from the X_test hash file provided and creates the images
You can resize them directly in the script or resize them somewhere else to desired size. 
One Paragraph of project description goes here

## Really great Multi class weighted softmax loss function - 
https://gist.github.com/wassname/ce364fddfc8a025bfab4348cf5de852d

## Nice guide to installing Maven 3.5.x
https://www.vultr.com/docs/how-to-install-apache-maven-on-ubuntu-16-04

## Problem Definition

Microsoft Malware Classification Challenge requires us to process a set of text files containing binaries/asm and classify it into one of the 9 types of malwares listed.

## Changing Modalities

Owing to the large dataset size we require a distributed setting to handle it. However an alternative approach would be to change the modalities and represent the problem as a image classification problem.
Since each malware class has a distinct signature it is intuitive that a convolution network working on the image representation of the problem would give reasonable result.
In order to convert the bytes file into a image, we encode the Hex-pair into their decimal representation, and represent that as a pixel intensity.
The advantage of this method is that the convolution network automatically implements a n-gram model using the moving windows. Another and more useful advantage of changing modalities is the size of the files. 
Even without any rescaling the size of the file reduces by a tenth of its original size. After that we do scaling and downsample the images of size X,16 (where X depends on the number of lines in the bytes file), to 32x32 resolution.
After this preprocessing step, the total size of the training and testing dataset falls under 30 megabytes. 

## Observations

Size of the images - 

In order to run a convolution neural network we need the images to be of the same size. Since the X in X,16 depending on the number of lines in the malware's byte file is variable, we downsampled the images to various sizes namely 16x16,
32,32 64,64 128,128 256,256 512,512. We observed that the performance of the neural networks were indifferent to the size of the image. This is intuitive since even at the highest resolution of 512x512 we are downsampling images of maybe a few thousands of lines into a meagre 512 rows. As such we decided to stick to 32x32 images.

Network Depth - 

A network using 3 convolution layers of feature maps 32, 64, 128 respectively followed by a fully convolutional layer of 256 feature maps and (1x1) filter size gives a reasonable performance of 96.7% accuracy on the test set. Blindly stacking layers on top of each other causes overfitting and increase in the training time, without having any noticeable improvement in the results.

Duplicating images before downsampling - 

Another important feature to note is the downsampling strategy. If we directly downsample the image of size (X,16) into any other resolution other than 16x16 or 32x16 and so on, the performance falls by a percentage or so.
Instead it is beneficial to duplicate the image horizontally and convert the X,16 into X,32 before doing 32x32 downsampling. If we wanted 512x512 we would first duplicate our image to X,512 and then downsample to 512x512.

Optimization functions - 

Through experimentation we determine that Adagrad Optimizer is the best optimizer for the problem at hand.

Weighted Loss function - 

Since the classes are not balanced we use a weighted softmax layer. 


### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
