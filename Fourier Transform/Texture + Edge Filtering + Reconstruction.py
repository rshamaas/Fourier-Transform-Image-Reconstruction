import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread("PASTE FILE PATH HERE", cv2.IMREAD_GRAYSCALE) # <-----------------------------------------------------

# Perform Fourier Transform
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Get the image dimensions
rows, cols = image.shape
crow, ccol = rows // 2 , cols // 2  # Center of the image
x, y = np.ogrid[:rows, :cols]
distance = (x - crow)**2 + (y - ccol)**2

# Create a Gaussian High-Pass Filter
r_high = 70  # Radius for high-pass filter <-----------------------------------------------------------------------------
sigma_high = r_high / 2  # Standard deviation for high-pass filter (adjust for smoothness)
gaussian_high = 1 - np.exp(-distance / (2 * sigma_high**2))
fshift_high = dft_shift * gaussian_high[:, :, np.newaxis]  # Apply the Gaussian High-Pass Filter to the shifted DFT

# # Inverse DFT for the high-pass filter (edge detection)
f_ishift_high = np.fft.ifftshift(fshift_high)
img_back_high = cv2.idft(f_ishift_high)
img_back_high = cv2.magnitude(img_back_high[:, :, 0], img_back_high[:, :, 1])

# Create a Gaussian Low-Pass Filter
r_low = 40  # Radius for low-pass filter <-------------------------------------------------------------------------------
sigma_low = r_low / 2  # Standard deviation for low-pass filter (adjust for smoothness)
gaussian_low = np.exp(-distance / (2 * sigma_low**2))
fshift_low = dft_shift * gaussian_low[:, :, np.newaxis]  # Apply the Gaussian Low-Pass Filter to the shifted DFT

# Inverse DFT for the low-pass filter (noise reduction)
f_ishift_low = np.fft.ifftshift(fshift_low)
img_back_low = cv2.idft(f_ishift_low)
img_back_low = cv2.magnitude(img_back_low[:, :, 0], img_back_low[:, :, 1])

# Add low-pass and high-pass filtered shifts
fshift_combined = fshift_high + fshift_low

# Inverse DFT for the combined filters
f_ishift_combined = np.fft.ifftshift(fshift_combined)
img_back_combined = cv2.idft(f_ishift_combined)
img_back_combined = cv2.magnitude(img_back_combined[:, :, 0], img_back_combined[:, :, 1])

# Display the results
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(241), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# Edge Detection (High-pass filter)
plt.subplot(242), plt.imshow(img_back_high, cmap='gray')
plt.title('Edge Detection (High-Pass)'), plt.xticks([]), plt.yticks([])

# Noise Reduction (Low-pass filter)
plt.subplot(243), plt.imshow(img_back_low, cmap='gray')
plt.title('Noise Reduction (Low-Pass)'), plt.xticks([]), plt.yticks([])

# Combined Image (Low-pass + High-pass)
plt.subplot(244), plt.imshow(img_back_combined, cmap='gray')
plt.title('Reconstructed Image (Low + High)'), plt.xticks([]), plt.yticks([])

# Magnitude Spectrum
original_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.subplot(245), plt.imshow(original_spectrum, cmap='gray')
plt.title('Original Spectrum'), plt.xticks([]), plt.yticks([])

edge_spectrum = 20 * np.log(cv2.magnitude(fshift_high[:, :, 0], fshift_high[:, :, 1]))
plt.subplot(246), plt.imshow(edge_spectrum, cmap='gray')
plt.title('Edge Spectrum'), plt.xticks([]), plt.yticks([])

texture_spectrum = 20 * np.log(cv2.magnitude(fshift_low[:, :, 0], fshift_low[:, :, 1]))
plt.subplot(247), plt.imshow(texture_spectrum, cmap='gray')
plt.title('Texture Spectrum'), plt.xticks([]), plt.yticks([])

combined_spectrum = 20 * np.log(cv2.magnitude(fshift_combined[:, :, 0], fshift_combined[:, :, 1]))
plt.subplot(248), plt.imshow(combined_spectrum, cmap='gray')
plt.title('Texture Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()

plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img_back_combined, cmap='gray')
plt.title('Reconstructed Image'), plt.xticks([]), plt.yticks([])

plt.show()

