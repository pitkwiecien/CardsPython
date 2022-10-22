import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import ravel

import constants as const
from exceptions.file_name_error import FileNameError
from exceptions.file_path_error import FilePathError


def draw(drawn_deck, save_file=None):
    figure, axes_list = plt.subplots(
        4, 13,
        figsize=(11.5, 5)
    )

    plt.subplots_adjust(
        left=0.01,
        right=0.99,
        bottom=0.03,
        top=0.97,
        wspace=0.1,
        hspace=0.1
    )

    for axis in ravel(axes_list):
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        img_name = drawn_deck.get_next().image
        img = mpimg.imread(str(const.PATH.joinpath(img_name).resolve()))
        axis.imshow(img)

    if save_file is None:
        plt.show()
    else:
        try:
            plt.savefig(save_file)
        except (OSError, ValueError) as e:
            raise FilePathError if type(e) is FileNotFoundError else FileNameError()

