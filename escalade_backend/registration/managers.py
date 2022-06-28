from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom User Manager to use email as unique identifier
    """

    def create_user(self, email, teamName, password=None):
        if not teamName:
            raise ValueError("Team name required")

        user = self.model(
            
            name=teamName,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user