# Register your receivers here
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from byro.members.signals import new_member_office_mail_information


@receiver(new_member_office_mail_information)
def new_member_office_mail_info_memberpage(sender, signal, **kwargs):
    return _('''Their additional information is:

Title:                {cnss.title}
Occupation:           {cnss.occupation}
Occupational history: {cnss.occupational_history}

'''.format(cnss=sender.profile_cnss))
