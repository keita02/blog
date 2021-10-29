

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ou3(pxfo&qxx^85@ia(qjc0fur*k_j!e-vlcm3sc*qbhc$hakc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',

    'tinymce',
    'post',
    'marketing',
    'ckeditor',
    'crispy_forms',
    'accounts',
    'galerie',
    'divide_section',
    'last_tendance',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'post.context_processors.banner_handler',
                'galerie.context_processors.gallery_image',
                'divide_section.context_processors.section',
                'last_tendance.context_processors.tendance',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Myblog',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# VENDOR_PATH = os.path.dirname(BASE_DIR)
VENV_PATH =  os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



TINYMCE_DEFAULT_CONFIG = {

   'height': 360,

   'width': 500,   

   # 'height': 360,

   # 'width': 600,

   'cleanup_on_startup': True,

   'custom_undo_redo_levels': 20,

   'selector': 'textarea',

   'theme': 'modern',

   'plugins': '''

   textcolor save link image media preview codesample contextmenu

   table code lists fullscreen insertdatetime nonbreaking

   contextmenu directionality searchreplace wordcount visualblocks

   visualchars code fullscreen autolink lists charmap print hr

   anchor pagebreak

   ''',


   'toolbar1': '''

   fullscreen preview bold italic underline | fontselect,

   fontsizeselect | forecolor backcolor | alignleft alignright |

   aligncenter alignjustify | indent outdent | bullist numlist table |

   | link image media | codesample |

  

   ''',

   'toolbar2': '''

   visualblocks visualchars |

   charmap hr pagebreak nonbreaking anchor | code |

   ''',

   'contextmenu': 'formats | link image',

   'menubar': True,

   'statusbar': True,

   }


SITE_ID = 1
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
# LOGIN_URL = 'accounts:login'



# -----------POUR S'INSCRIRE A L'AIDE D'EMAIL------------------------------

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ACCOUNT_EMAIL_VERIFICATION = True
# ACCOUNT_EMAIL_REQUIRED = True

# ------------------------------------------------------------------------


# AUTH_USER_MODEL = 'accounts.Account'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',

}

# AUTH_USER_MODEL = 'accounts.Account'
# Configuration d'smtp server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ansoumanekeita825@gmail.com'
EMAIL_HOST_PASSWORD = 'mIvgu2-bozmoc-zoxvub'
EMAIL_USE_TLS = True

SITE_ID = 1

# FORMULAIRE D'INSCRIPTION
# ACCOUNT_FORMS = {'signup': 'post.forms.CustomSignupForm'}


# ACCOUNT_FORMS = {'login': 'accounts.forms.MyLoginForm'}