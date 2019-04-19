+++
title = "HTTPSing me softly"
date = "2017-07-27"
+++
**EDIT**: the demo is no longer available.

I spent a while today morning making a proof-of-concept-ish of soft HTTPS enforcement without JavaScript.

You might look at it and think it's completely idiotic and ask why would anybody want this, but I have a Nokia E51 and I constantly run into websites that force HTTPS on everything and my phone doesn't understand either TLS or SNI (can't remember) so the only thing that works for me is Google, not even Wikipedia.

Imagine an empty CSS file at `/.well-unknown/cryptolocker` with HSTS and `immutable` in `Cache-Control`. Place `<link rel="stylesheet" href="https://yourdomain/.well-unknown/cryptolocker">` in your documents. Once this CSS loads, the whole domain will pick up HSTS from it, but only if the browser was capable of loading it at least once.

I ~~have~~ had a version of it running at ~~harbringer.meekchopp.es~~ if you're interested, and here's the nginx config it took to build.

```
server {
        server_name harbringer.meekchopp.es;
        listen 80;
        listen 443 ssl http2;
        include acme.snippet.conf; # my snippet for letsencrypt auto-renewal
        include ssl.snippet.conf; # my snippet for ciphers and stuff
        # ssl certificate and key goes here
        # other cool security headers go here
        add_header Strict-Transport-Security "max-age=31536000";
        location /.well-unknown/cryptolocker {
                default_type text/css;
                add_header Cache-Control "max-age=31536000, public, immutable";
                add_header Strict-Transport-Security "max-age=31536000";
                return 200 "";
        }
        location / {
                root /var/www/harbringer;
        }
}
```

Among important things to remember is the fact that nginx's `add_header` is only inherited from `server` by `location` (and other combinations) if there are no such instructions at current level, so the repeated HSTS line is fully intentional.
