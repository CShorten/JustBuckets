# JustBuckets
<h5> Automated Highlight Reels from Basketball Games with Deep Convolutional Neural Networks </h5>
<h3> Project Motivation </h3>
Before I began my journey studying Deep Learning and Artificial Intelligence, I was playing Division 1 basketball at Florida Atlantic Unversity. In order to get a Division 1 basketball scholarship, I had to spend my Junior -> Senior summer of high school playing in a series of tournaments and camps. 
<br>
<br>
In addition to endorsements from past coaches and camp directors, it helps enormously to have a highlight reel resum&eacute; that college coaches can use to evaluate your fit for their program. Unless you are one of the top players in the country, you will have to make this highlight reel yourself. 
<br>
<br>
Luckily for me, I came across a great program called Scoutsfocus that made these highlight reels for you from a collection of 3 games at their 1-day event. These highlight reels are great, but they cost ~$100 and take about 6-8 weeks to make. 
<br>
<br>
What if a <b>computer vision model</b> could make highlight reels? Costing you $0 and taking a matter of hours rather than weeks. This project explores this idea through a series of Deep Convolutional Neural Networks that crop full length games into individual plays, and extract made baskets from the game. 

<h1> Project Workflow </h1>
The following sections will describe each stage of the pipeline of building a Deep Learning system for this task. The workflow consists of Data Collection --> Data Annotation --> Training Models --> Hyperparameter Optimization --> Performance Analysis. This report ends with a discussion about some ideas around the project such as the generalization of this system, building large image datasets with semi-supervised learning, and adjusting the model in deployment with active learning.

<h1> Data Collection </h1>
Assembling the dataset
<h2> Collection Pipeline </h2>
<ol>
  <li> Download full games from YouTube </li>
  <li> Extract frames with cv2 </li>
    <ul>
      <li> Emphasis on Organization and avoiding naming conflicts between cities and games </li>
      <li> Passed in Source Directory of Games, Name of Game, Directory to write frames in </li>
      <li> ms per frame </li>
      <li> Starting experiments with 20K frames from 5 games | 100K images in dataset </li>
    </ul>
  <li> Resize frames with PIL </li>
    <ul>
       <li> Frames from the original video are 1280 x 720 with averaging ~250 KB with JPEG compression </li>
       <li> Downsize frames 4x to 320 x 180, preserving aspect ratio </li>
       <li> We want to train a detection model to put a bounding box around the rim, which is now ~ 50x100 </li>
       <li> Want to experiment with CIFAR-10 classification to see how much accuracy is impacted by further downsampling the images, e.g. 80% on 32 x 32 --> 60% on 16 x 16 --> ... </li>
    </ul>
</ol>


<h1> Data Annotation </h1>
The otuput of our Data Collection pipeline is 100K 320 x 180 images from 5 different games. We want to label this data to train 3 Deep Convolutional Neural Networks:
<ul>
  <li> Image Classification of Rim vs. No Rim </li>
  <li> Objet Detection of the Rim </li>
  <li> Action Recognition of made baskets </li>
</ul>

An important component of this is that the output of each model is facilitating the data engineering for the next model. Our image classifier first detects wether there is a rim in the image at all. Our object detection model will then find the rim and crop it out for the action recognition model. The action recognition model will take a stack of the k last frames and classify these sequences as either a 'basket' or 'no basket'.

<h1> Training Models </h1>
<h2> Training an Image Classifier </h2>
The first model to train is an image classifier that distinguishes between frames with a rim in the scene or not. Naturally, there cannot be a basket in the video sequence if there isn't even a rim in it. This model will become a part of the data annotation pipeline to preprocess images that do not need to be considered when labeling rims with a bounding box.
<h4> Image Classifier Pipeline </h4>
<ul>
  <li> Load pre-trained ResNet50 </li>
  <li> Data Augmentation Parameters </li>
  <li> Fine-tune on new dataset </li>
</ul>

<h3> Optimizing this workflow is described below in "Hyperparameter Optimization" </h3>

<h2> Training an Object Detector </h2>

<h2> Training an Action Recognition Model with the Markov Property </h2>
The next stage of this pipeline is to detect wether a basket was scored in a given time window or not, easily the most challenging component of this project. 

<h4> The Markov Property? </h4>
There are many ways to think about integrating temporal information into a vision model:
<ul>
  <li> Classify frames individually, use a heuristic or a learned parameter to aggregate scores </li>
  <li> CNN + LSTM </li>
  <li> CNN + Transformer </li>
  <li> 3D CNN </li>
  <li> Stack past frames (Markov Property) </li>
     <ul>
       <li> In AlphaGo, AlphaGo Zero, and AlphaZero, the last 8 states of the game board are stacked together to form the state representation to the agent at the current timestep. </li>
     </ul>
 </ul>

<h1> Notes on this Project </h1>
<h2> Is this a Meta Learning Problem? </h2>
One of the most interesting trends in Deep Learning and AI is Meta-Learning. Meta-Learning can be a confusing term that is thrown around with things like AutoML, Neural Architecture Search, Hypernetworks, or Few-Shot Learning and Task Adaptation. In this context, I use the term "Meta-Learning" to describe task adaptation as is used in <a href = "http://cs330.stanford.edu/">Dr. Finn's CS 330 "Deep Multi-Task and Meta Learning"</a> course (lectures to be uploaded soon).
<br>
<br>
I think we naturally think of applying Meta-Learning to reinforcement learning problems. Examples of this are questions like "How can we train an agent to master 5 atari games and generalize to a 6th?". I think this project shows an interesting examples of where you would want to use Meta-Learning algorithms for classification and detection models trained with supervised, or semi-/self- supervised learning.

