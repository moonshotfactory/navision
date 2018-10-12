import skimage
from skimage import data

import warnings
warnings.filterwarnings('ignore')


def main():
    cat = data.chelsea()
    print(type(cat))
    print(cat.shape)

    # Select reddish pixels
    mask_reddish = cat[:, :, 0] > 160

    # Change to green
    cat[mask_reddish] = [0, 255, 0]

    # Resize image
    new_image = skimage.transform.resize(cat, (128, 256, 3))
    skimage.io.imsave('mycat.png', new_image)
    skimage.io.imshow(new_image)


if __name__ == "__main__":
    main() 
