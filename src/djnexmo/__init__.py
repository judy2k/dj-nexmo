
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

import nexmo

__version__ = '0.0.4'

default_app_config = "djnexmo.apps.NexmoConfig"

client = nexmo.Client(
    key=getattr(settings, "NEXMO_API_KEY", None),
    secret=getattr(settings, "NEXMO_API_SECRET", None),
    signature_secret=getattr(settings, "NEXMO_SIGNATURE_SECRET", None),
    signature_method=getattr(settings, "NEXMO_SIGNATURE_METHOD", None),
    application_id=getattr(settings, "NEXMO_APPLICATION_ID", None),
    private_key=getattr(settings, "NEXMO_PRIVATE_KEY", None),
)
