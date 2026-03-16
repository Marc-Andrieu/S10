from pathlib import Path
import cv2
import numpy

PATH_IMAGE = Path(__file__).parent

image_input = cv2.imread(str(PATH_IMAGE / "image_test.jpg"))
image_grey = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_grey, (5, 5), 0)
# Canny pour choper les bords des objets
image_edges = cv2.Canny(image_blur, 100, 200)

cv2.imwrite(str(PATH_IMAGE / "out_canny.jpg"), image_edges)

# Transformée de Hough pour en tirer des lignes
lines = cv2.HoughLinesP(image_edges, 1, numpy.pi / 180, 100, maxLineGap=5) # Résolution linéaire 1 px, angulaire pi/180, treshold 50 (au pif), maxLineGap 50 (bien guez, trouver mieux)

# Tri des lignes pour ne garder que les plus longues
longest_line_length = 0
for line in lines: # Qui a la plus longue?
    x1, y1, x2, y2 = line[0]
    line_length = numpy.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    longest_line_length = max(longest_line_length, line_length)

# On tej les courtes
filtered_lines = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    line_length = numpy.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if line_length >= 0.5 * longest_line_length:
        filtered_lines.append(line)

for line in filtered_lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image_input, (x1, y1), (x2, y2), (0, 255, 0), 2)

image_output = image_input

cv2.imwrite(str(PATH_IMAGE / "out_lines.jpg"), image_output)