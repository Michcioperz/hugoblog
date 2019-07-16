---
title: "Spotify confuses me"
date: 2019-07-16T17:07:56+02:00
---



My first Spotify playlist dates back to February 2013. It's over 2000 tracks long at this point, and most of my time alone I just put it on shuffle.

At first I was only listening on my desktop and my Android phone. I made use of the free tier for a year, before Spotify realized it had near-zero revenue in Poland and started pushing for Premium subscriptions aggressively by cutting down features. I think what prompted me to upgrade was the "you can only skip 5 times an hour when shuffling" thing that, back then, only happened on phones and never on tablets.

With Premium, I could add another device to the pool – my Raspberry Pi 1B, thanks to [Mopidy](https://mopidy.com). Mopidy makes use of libspotify, a proprietary blob provided by Spotify that could be used in Premium-only applications. By the time I discovered libspotify, it was already long deprecated, with the promise of a new library to replace it soon.

In (if I remember) 2018 libspotify was finally removed from their developer documentation. This hasn't stopped pyspotify developers from, even if just formally, releasing an update of their Python bindings to it. That would suggest it's still alive and kicking.

The official way of playing music from Spotify in third party applications now is through Web Playback SDK. If I understand correctly, it's what actually powers [the official web client](https://open.spotify.com); if it's not, it hasn't given me a chance to notice, because basically it spins up a Spotify Connect listener that can be controlled through other apps or through Web API. It depends on browser's support for Encrypted Media Extensions, more commonly known as "DRM in your browser". This alone excludes low power devices from making use of it.

And while they murmured something about bringing a proper libspotify alternative to the table, I've seen no progress in this direction. Fortunately, someone reversed enough of libspotify to [rewrite it in Rust](https://github.com/librespot-org/librespot). This also only creates a Spotify Connect listener, but it's still a better option.

---

The reason I am bringing this development up is because I'm increasingly fed up with Spotify apps' UX (especially on Android and iOS, on desktop the problem boils down to slow reaction and resource usage of Electron) and I'm trying to remind myself that I still have other options.

It used to be that browsing a playlist, an album, a whatever, you could long press a track to add it to queue, or to add it to a playlist, or to perform 10 other actions imaginable. Now sometimes it works, sometimes it puts the list in multi-select mode, so I can multi-select 1 track and perform the desired action, and sometimes it does nothing. This is easy to work around by pressing the three-dots button on the right side, but it's counter-intuitive after years of long pressing things on phones.

It also takes annoyingly long time to do anything. It might be my fault for having mere 2000 tracks in my main playlist, or it might be the fault of their attempts to put smart recommendations everywhere, increasing the amount of server communication necessary.

And it's not like they care if their recommendations are useful or not. In the Release Radar per-user auto-playlist on Fridays there is an option for every song to mark it or its artist as unwanted, but it never seems to work. I could delete David Guetta every week for a month and still get another track of his in the next iteration of my Radar.

Recently they've announced the release of Spotify Lite for Android, which is something I would very much like, hoping it's optimized enough to quell my anger. Unfortunately, as of last year, [Poland is a first world country](https://www.telegraph.co.uk/business/2018/09/24/poland-becomes-first-country-former-soviet-bloc-ranked-developed/), undeserving of geo-blocked well optimized software.

Days like this my memory wanders back to 2011, when Snaptu was acquired by Facebook. Snaptu was a J2ME app — I'm not entirely sure, but probably a thin client — because I can't imagine fitting a real local clients of Twitter, LinkedIn, Picasa and Flickr in one 100 KB .jar file. It wasn't great, the interface was a bit clunky, but it did its job. Soon after acquisition it was shattered by Facebook, and turned into a Facebook-only client. The core was still there in 2017, when I last used Facebook Lite for Android, kept from the old Snaptu. I recognized it was Snaptu all along by its splash screen with moving dots, reminiscent of the ancient J2ME app.

---

Looking at the trends in the mobile app stores, maybe there is demand for lite apps now? I should go now and give my business partner a call.