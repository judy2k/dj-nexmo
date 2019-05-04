
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


from django.db import models


class SMSMessagePart(models.Model):

    class Meta:
        ordering = ("-concat_ref", "concat_part")
        unique_together = ("concat_ref", "concat_part")
        verbose_name = "Message Part"
        verbose_name_plural = "Message Parts"

    concat_ref = models.CharField(max_length=32, db_index=True)

    message_id = models.CharField(max_length=32, unique=True)
    msisdn = models.CharField(max_length=24)
    to = models.CharField(max_length=24)

    text = models.CharField(max_length=160, null=True)
    # TODO: Need to do something with these:
    data = models.BinaryField(max_length=160, null=True)
    udh = models.BinaryField(max_length=160, null=True)

    type = models.CharField(
        max_length=7,
        choices=[("text", "Text"), ("unicode", "Unicode"), ("binary", "Binary")],
    )
    keyword = models.CharField(max_length=160, null=True)
    message_timestamp = models.DateTimeField()
    timestamp = models.DateTimeField()

    concat_part = models.IntegerField()
    concat_ref = models.CharField(max_length=32)
    concat_total = models.IntegerField()

    def __str__(self):
        return (
            "Message {self.concat_ref}: {self.text!r} (Part {self.concat_part} of {self.concat_total})".format(
                self=self,
            )
        )
