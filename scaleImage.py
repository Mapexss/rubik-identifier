if __name__ == "__main__":
    print("File scale!")
else:
    import cv2
    class imageScale:
        def __init__(self, scale_percent, masked, image, colored):
            #super().__init__()
            self.scale_percent = scale_percent
            self.masked = masked
            self.image = image
            self.colored = colored
                        
        def changeScale(self, scale_percent, masked, image, colored):
            width = int(image.shape[1] * scale_percent[0] / 100)
            height = int(image.shape[0] * scale_percent[1] / 100)
        
            dimensions = (width, height)
        
            if masked == "T":
                image_resized = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA) # com contorno
                return image_resized
            else:
                image_resized = cv2.resize(colored, dimensions, interpolation = cv2.INTER_AREA) # sem contorno
                return image_resized