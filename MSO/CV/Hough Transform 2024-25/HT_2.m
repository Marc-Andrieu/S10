%Read a grayscale image into the workspace and display it.
A = imread('coins.png');
imshow(A)
%Find all the circles with radius r pixels in the range [15, 30].
[centers, radii, metric] = imfindcircles(A,[15 30]);%
%Retain the five strongest circles according to the metric values.
centersStrong5 = centers(1:10,:); 
radiiStrong5 = radii(1:10);
metricStrong5 = metric(1:10);
%Draw the five strongest circle perimeters over the original image.
viscircles(centersStrong5, radiiStrong5,'EdgeColor','b');
%Copyright 2012 The MathWorks, Inc.
