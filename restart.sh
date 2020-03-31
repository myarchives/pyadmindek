pkill gunicorn
gunicorn \
    -w 10 \
    --timeout 120 \
    -b 0.0.0.0:8001 \
    --limit-request-line 0 \
    --limit-request-field_size 0 \
    --forwarded-allow-ips="*" \
    --log-level debug \
    --access-logfile /data/project/pyadmindek/access.log \
    --error-logfile /data/project/pyadmindek/error.log \
    app:app -D