I presented this as a project in my Modern Physics class, and I am curious to what extent I can improve it as a learning tool. This is a very much a work in progress but can be cool to play with.

## How it works

The image is greyscaled for convenience. It uses numpy to perform the a discrete fourier transform and create gaussian distributions. All the frequencies above a threshold value (high pass filter) are preserved as one image and all the frequenceies below a threshold value (low pass filter) are preserved as another image. Both are combined together to create the reconstructed image. Mathplotlib is used to plot the pixels of the images.

Step by Step for a basic image:

![image](https://github.com/user-attachments/assets/c9ecf49e-89ed-41a9-bc43-3e7be24b70b8)

# Instructions

Copy paste the Python code in your IDE or download it.
1. In line 6, You MUST paste a file path for an image (jpg, png, etc) in the "PASTE FILE PATH HERE".
2. (Optional) In lines 19 and line 30, change the values of r-high and r_low, respectively, as any integer you want to play with it.

You are basically filtering out the frequencies in the range between r-high and r-low in the gaussian distribution. So if r_high and r_low are the same number, you will (obviously) recreate the exact same image since you filtered out nothing. I recommend playing with r_high between 50-90 and r-low between 10-50 for various images.

Example Using Sample Image:

![image](https://github.com/user-attachments/assets/7c756a73-4c1b-4c55-aab5-9c7218ce347f)

#
### Future updates:
 - details of the fourier transform process for learning purposes
 - creating an executable program that requests image file or allows pasting of a screenshot
   - asking for inputs rather than manually adjusting the code
   - replacing mathplotlib for displaying images
   - using a slider in increments to show the varying thresholds, possibly by performing all the combinations and the letting the slider replace what would be shown
 - color
