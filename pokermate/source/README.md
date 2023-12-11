----------------------------------------------------------------
README

Object Detection using YOLO (You only look once) version 7.0 
on a deck of playing cards.
----------------------------------------------------------------

Object detection is basically a Neural Network application which intends to identify objects in an image or video. It's part of a much larger group of applied deep learning called Computer Vision (CV), and is one of the most influential and impactful sections in AI.

There are many terms in CV that refer to detection:

	- Object Classification: Classify an input image as a whole into one or more classes.

	- Object Segmentation: Detect parts of an input image which are different from other parts.

	- Object Detection: Detect parts of an input image and classify them into one or more classes. In a nutshell, OD = Object Segmentation + Object Classification.


There have been numerous object detection nerual network architectures and some of them have set high benchmarks. Mostly around 2018s, NN architectures such as Faster RCNN, Yolo came into picture which have transformed the way Object Detection works.

Object detection is generally categorized into 2 broad stages:-

	- Single-stage object detectors: Detectors which look at an image just once, perform computations in the network, and output a response. E.g.
			- YOLO
			- SSD

	- Two-stage object detectors: Detectors which detect object in multuple iterations, going back-and-forth the image to classify parts of it. E.g.
			- Mask R-CNN
			- R-CNN
			- Faster R-CNN


YOLO could be analogus to Attention Weights in Neural Networks, or GPT series in Language models in terms of populatrity, usability and widespread application/adoption.

This project aims to apply YOLO version 7.0 for detecting a playing card along with its suit. A Streamlit UI shall enable users to upload a photo clicked from any electornic device such as Mobile, Tablet, Camera to name a few. Given the user-uploaded input photo (image), the model should be able to detect a playing card in it, and identify its value and suit. 

