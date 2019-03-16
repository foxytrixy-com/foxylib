class PytzToolkit:
    @classmethod
    def localize(cls, dt, tzinfo):
        if tzinfo is None:
            return dt.replace(tzinfo=tzinfo)

        return tzinfo.localize(dt)

pytz_localize = PytzToolkit.localize