from django.contrib.auth.models import UserManager as DefaultUserManager


class UsuarioManager(DefaultUserManager):

    def _create_user(self, documento_numero, password, **extra_fields):
        if not documento_numero:
            raise ValueError("Debe indicarse el número de documento")

        user = self.model(documento_numero=documento_numero, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, documento_numero, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(documento_numero=documento_numero, password=password, **extra_fields)

    def create_superuser(self, documento_numero, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(documento_numero=documento_numero, password=password, **extra_fields)
