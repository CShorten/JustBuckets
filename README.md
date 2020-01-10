# JustBuckets
<h5> Automated Highlight Reels from Basketball Games with Deep Convolutional Neural Networks </h5>

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
