from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, role=None, department=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a full name')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role="admin",
            department="EMPLOYEE",
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        return self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )


class Account(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    DEPARTMENTS = (
        ('IT', 'IT'),
        ('IELTS', 'IELTS'),
        ('SPOKEN', 'SPOKEN'),
        ('EMPLOYEE', 'EMPLOYEE'),
    )

    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=15, choices=ROLES,)
    department = models.CharField(max_length=30, choices=DEPARTMENTS)
    address = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(
        upload_to='photos/userPhoto', blank=True, null=True)
    mobile = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserPayment(models.Model):
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='payments')
    month = models.DateField(null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE,
                                blank=True, null=True, related_name='created_payments')

    def __str__(self):
        return f"Payment for {self.user} - {self.month}"


class Settings(models.Model):
    shut_down_app = models.BooleanField(default=False, null=True)
    shut_down_reason = models.TextField(null=True, blank=True)
    contact_name = models.CharField(max_length=45, null=True)
    contact_number = models.CharField(max_length=20, null=True)
    meal_set_last_time = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    meal_set_alert_time = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    today_meal_coocking_start_time = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    today_meal_coocking_end_time = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    alert_text_for_all = models.TextField(null=True, blank=True)

    
    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'
