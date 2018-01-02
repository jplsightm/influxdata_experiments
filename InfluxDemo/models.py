import copy
import numbers
from datetime import datetime
import pytz


class Asset(object):
    """
    I am modeling this after IIoT. An asset is a machine or test station that produces data. Ideally I am providing
    metadata (tag keys and values) that will describe the asset.

    It should be noted that I have not looked at Telegraf too much, so I may be replicating it's functionality

    """

    def __init__(self, asset_name, fixed=True, refrence_id=None):
        """
        :param asset_name: name of the asset
        :param fixed: If the asset is fixed in place - True. If it is a mobile asset (e.g. car, truck, trailer, etc) -
                False
        :param refrence_id: assets tend to be part of systems. Other systems are pretty good at tracking structure....
                this is a tie out
        """

        self.asset_name = asset_name
        self.fixed = fixed
        self.ref_id = refrence_id
        self.template = self._create_boiler_plate()

    def _create_boiler_plate(self):
        bp = {
            "measurement": None,
            "tags": {
                "asset_name": self.asset_name,
                "fixed": self.fixed,
                "ref_id": self.ref_id
            },
            "time": None,
            "fields": {
            }
        }

        return bp

    def update_static_tags(self, tags):
        if not isinstance(tags, dict):
            raise TypeError('There is a strong assumption that tags is a dictionary')
        self.template['tags'].update(tags)


class Measurement(object):
    """
    Create Measurements that will then be written with values added. There will also be a chance to add Tags that are
    variable (for example, something like a serial number or part number)
    """

    def __init__(self, m_name, asset):
        self.m_name = m_name
        self.rec = copy.deepcopy(asset.template)
        self.rec['measurement'] = m_name
        self.timezone = 'UTC'
        self.dlst = False

    def set_timezone(self, timezone, dlst=False):
        if timezone in pytz.all_timezones:
            self.timezone = timezone
        else:
            raise ValueError('{} if not a valid timezone. Try import pytz; pytz.all_timezones; for a valid list')
        self.dlst = dlst

    def update_fields(self, fields, timestamp=None):

        # validate strong assumptions
        bad_keys = [k for k in fields if not isinstance(k, basestring)]
        if len(bad_keys) > 0:
            raise ValueError('Keys in fields must be a base string. Bad values include: {}'.format(bad_keys))
        bad_values = [v for v in fields.values() if not isinstance(v, numbers.Real)]
        if len(bad_values) > 0:
            raise ValueError('Values in fields must be an int or float. Bad values include: {}'.format(bad_values))

        self.rec['fields'].update(fields)

        if timestamp is None:
            timestamp = datetime.now()

        local_dt = pytz.timezone(self.timezone).localize(timestamp, is_dst=self.dlst)
        utc_dt = local_dt.astimezone(pytz.utc)

        self.rec['time'] = utc_dt

    def update_tags(self, tags):
        # validate strong assumptions
        bad_keys = [k for k in tags if not isinstance(k, basestring)]
        if len(bad_keys) > 0:
            raise ValueError('Keys in tags must be a base string. Bad values include: {}'.format(bad_keys))
        bad_values = [v for v in tags.values() if not isinstance(v, basestring)]
        if len(bad_values) > 0:
            raise ValueError('Values in fields must be a base string. Bad values include: {}'.format(bad_values))

        self.rec['tags'].update(tags)
