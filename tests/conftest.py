
# Licensed under the Apache License, Version 2.0 (the "License"). You may not
# use this file except in compliance with the License. A copy of the License is
# located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


from django.conf import settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pytest_configure():
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=["djnexmo"],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        SECRET_KEY="this is n0t a seekret",
        NEXMO_SIGNATURE_SECRET="abcdefABCDEF12345",
        LANGUAGE_CODE="en-us",
        TIME_ZONE="UTC",
        USE_I18N=True,
        USE_L10N=True,
        USE_TZ=True,
    )
