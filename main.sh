#!/bin/bash



start_date=2020-01-01
end=2023-03-11
while [ "$start" != $end ]; do
  echo $start
  number=$(( ( RANDOM % 365 )  + 1 ))
  start=$(date -I "$start_date + $number day")
  touch $start$RANDOM
  git add .
  git commit -am "my contribution on day $start" --date=$start
done
