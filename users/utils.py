from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_welcome_email(user_email, user_name):
    subject = 'مرحباً بك في نظام المصادقة!'
    
    # إنشاء محتوى HTML للبريد الإلكتروني
    html_message = f"""
    <html>
        <body dir="rtl">
            <h2>مرحباً {user_name}!</h2>
            <p>شكراً لتسجيلك في نظام المصادقة.</p>
            <p>نحن سعداء بانضمامك إلينا!</p>
            <br>
            <p>مع تحيات،</p>
            <p>فريق النظام</p>
        </body>
    </html>
    """
    
    # تحويل HTML إلى نص عادي
    plain_message = strip_tags(html_message)
    
    # إرسال البريد الإلكتروني
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        html_message=html_message,
        fail_silently=False,
    ) 