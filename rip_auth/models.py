

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

# 커스텀 유저를 다루기 위한 UserManager 클래스를 재정의
class RipUserManager(BaseUserManager):

    def create_user(self, **kwargs):
        if not kwargs['email']:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=RipUserManager.normalize_email(kwargs.pop('email')),
            **kwargs
        )

        user.is_active = False
        user.is_staff = False
        user.set_password(kwargs['password'])

        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        u = self.create_user(email=email,
                             username=username,
                             password=password
                             )
        u.is_staff = True
        u.is_active = True
        u.save(using=self._db)
        return u


class RipUser(AbstractBaseUser, PermissionsMixin):
    """
    # RipUser Model
    회원이 가지는 정보들을 저장한다.
    ## 가입에 필요한 정보
    * email        : 가입신청할 때 쓰는 이메일을 나타낸다.
    * real_name    : 회원의 이름을 나타낸다.
    * student_id   : 회원의 학번을 나타낸다.

    ## 포탈을 이용할 때 필요한 정보
    * is_active  : 시스템에 로그인할 권한이 있는지 여부를 나타낸다.
    * is_staff   : 운영진인지를 나타낸다.
    * username   : 학회 포탈에서 사용할 ID
    """
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    real_name = models.CharField(
        verbose_name='real_name',
        max_length=20,
        blank=False
    )

    student_id = models.CharField(
        verbose_name='student_id',
        max_length=8,
        default='B000000',
        blank=False
    )

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    username = models.CharField(
        verbose_name='username',
        max_length=20,
        blank=False,
        unique=True
    )

    objects = RipUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'rip_auth'
        db_table = "rip_user"
        default_permissions = ()

        """
        Database에서의 검색속도 향상을 위해 인덱스를 적용할 칼럼
        * 학번으로 빠르게 검색이 가능해야 한다.
        * email로 검색해도 빠르게 검색이 가능해야 한다.
        * ID로 검색해도 빠르게 검색이 가능해야 한다.
        """
        indexes = [
            models.Index(fields=['student_id', ]),
            models.Index(fields=['email', ]),
            models.Index(fields=['username', ]),
        ]

    def get_full_name(self):
        # The user is identified by their username
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        return self.is_staff
