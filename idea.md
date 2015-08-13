## ideas

(1) using color tracking         return
This is turning out to be really hard because (a) the bees don't have one blotch of some color on them and (b) even if they did, because of the high densities of bees, it would be difficult to accurately measure the number of bees

(2) using a haar classifer   return
guides include:
- <http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html>
- <https://github.com/jeffThompson/MirrorTest/blob/master/TrainingInstructions.md>
- <http://www.memememememememe.me/training-haar-cascades/>

All of these are pretty advanced and over my head. I've gotten a part of the way there but there's some g++ error (possibly due to a typo in the coding robin tutorial) that's messing me up.

Properly doing this would also require finding a way of cropping all the bees out of the videos frames with the same aspect ratio.

(3) using Ctrax   return
Ctrax is used by a lot of people that study flies to track flies. I've tried it on Rong's videos, modifying many of the parameters, and it doesn't work well at all. The problem stems from the high density of bees in each frame, making it difficult for the program to even understand what shape and size a bee should take.
