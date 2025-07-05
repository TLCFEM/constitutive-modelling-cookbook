FROM ghcr.io/xu-cheng/texlive-full:20240901

LABEL KEEP="true"

RUN adduser -D -h /home/nonroot nonroot

WORKDIR /home/nonroot

USER nonroot
