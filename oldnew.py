import cv2
import numpy as np

# Orijinal görüntüyü yükle
OriginalImage = cv2.imread("abraham.jpg")

# Maske görüntüsünü yükle (gri tonlamada)
makredDamages = cv2.imread("mask.jpg", 0)

# Maske oluşturmak için eşikleme
ret, thresh = cv2.threshold(makredDamages, 254, 255, cv2.THRESH_BINARY)

# Maskeyi kalınlaştır
kernel = np.ones((7, 7), np.uint8)
mask = cv2.dilate(thresh, kernel, iterations=1)

# Görüntüyü restore et
try:
    restoredImage = cv2.inpaint(OriginalImage, mask, 3, cv2.INPAINT_TELEA)
    cv2.imshow("İyileştirilmiş Fotoğraf", restoredImage)  # Bu satırın hatalı olmasına dikkat edin
except Exception as e:
    print(f"Hata oluştu: {e}")

# Düzeltmiş resmi kaydet
cv2.imwrite("RestoredAbraham.jpg", restoredImage)

cv2.waitKey(0)
cv2.destroyAllWindows()