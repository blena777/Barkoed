[app]

# عنوان تطبيقك
title = BarcodeApp

# اسم الحزمة
package.name = barcodeapp

# نطاق الحزمة (مطلوب للتعبئة على منصة الأندرويد/آي أو إس)
package.domain = org.yourdomain

# مصدر الشفرة حيث يوجد ملف main.py
source.include_exts = py,png,jpg,kv,atlas

# إصدار التطبيق
version = 0.1

# قائمة بالمتطلبات الخاصة بالتطبيق
requirements = python3, kivy, opencv-python, pyzbar, qrcode[pil]

[buildozer]

# مستوى السجل (0 = فقط الأخطاء، 1 = معلومات، 2 = تفصيل العملية (مع إخراج الأوامر))
log_level = 2

# إظهار تحذير إذا تم تشغيل buildozer كمستخدم root (0 = خطأ، 1 = صحيح)
warn_on_root = 1
