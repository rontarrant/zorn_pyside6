import mixbox

rgb1 = (0, 33, 133)  # blue
rgb2 = (252, 211, 0) # yellow
t = 0.5              # mixing ratio

rgb_mix = mixbox.lerp(rgb1, rgb2, t)

print("rgb1: ", rgb1)
print("rgb2: ", rgb2)
print("rgb_mix:", rgb_mix)
