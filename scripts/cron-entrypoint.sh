#!/bin/sh
set -e

until psql "$DATABASE_URL" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

CMD="$*";
if [ "$CMD" = "celery flower -A myproject" ]; then
#    celery -A myproject purge -f

    celery worker -A myproject -Ofair -n yashoes1@debug_worker \
        --autoscale=4,3 \
        --pidfile="./logs/%n.pid" \
        --logfile="./logs/%n%I.log" \
        --detach

    celery worker -A myproject -Ofair -n yashoes2@debug_worker \
        --autoscale=7,3 \
        --pidfile="./logs/%n.pid" \
        --logfile="./logs/%n%I.log" \
        --detach

#    celery -A yashoes_cron beat \
#        --detach \
#        --pidfile="./logs/schedule.pid"
fi

exec "$@"
