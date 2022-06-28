from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom User Manager to use email as unique identifier
    """

    def create_user(self, teamName, email=None, password=None):
        if not teamName:
            raise ValueError("Team name required")

        user = self.model(
            
            teamName=teamName,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, teamName, email=None, password=None):
        user = self.create_user(teamName=teamName, email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user