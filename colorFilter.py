if __name__ == "__main__":
    print("File colorFilter")
else:
    from numpy import array, int32
    from cv2 import inRange

    class color():
        def __init__(self, hsv):
            super().__init__()
            self.hsv = hsv
            self.low_blue = array([100, 100, 90])
            self.high_blue = array([150, 255, 255])
            self.low_green = array([50, 100, 80])
            self.high_green = array([80, 255, 240])
            self.low_yellow = array([15, 120, 120])
            self.high_yellow = array([45, 255, 255])
            self.low_orange = array([10, 100, 100])
            self.high_orange = array([20, 255, 255])
            self.low_red = array([0, 150, 100])
            self.high_red = array([5, 255, 255])
            self.low_white = array([0, 0, 50])
            self.high_white = array([255, 50, 255])

        def blue(self, hsv):
            color_mask = inRange(hsv, self.low_blue, self.high_blue)
            return color_mask

        def green(self, hsv):
            color_mask = inRange(hsv, self.low_green, self.high_green)
            return color_mask

        def yellow(self, hsv):
            color_mask = inRange(hsv, self.low_yellow, self.high_yellow)
            return color_mask

        def orange(self, hsv):
            color_mask = inRange(hsv, self.low_orange, self.high_orange)
            return color_mask

        def red(self, hsv):  # Luz específica
            color_mask = inRange(hsv, self.low_red, self.high_red)
            return color_mask

        def white(self, hsv):
            color_mask = inRange(hsv, self.low_white, self.high_white)
            return color_mask

        def inRangeColor(self, img, color_mask):
            if (color_mask == 1):
                return inRange(int32(img), self.low_green, self.high_green)
            if (color_mask == 2):
                return inRange(int32(img), self.low_red, self.high_red)
            if (color_mask == 3):
                return inRange(int32(img), self.low_yellow, self.high_yellow)
            if (color_mask == 4):
                return inRange(int32(img), self.low_white, self.high_white)
            if (color_mask == 5):
                return inRange(int32(img), self.low_blue, self.high_blue)
            if (color_mask == 6):
                return inRange(int32(img), self.low_orange, self.high_orange)
