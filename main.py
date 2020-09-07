import os
from datetime import datetime, timedelta
import random


start_date = datetime(2020, 9, 7)
end_date = datetime(2023, 3, 5)
incDay = timedelta(days=1)
while (start_date <= end_date):
    coQuantity = random.randint(1, 17)
    for i in range(coQuantity):
        os.system(f"touch ./files/C{start_date.strftime('%Y-%m-%d')}{random.randint(1, 12000)}")
        os.system(f"git add .")
        os.system(f"git commit -am \"my contribution on day {start_date.strftime('%Y-%m-%d')}\" --date={start_date.strftime('%Y-%m-%d')}")
    start_date += incDay
    

# start_date=2020-01-01
# end=2023-03-11
# while [ "$start" != $end ]; do
#   echo $start
#   number=$(( ( RANDOM % 365 )  + 1 ))
#   start=$(date -I "$start_date + $number day")
#   touch $start$RANDOM
#   git add .
#   git commit -am "my contribution on day $start" --date=$start
# done