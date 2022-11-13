if __name__ == "__main__":
    print("File imageFilter!")
else:
    #from cv2 import GaussianBlur, adaptiveThreshold, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY
    import cv2
    class filters:
        def __init__(self) -> None:
                super().__init__()
        
        def blurFilter(self, image):
            blurred = cv2.GaussianBlur(image, (5, 5), 0)
            return blurred
        
        def saturationFilter(self, image):
            #hsv[:,:,1] = greenMask 
            pass