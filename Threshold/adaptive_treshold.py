import os
import cv2

# قراءة الصورة
img = cv2.imread(os.path.join('.', 'img', 'handwriting.jpg'))

# التحقق من تحميل الصورة
if img is None:
    print("❌ لم يتم تحميل الصورة، تأكد من المسار الصحيح.")
    exit()

# استخراج المقاس
height, width = img.shape[:2]
size_text = f"{width} x {height} px"

# إضافة المقاس على الصورة الأصلية
cv2.putText(img, size_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
            2, (0, 0, 255), 3, cv2.LINE_AA)

# تصغير الصورة للعرض فقط (مثلاً 800 بكسل عرض)
scale_width = 800
scale_height = int((scale_width / width) * height)
resized = cv2.resize(img, (scale_width, scale_height))

# تحويل الصورة إلى رمادية
img_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# تحويل إلى أبيض وأسود - عتبة ثابتة
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# تحويل إلى أبيض وأسود - عتبة تكيفية
adaptive_img = cv2.adaptiveThreshold(img_gray, 255, 
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 19, 10)

# عرض النتائج
cv2.imshow("Resized Image", resized)
cv2.imshow("Threshold (Fixed)", thresh)
cv2.imshow("Adaptive Threshold", adaptive_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
