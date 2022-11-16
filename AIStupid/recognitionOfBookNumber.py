import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

class StupidBook:
    def stupid(self, bookImg, camNum):
        
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        path = './files'
        img_name = bookImg
        full_path = path + '/' +img_name
        img_ori = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
        img_copy = img_ori.copy()
        img_cut = img_copy[500:600,40:900]
        plt.imshow(img_cut, cmap='gray')
        cv2.waitKey(0)
        
        text = pytesseract.image_to_string(img_cut,config='--psm 6')
        bookNumArr = text.split("\n")[1]
        print(bookNumArr)
        bookNum = bookNumArr.split(" ")
        diffBook = []
        for i in range(len(bookNum)):
            if(bookNum[i] != camNum):
                print(bookNum[i])
                number = ""
                for i in bookNum[i]:
                    print(i)
                    if(i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0'):
                        number += i
                if len(number) == 3 and number != '200':
                    diffBook.append(number)
            else :
                pass
            
        return diffBook