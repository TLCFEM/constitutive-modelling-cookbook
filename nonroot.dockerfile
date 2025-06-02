FROM ghcr.io/xu-cheng/texlive-full

RUN adduser -D nonroot
USER nonroot
