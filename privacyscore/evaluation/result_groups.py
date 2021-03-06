"""
This module defines the result groups which a result might have and their
human-readable representation.

At the moment, a default mapping of keys to groups is present. This should be
replaced by a dynamic, user-defined group mapping should be usable.
"""
from collections import OrderedDict

from django.utils.translation import ugettext_lazy as _


# TODO: Replace by dynamic user-defined groups
RESULT_GROUPS = OrderedDict()
RESULT_GROUPS['privacy'] = {
    'name': _('NoTrack: No Tracking by Website and Third Parties'),
    'short_name': _('NoTrack'),
    'long_name': _('No Tracking by Website and Third Parties'),
}
RESULT_GROUPS['ssl'] = {
    'name': _('EncWeb: Encryption of Web Traffic'),
    'short_name': _('EncWeb'),
    'long_name': _('Encryption of Web Traffic')
}
RESULT_GROUPS["security"] = {
    'name': _('Attacks: Protection Against Various Attacks'),
    'short_name': _('Attacks'),
    'long_name': _('Protections Against Various Attacks'),
}
RESULT_GROUPS['mx'] = {
    'name': _('EncMail: Encryption of Mail Traffic'),
    'short_name': _('EncMail'),
    'long_name': _('Encryption of Mail Traffic'),
}

DEFAULT_GROUP_ORDER = list(RESULT_GROUPS.keys())
