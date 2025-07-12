import mixbox

#print(mixbox.__file__)

rgb1 = (0, 33, 133)  # blue
rgb2 = (252, 211, 0) # yellow
ratio = 0.5              # mixing ratio

rgb_mix = mixbox.lerp(rgb1, rgb2, ratio)

print(rgb_mix)
