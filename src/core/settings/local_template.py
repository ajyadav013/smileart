"""
Django local settings template for core project
"""

DEBUG = True

SECRET_KEY = "[yy.Mm~[w4KvUeYQ=5?A[Pf51TRcl(]K>,-EQ94.Biz$Ob`h7sTXd}a1=E%d"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smileart',
        'USER': 'smileart',
        'PASSWORD': 'smileart',
    }
}


ALLOWED_HOSTS = ["*"]
