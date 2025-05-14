# نظام المصادقة باستخدام Django

نظام مصادقة متكامل مبني باستخدام Django و Django REST Framework.

## المميزات

- تسجيل المستخدمين مع التحقق من البريد الإلكتروني
- المصادقة باستخدام JWT
- المسارات المحمية
- إدارة الملف الشخصي للمستخدم
- توثيق API
- إرسال بريد إلكتروني ترحيبي عند التسجيل

### Todo API

This project provides a RESTful API for managing Todo items.

## API Endpoints

### Get all Todos
- **URL**: `/api/todos/`
- **Method**: `GET`
- **Description**: Retrieve a list of all todo items.

### Create a Todo
- **URL**: `/api/todos/`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
      "title": "Todo Title",
      "description": "Todo Description",
      "completed": false
  }
  ```
- **Description**: Create a new todo item.

### Get a Todo by ID
- **URL**: `/api/todos/<id>/`
- **Method**: `GET`
- **Description**: Retrieve a specific todo item by its ID.

### Update a Todo
- **URL**: `/api/todos/<id>/`
- **Method**: `PUT`
- **Request Body**: 
  ```json
  {
      "title": "Updated Title",
      "description": "Updated Description",
      "completed": true
  }
  ```
- **Description**: Update an existing todo item.

### Delete a Todo
- **URL**: `/api/todos/<id>/`
- **Method**: `DELETE`
- **Description**: Delete a specific todo item by its ID. Returns a success message if deleted successfully.

## Response Format
All responses will be in JSON format.

### المصادقة

- `POST /api/register/`  
  تسجيل مستخدم جديد  
  الحقول المطلوبة: email, name, password, password2  
  الإرجاع: بيانات المستخدم و JWT tokens  
  يتم إرسال بريد إلكتروني ترحيبي تلقائياً

- `POST /api/login/`  
  تسجيل الدخول  
  الحقول المطلوبة: email, password  
  الإرجاع: بيانات المستخدم و JWT tokens

- `POST /api/token/refresh/`  
  تحديث JWT token  
  الحقول المطلوبة: refresh token  
  الإرجاع: token جديد

### الملف الشخصي

- `GET /api/profile/`  
  الحصول على الملف الشخصي  
  المطلوب: JWT token في رأس Authorization  
  الإرجاع: بيانات المستخدم

## الإعداد

1. استنساخ المستودع
2. إنشاء بيئة افتراضية:
   ```bash
   python -m venv venv
   source venv/bin/activate  # في Windows: venv\Scripts\activate
   ```
3. تثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```
4. إعداد البريد الإلكتروني:
   - قم بتفعيل المصادقة الثنائية في حساب Gmail
   - قم بإنشاء كلمة مرور للتطبيق من إعدادات حساب Google
   - قم بتحديث إعدادات البريد الإلكتروني في `settings.py`:
     ```python
     EMAIL_HOST_USER = 'your-email@gmail.com'
     EMAIL_HOST_PASSWORD = 'your-app-password'
     ```
5. تشغيل الترحيلات:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. تشغيل الخادم:
   ```bash
   python manage.py runserver
   ```

## اختبار API

يمكنك استخدام Postman أو أي عميل API لاختبار نقاط النهاية. تأكد من:

1. تسجيل مستخدم جديد باستخدام `/api/register/`  
   سيتم إرسال بريد إلكتروني ترحيبي تلقائياً
2. تسجيل الدخول باستخدام `/api/login/`
3. استخدام JWT token في رأس Authorization للمسارات المحمية
4. اختبار نقطة النهاية `/api/profile/` باستخدام الـ token

## ميزة البريد الإلكتروني الترحيبي

- يتم إرسال بريد إلكتروني ترحيبي تلقائياً عند تسجيل مستخدم جديد
- يحتوي البريد الإلكتروني على:
  - رسالة ترحيب شخصية
  - اسم المستخدم
  - معلومات إضافية عن النظام
- يمكن تخصيص قالب البريد الإلكتروني في `users/utils.py`
- يستخدم النظام SMTP Gmail لإرسال البريد الإلكتروني
- يتم التعامل مع أخطاء إرسال البريد الإلكتروني بشكل آمن

## ملاحظات هامة

- تأكد من استخدام كلمة مرور التطبيق وليس كلمة مرور حساب Gmail العادية
- في بيئة الإنتاج، يجب تخزين إعدادات البريد الإلكتروني في متغيرات البيئة
- يمكن تخصيص قالب البريد الإلكتروني حسب احتياجاتك
