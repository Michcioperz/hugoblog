+++
title = "Log of my productive activities with excruciating level of detail"
containsCode = true
+++

- 2021-11-15 – created this page while on a train
- 2021-11-14 – created /now and /careers pages on my website
- 2021-11-13 – received third vaccine jab
- 2021-11-10 – discovered that [snapcast](https://github.com/badaix/snapcast) provides remote audio with mostly acceptable delay (~1 second) and not too much configuration. I'm a bit unhappy that I have to hardcode the source device when launching it.
  - ruled out solutions: PulseAudio TCP (PipeWire doesn't support RTP mode yet), zita-njbridge (it kept crashing on my PipeWire), an attempt to write something like socat but over QUIC instead of TCP (I should've read more about QUIC's design first)
- 2021-11-04 – bought a coffee plant from Ikea
- 2021-11-04 – redid a T-shirt design for "Olympiad in Statically Allocated Interval Trees" I came up with some years ago
- 2021-10-31 – started tinkering with [Tauri](https://github.com/tauri-apps/tauri). The minimal set of Nix dependencies seems to be `with pkgs; [ stdenv.cc openssl pkg-config glib cairo pango atk gdx_pixbuf libsoup gtk3 webkitgtk ]` plus NodeJS and Rust of your choice (I have global Rustup)
  - also I guess I know how to make GraphQL queries by hand now
- 2021-10-31 – wrote {{< details "a shell script for changing the dynamic linker on Nix" >}}
{{< highlight shell >}}
#!/usr/bin/env nix-shell
#!nix-shell -i bash -p stdenv
set -ex
interpreter="$(cat $(dirname $(dirname $(which cc)))/nix-support/dynamic-linker)"
for target in “$@”
do
  patchelf –set-interpreter “$interpreter” “$target”
done
{{< /highlight >}}
{{< /details >}}
- 2021-10-30 – trashed my cloud server
- 2021-10-24 – wrote (and didn't publish) a backend for [my podcasts app](https://github.com/michcioperz/dom) that lets me watch anime from torrents by extracting magnet links from nyaa's RSS feeds
- 2021-10-24 – moved most of services off my cloud server onto a Raspberry Pi
- 2021-10-21 – gave a talk at my MSc seminar about NixOS
- 2021-10-19 – moved [typo13k](https://typo13k.glitch.me) from Heroku to Glitch
- 2021-10-18 – discovered that s3fs-fuse with my Minio is not POSIX-y enough to be used for file uploads by The Lounge
- 2021-10-17 – wrote [jmdgen](https://jmdgen.michci.ooo), a talk abstract webpage generator for [my MSc seminar](https://students.mimuw.edu.pl/SR/)
- 2021-10-14 – moved my static websites from the funny Nix contraption to Netlify
- 2021-10-11 – bought a 5.65 inch e-paper display and made it display weather from meteo.pl
- 2021-10-07 – wrote a contraption that lets you watch anime from MKV torrents in browser by repackaging into temporary MP4 and VTT files (TODO: use DASH instead)
- 2021-09-30 – finished internship at Sentry.io
- 2021-09-26 – wrote a Python/Django contraption that lets me rewrite Spotify playlists with scripts using contents of other playlists
- 2021-09-25 – wrote [a blog post documenting ClickHouse's unintuitive UUID ordering]({{< ref "post/clickhouse-uuid-ordering" >}})
- 2021-09-25 – wrote a Github Actions + Go contraption to trigger Nix builds and deploys of my static websites on my NixOS cloud server
- 2021-09-23 – assembled a Creality Ender 3 v2 3D printer
- 2021-09-21 – discovered [ClickHouse's UUID ordering]({{< ref "post/clickhouse-uuid-ordering" >}}) as manifested [here](https://twitter.com/Michcioperz/status/1440348107485581318)
- 2021-09-13 – received notice of approval of [my MSc thesis](https://apd.uw.edu.pl/diplomas/208893/) topic
- 2021-09-10 – modified [anacrolix's torrentfs](https://github.com/anacrolix/torrent/blob/master/cmd/torrentfs/main.go) to use in-memory storage and wrote a script for mpv to be able to play magnet links through that
- 2021-09-05 – made [Path of Anileast Resistance](https://stoic-banach-fda51b.netlify.app/), a webapp in Svelte that tells you which anime series you are (time-wise) closest to finishing, so you can get that feeling of accomplishment ASAP
- 2021-08-27 – deployed something big on Sentry.io's prod
- 2021-07-25 – wrote [a weird CLI podcast app](https://github.com/michcioperz/dom). I also have a private backend for it that uses Radio 357's secret endpoints. Generally it's just a simple TUI for launching mpv on links found on the internet
- 2021-07-12 – started internship at Sentry.io
- 2021-05-31 – tried to build openmaptiles on an ARM server and failed (TODO: expand on this)
