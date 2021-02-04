
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


from django import template
from django.template.defaultfilters import stringfilter

import phonenumbers

register = template.Library()


@register.filter(name="international")
@stringfilter
def international(value):
    value = value.strip()
    if not value.startswith("+"):
        value = "+" + value
    phonenumbers.parse(value)
    return phonenumbers.format_number(
        phonenumbers.parse(value), phonenumbers.PhoneNumberFormat.INTERNATIONAL
    )


@register.filter(name="national")
@stringfilter
def national(value):
    value = value.strip()
    if not value.startswith("+"):
        value = "+" + value
    phonenumbers.parse(value)
    return phonenumbers.format_number(
        phonenumbers.parse(value), phonenumbers.PhoneNumberFormat.NATIONAL
    )
