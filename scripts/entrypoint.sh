#!/bin/sh
set -e

until psql "$DATABASE_URL" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

CMD="$*";
if [ "$CMD" = "python manage.py runserver 0.0.0.0:8000" ]; then
  if [ "$AUTO_MIGRATE" = '1' ]; then
    python manage.py migrate --noinput
  fi

  if [ "$AUTO_SEED" = '1' ]; then
    python manage.py seed_admin
    python manage.py seed_brand
    python manage.py seed_product
    python manage.py seed_variant
  fi

  if [ "$AUTO_COLLECT_STATIC" = '1' ]; then
    python manage.py collectstatic --noinput
  fi

  if [ "$AUTO_CRONJOBS" = '1' ]; then
    python manage.py crontab remove
    python manage.py crontab add
  fi
fi

exec "$@"
