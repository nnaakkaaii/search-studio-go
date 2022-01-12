sleep 30
until psql -h db -U root -d tmp -c "\l"
do
  sleep 1
done
/docker-search-go