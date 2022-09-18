FROM python:3-slim-bullseye

COPY .netrc /root

RUN \
    chmod +x /app/docker-entrypoint.sh; \
    pip install playwright==1.25.2; \
    playwright install; \
    playwright install-deps

ENTRYPOINT ["/app/docker-entrypoint.sh"]