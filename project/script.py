from datetime import datetime
from dateutil.relativedelta import relativedelta

expiry_date = datetime.now() + relativedelta(months=1)
print(expiry_date)