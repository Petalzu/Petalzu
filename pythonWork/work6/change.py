import pickle
import os

class ImageError(Exception):
    pass


class CoordinateError(ImageError):
    pass


class Image:
    def __init__(self, width, height, filename="", background="#FFFFFF"):
        self.filename = filename
        self.background = background
        self.data = {}
        self.width = width
        self.height = height
        self.colors = {self.background}

    def __getitem__(self, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
                not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        return self.data.get(tuple(coordinate), self.background)

    def __delitem__(self, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
                not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        self.data.pop(tuple(coordinate), None)

    def __setitem__(self, coordinate, color):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
                not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        if color == self.background:
            self.data.pop(tuple(coordinate), None)
        else:
            self.data[tuple(coordinate)] = color
            self.colors.add(color)

    def save(self, filename=None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            data = [self.width, self.height, self.background, self.data]
            fh = open(self.filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def load(self, filename=None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            fh = open(self.filename, "rb")
            data = pickle.load(fh)
            (self.width, self.height, self.background,self.data) = data
            self.colors = (set(self.data.values()) | {self.background})
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def export(self, filename):
        if filename.lower().endswith(".xpm"):
            self.__export_xpm(filename)
        else:
            raise ExportError("unsupported export format: " +os.path.splitext(filename)[1])


border_color = "#FF0000"  # red
square_color = "#0000FF"  # 5blue
width, height = 240, 60
midx, midy = width // 2, height // 2
image = Image(width, height, "square_eye.img")
for x in range(width):
    for y in range(height):
        if x < 5 or x >= width - 5 or y < 5 or y >= height - 5:
            image[x, y] = border_color
        elif midx - 20 < x < midx + 20 and midy - 20 < y < midy + 20:
            image[x, y] = square_color

Image.save()
Image.export("square_eye.xpm")
