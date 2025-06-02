FROM ghcr.io/xu-cheng/texlive-full

RUN adduser -D -h /home/nonroot nonroot

WORKDIR /home/nonroot

USER nonroot
