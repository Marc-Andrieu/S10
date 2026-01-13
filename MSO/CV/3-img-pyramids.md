# Image pyrapid and applications

## Template matching

### Method 0: filter the image with eye patch

$$
h[m; n] = \sum_{k, l} g[k; l] \times f[m + k; n + l]
$$

### Method 1: filter the image with zero-mean eye

$$
h[m; n] = \sum_{k, l} (f[k; l] - \bar f) \times g[m + k; n + l]
$$

### Method 2: SSD

$$
h[m; n] = \sum_{k, l} (g[k; l] - f[m + k; n + l])^2
$$

### Method 3: Normalized cross-correlation

Matlab:

```matlab
normxcorr2(template, im)
```

$$
h[m; n] = \dfrac{\displaystyle \sum_{k, l} (g[k; l] - \bar g) \times (f[m - k; n - l] - \bar f_{m, n})}{\displaystyle \sqrt{\sum_{k, l} (g[k; l] - \bar g)^2 \times  \sum_{k, l} (f[m - k; n - l] - \bar f_{m, n})^2}}
$$

## Gaussian pyramid

### Algorithm for downsampling by factor of 2

```matlab
% 1. Start with image(h, w)
% 2. Apply low-pass filter
im_blur = imfilter(image, fspecial('gaussian', 7, 1))
% 3. Sample every other pixel
im_small = im_blur(1:2:end, 1:2:end);
```
