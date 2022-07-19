# commands to create pian.mo:
#    python <python_dir>/Tools/i18n/pygettext.py gettext_module.py
#    mkdir en/LC_MESSAGES
#    python <python_dir>/Tools/i18n/msgfmt.py pian.po -o en/LC_MESSAGES/pian.mo
import os, gettext
os.environ.setdefault('LANG', 'en')  # application-default language
gettext.install('pian', '.')

import gettext_module
