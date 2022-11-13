class main:

    def __init__(self) -> None:
        super().__init__()
        self.masked = None
        self.scale_percent = None

    def applyFilters(self) -> None:

        url = "http://192.168.0.103:8080/photo.jpg"
        # url = "http://192.168.0.102:8080/video"

        from requests import get
        import numpy as np
        # from urllib.request import urlopen
        from colorFilter import color
        from scaleImage import imageScale
        from imageFilter import filters

        def desenha_retangulo(image, x, y, w, h):
            roi = []

            for i in range(1, 7, 2):
                for j in range(1, 7,  2):

                    var = (int(((x+w * (i / 3)) + x)/2),
                           int(((y+h * (j / 3)) + y)/2))

                    roi.append(image[var[1]-10:var[1]+10, var[0]-10:var[0]+10])
                    image = cv2.rectangle(
                        image, (var[0] - 30, var[1] - 30), (var[0] + 30, var[1] + 30), (0, 0, 255), 5)
            return image, roi

        def calcula_mediaCor(roi):
            mediaR = 0
            mediaG = 0
            mediaB = 0
            count = 0
            media2 = []
            cores = []
            corResultado = 0
            for i in roi[0][0]:
                count += 1
                mediaR += i[0]
                mediaG += i[1]
                mediaB += i[2]
                # media.append(np.sum(regiao))

            for j in range(3):
                resultado: tuple[int, int, int] = (int(mediaR/count),
                                                   int(mediaG/count),
                                                   int(mediaB/count))
                print(resultado)
                print('1')
                if (resultado):
                    estaNoRange = classeCor.inRangeColor(resultado, j)

                    if (estaNoRange):
                        for corResultado in range(1, 7):
                            return corResultado

            # cores.append(i.inRangeColor(resultado, cor))

            return corResultado

        while True:

            image_resp = get(url)
            if image_resp is None:
                print('Error abrindo a imagem image!')
                return -1

            image_array = np.array(
                bytearray(image_resp.content), dtype=np.uint8)

            image = cv2.imdecode(image_array, -1)

            k = filters()
            blurred = k.blurFilter(image)

            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            classeCor = color(hsv)

            colorFiltered = classeCor.green(hsv)  # mudar cor do filtro

            colored = cv2.bitwise_or(
                blurred, image, mask=colorFiltered)

            contornos, _ = cv2.findContours(
                colorFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            for contorno in contornos:
                area = cv2.contourArea(contorno)
                if area > 135000:
                    x, y, w, h = cv2.boundingRect(contorno)
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                    image, roi = desenha_retangulo(image, x, y, w, h)

                    #mediaCor = calcula_mediaCor(roi)

                    # image = desenhar_circulos(image, x, y, w, h)
                    # var1: tuple = (int(((x+w / 3) + x)/2),int(((y+h / 3) + y)/2))

                    #  cv2.circle(image, var1, 5, (0, 0, 255), -1)
                    # cv2.drawContours(
                    #    colored, contorno, -1, (255, 255, 255), 3)

            j = imageScale(self.scale_percent, self.masked, image, colored)
            result1 = j.changeScale([50, 50], "T", image, colored)
            result2 = j.changeScale([50, 50], "F", image, colored)

            # result1 = cv2.rectangle(
            #    result1, (345, 130), (545, 330), (255, 255, 255), 2)

            cv2.imshow("Frame", result1)
            cv2.imshow("Mask", result2)

            key = cv2.waitKey(1)
            if key == 27:
                break

    def debug_camera(self):
        index = 0
        arr = []
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                arr.append(index)
            cap.release()
            index += 1
        return arr


if __name__ == "__main__":
    import cv2
    p = main()
    p.applyFilters()
    # p.debug_camera()
