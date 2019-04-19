+++
title = "Late introduction of Weiss"
date = "2017-06-27"
+++

I figured out it's about time to give some of my projects a write up, and I'm pressed by time, so it seems like a perfect opportunity.



A few months ago, as my dear friend and Crystal fanatic [RX](https://github.com/RX14)[14](https://twitter.com/RX14_chibi) decided to shut down his file hosting of worldwide fame, [aww.moe](https://aww.moe). Most precisely, it wasn't shut down, it was changed to private-only, and while he did offer me an account, I didn't feel like depending on somebody else to host my precious files.

_It turned out to be a fairly good decision, as a few days ago it suffered an outage. Not the owner's fault though._



And so I decided to set into motion a wild idea I've had in mind for a while now.

Think about how various file hosting services choose URLs for the uploaded files. Most of time it's a random string of several characters, and that's not exactly too user-friendly, but prevents enumeration. I actually can't think of any other way, so let's leave it at that.

I felt like there had to be a better idea, one that would create short file names while keeping enumeration non-trivial.



My algorithm goes like this:

1. Calculate an SHA-3 512-bit hash of the uploaded file.
2. If it can be found in the database, just reuse the old URL.
3. Find the shortest non-empty prefix of the hash and use it as filename.

Let's say you upload `file.png` and its hash is `ababababab`whatevermorecharacters. First it will try to save it as `a.png`, then `ab.png`, then `aba.png`, and so on.



This little file hosting I codenamed Weiss, because at the time I was binge-watching the brilliant piece of American anime that is RWBY, and one of its heroines Weiss comes from a rich business family that surely has warehouses and stuff – I later inferred the nice name of the hosting from there, naming it the *Schnee Files Company*.



Weiss's basic setup is pretty straightforward. Install the necessary libraries (there aren't many), build an executable with the Golang toolchain, create a PostgreSQL user `weiss` and a database that matches and is owned by the user (this can be changed in the code, I didn't care about this level of customization at the time), set the environment variable `WAREHOUSE` to somewhere Weiss should store files, and voila, run the executable.

At least that should be it, but it isn't.

While Weiss does care to create the database table she needs at runtime, that's still a quickly written hack.

First of all, she doesn't handle user authentication herself, instead relying on the reverse proxy (Apache, Nginx) to handle it and forward the `Authorization` header to infer uploader's username from. That could be changed in the future perhaps, but at the time it felt good enough for me.

Second, Weiss relies much more on the reverse proxy – the only endpoint handled by Weiss is `/u`, which only accepts POST requests, and which is just for uploading. There isn't even an upload form – you have to upload an upload form with a direct curl request or something like that.

And then, Weiss currently quite prefers convention over configuration – the warehouse directory is expected to be served at `/f` using the reverse proxy. Here you can see my little app depends on the reverse proxy nearly as much as her namesake depends on her father, at least in the beginning.



That said, if you feel adventurous, you can get all 1 file of source code from <https://github.com/michcioperz/weiss/blob/master/weiss.go>, but most likely you don't.
