FROM ghcr.io/xu-cheng/texlive-full:20240901

RUN adduser -D nonroot
USER nonroot
