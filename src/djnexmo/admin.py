
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


from django.contrib import admin

from .models import SMSMessagePart


@admin.register(SMSMessagePart)
class SMSMessagePartAdmin(admin.ModelAdmin):
    list_display = ("msisdn", "to", "__str__")
    list_display_links = ("__str__",)
    search_fields = ("msisdn",)
    view_on_site = False
