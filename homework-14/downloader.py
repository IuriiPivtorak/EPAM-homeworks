import urllib.request
from PIL import Image
import os
import sys
import argparse
from queue import Queue
from threading import Thread
from time import time


def create_parser():
    """
    Parser function for console commands.

    :returns: argparse class object - parser.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('links', nargs='?')
    parser.add_argument('--dir', nargs='?', default=os.getcwd())
    parser.add_argument('--threads', nargs='?', default='1')
    parser.add_argument('--size', nargs='?', default='100x100')
    return parser


error_counter = 0
file_counter = 0
bytes_downloaded = 0


def downloader(image_url, size, name, directory):
    """
    Function for downloading and resizing images.

    :param image_url: url of image to download.
    :type image_url: str.
    :param size: width x height of final image.
    :type size: str.
    :param name: name of filename with image.
    :type name: str.
    :param directory: directory for image to save in.
    :type directory: str.
    :returns: None.
    """
    full_file_name = os.path.join(directory, '{}.jpeg'.format(str(name)))
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        my_req = urllib.request.urlopen(image_url)
        a, b = size.split('x')
        im = Image.open(my_req)
        res_im = im.resize([int(a), int(b)], Image.ANTIALIAS)
        res_im.save(full_file_name)
        im.close()
        print('file {} done!'.format(name))
        global file_counter
        file_counter += 1
        global bytes_downloaded
        bytes_downloaded += int(my_req.info()['Content-Length'])
    except Exception as err:
        print('file {} error: {}'.format(name, err))
        os.remove(full_file_name)
        global error_counter
        error_counter += 1


if __name__ == '__main__':
    start = time()


    def worker():
        """
        Function to put into each thread.

        :returns: None.
        """
        with open(namespace.links) as f:
            content = f.readlines()
        while True:
            items = q.get()
            downloader(items, namespace.size, content.index(items), namespace.dir)
            q.task_done()

    def names():
        """
        Function-generator for getting future filenames of images.

        :returns: None.
        """
        try:
            with open(namespace.links) as file:
                context = file.readlines()
                for x in context:
                    yield x
        except FileNotFoundError:
            print('Error: no such file!')
            sys.exit()

    parser = create_parser()
    namespace = parser.parse_args()
    if not os.path.exists(namespace.dir):
        os.makedirs(namespace.dir)
    if namespace.links:
        q = Queue()
        for i in range(int(namespace.threads)):
            t = Thread(target=worker)
            t.setDaemon(True)
            t.start()

        for item in names():
            q.put(item)

        q.join()

        print('{} file(s) saved'.format(file_counter))
        print('{} error(s)'.format(error_counter))
        print('{} bytes downloaded'.format(bytes_downloaded))

        end = time()
        timed = end - start
        print('time took: {}'.format(timed))

    else:
        raise FileNotFoundError('please, input links folder!')
