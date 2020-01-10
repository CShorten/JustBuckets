# JustBuckets
Extract Made Baskets from Basketball Games

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
