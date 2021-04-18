---
title: "Owncast on NixOS"
date: 2021-04-18
---

I really enjoy painful discovery of hidden dependencies, so I thought it would be fun to package Owncast for NixOS for my own nefarious purposes. I didn't have any experience with Owncast before, but what could possibly go wrong?

A brief reminder of definitions:

 - [NixOS](https://nixos.org) is a funny Linux distro that doesn't use `/usr` paths and believes that both system config and system packages can be described together as a tree, and funny things happen.
 - [Owncast](https://owncast.online) is a live streaming server software meant for single user self hosting, so that you can do live streams without depending on YouTube or Twitch.
 - [MinIO](https://min.io) is a self hosted alternative to Amazon S3, which by now is a de facto standard for online file storages. I didn't mention it in the opening paragraph, but it will be useful.

There is [a chapter of Nixpkgs manual on packaging software written in Go](https://nixos.org/manual/nixpkgs/stable/#sec-language-go) which made me think this would be easy. And to some extent it was, to some extent no. All in all, the package itself was [pretty simple](https://github.com/michcioperz/nixie/blob/871713215b7a27b9a8a9304f158d3c892934a15b/overlay/owncast.nix), but I had way too much _fun_ with configuring it.

There is a funny thing that happened to Owncast in version 0.0.6 where they threw out the on-disk config (which, by the blessing of [The Nine](https://www.destinypedia.com/Nine), was a YAML file). Since 0.0.6, the config is stored in a SQLite database. This doesn't go well with NixOS's paradigm of generating config files, but oh well. What can you do?

Turns out, this is kind of a pain. First, Owncast assumes that it is being run in, more or less, its source directory, because that's where the directories are for its HTML interface, but also by default it places the video files in the directory right next to the HTMLs. So just getting it to run in `${pkgs.owncast.src}` won't do, but it's still not super-hard, we can just copy all the default files to some writable directory like `/var/lib/owncast`. It took me a few tries to find the `cp` flag I needed to add, `--no-preserve=mode`, so that the new files would be writable despite being copied from readonly Nix store.

It still wasn't starting at this point.

Owncast depends on [ffmpeg](https://ffmpeg.org), which is a Swiss knife kind of program and library for converting audio/video. It just needs to be in environment path, which I thought it did, but Owncast kept crashing, saying it couldn't find it. So I took a look at `utils/utils.go` and found that it would accept a `./ffmpeg` symlink in the working directory if it existed, and it did. For a moment.

I realized where the problem was with the next error message I saw, which said that `sh` could not be run, because there wasn't one in path.

This is one of the things I really like about the Nix approach to packaging. Because there isn't a single `/usr` directory structure that everything gets thrown into, you have to explicitly say what other programs you are using. NixOS uses this principle in the systemd services it generates, which makes sure that the only things that are in `$PATH` of services by default are just coreutils.

Turns out, neither `sh` nor `which` (which is used by Owncast to determine if there is a `ffmpeg` in path) belong in that default constrained path for services. This was fixed by adding `pkgs.bash` and `pkgs.which` to the service's path.

At this point Owncast finally started, which was nice, but I still needed to configure it and one of the things I wanted to do was configure my MinIO instance as video storage. This is because my VPS at Hetzner has a smaller data transfer cap and also less storage than my Intel Atom "dedi" at Online.net.

Configuring it in Owncast was pretty straightforward, but when I tried to stream, it didn't work. A quick look into the logs showed that instead of trying to connect to my MinIO at domain `r.aid.pl`, Owncast was trying to reach its particular bucket at `owncast-koguma.r.aid.pl` subdomain. I'm not seeing a way to change it which is sad, so I had to fix it on MinIO side by adding a wildcard DNS record, expanding the SSL certificate, and setting `MINIO_DOMAIN=r.aid.pl` in MinIO's environment.

And at that point, it actually started to work, which is nice. I'm looking forward to actually streaming something, but that might have to wait until I come up with something interesting to stream… 👀
