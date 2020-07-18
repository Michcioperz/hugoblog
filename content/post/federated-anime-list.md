+++
date = "2018-05-30"
title = "So you wanna federate your anime list?"
+++

With [MyAnimeList](https://myanimelist.net) down for days now, I’ve been seeing people turn to other alternatives such as [Kitsu](https://kitsu.io) and [Anilist](https://anilist.co) a fair deal recently, and although I have long since done so, it is a new for at least three of my friends.

But even with Kitsu being a [libre](https://github.com/hummingbird-me/hummingbird) alternative to MAL, I’ve been kind of disappointed with how centralized it is, and how if it falls down, it falls down, just like any centralised social network.

### Ding-ding-ding, there’s a standard for these!

You might know by now that I’m a long-time user of [Mastodon](https://joinmastodon.org), as well as an ally of its underlying federation standard, [ActivityPub](https://activitypub.rocks). ActivityPub is a pretty cool building block for a social network, making use of JSON-LD, which is basically JSON with XML-ish namespaces (so that the techbros contribute to creating semantic web without even knowing it).

I considered the idea of using ActivityPub to make something like Kitsu, but federated. That was a good while ago, and I managed to forget it, but my friend BluRaf necrobumped the idea in our IRC independently today. And so I brought it back to the planning table.

I have an important deadline tomorrow, and there is no deadline without watching some anime instead of working on the project, so while I took my time rewatching some _KonoSuba_ with my flatmates (side note: that series still rules), I arrived at a certain personal conclusion:

### There is no need to socialize my anime list. Or so it works for me.

ActivityPub is a pretty cool standard, but I ain’t puttin’ it in my fridge and also in my anime list.

Ultimately all I care about is aggregating intel on what my friends think about particular series, and what is their progress, but I don’t necessarily want to scroll down my (not yet installed) Friendica and see that oh, Asie has finally finished _Yuru CampΔ_ just now. It’s vaguely cool, but not important.

### But with less features don't come less problems.

At this point I could pretty easily imagine creating a simple standard for storing information about your anime list. Why, I could probably just take [Kitsu’s data structures from their APIs](https://kitsu.docs.apiary.io/) and roll with it. It should be pretty easy to formulate a sort of standard that would share your anime list with others in a similar way posts are being shared over RSS/Atom. I bet it could even be made to work with _both_ XML-RDF and JSON-LD (it’s probably what I would have done, considering how I feel like JSON-LD is a weird extension that was never meant to work). Let’s even assume I can get my friends (and my friends can get their friends) to use all that.

### But the centralization could still be a problem.

A social network like Mastodon has it vaguely easy how there is no oracle to depend on, because it’s all about content people create. Meanwhile with anime lists, we need a way to ensure that everyone is talking about the same anime, and I don’t think Gainax would happily plug in an XML/JSON somewhere in the middle of the internet and keep it up forever so that we have a common reference to _Neon Genesis Evangelion_.

What I think is a cool way to tackle this is _multiple oracles_. I mean, I guess?

Let’s say that on my anime list there is this object for _Yuru CampΔ_:

```json
{
  "title": "Yuru CampΔ",
  "some currently unimportant properties": "doesn't matter for now",
  "sameAs": [
    "https://kitsu.io/anime/yuru-camp",
    "https://myanimelist.net/anime/34798/Yuru_Camp%E2%96%B3",
    "https://www.animenewsnetwork.com/encyclopedia/anime.php?id=20010"
  ]
}
```

It’s kind of an obvious idea, I guess? Putting links to whatever known equivalents of this are on the internet. But suppose my friend Delirein doesn’t care about the semantics and doesn’t care about finding the links. But I care. So maybe we could have it so I can add `https://delirein.com/animeme/show/yuru-camp` to my list of related links, and maybe his software could suggest the links to him out of box, if he’s following me? That’s just a rough idea.

### I even thought about it as far as making integration easier for pirate and legit anime sites

Suppose you’ve had _Made in Abyss_ on your to-watch list for eternity, and you’re really trying to find time to watch it, but you can’t. And even if you wanted to watch it, it would have to be organically sourced (from your favourite pirate site that nobody can replace, ever).

You press the button on your anime list. The wheel spins for a second or three, and then gives you the links to episodes on your sites of choice. Here’s how I think we could make it work:

There’s this old standard called Webfinger. Everyone hates it. It’s annoying. ActivityPub was designed _specifically_ to not use Webfinger, unlike its predecessor. Mastodon still uses Webfinger.

Webfinger is made of one endpoint at `/.well-known/webfinger`. You go to `https://niu.moe/.well-known/webfinger?resource=acct:Michcioperz@niu.moe` and it tells you that `Michcioperz@niu.moe` is the same thing as `https://niu.moe/@Michcioperz` and `https://niu.moe/users/Michcioperz`, and that specifically one of these is my ActivityPub profile.

Imagine anime sites implemented this. So you went to `http://crunchyroll.com/.well-known/webfinger?resource=https://kitsu.io/anime/yuru-camp` and it gave you `http://www.crunchyroll.com/laid-back-camp` outright? I think that would be nice.

It would be even nicer if anime lists implemented this too. So you went to `http://crunchyroll.com/.well-known/webfinger?resource=https://meekchopp.es/animeme/show/yuru-camp`, then Crunchyroll would go to `https://meekchopp.es/.well-known/webfinger?resource=https://meekchopp.es/animeme/show/yuru-camp`, where it would find out that I mean something that’s `https://kitsu.io/anime/yuru-camp`, and did the same.

Now, I can’t really imagine Crunchyroll implementing something like this, because as much as I love the exploits of their social media king Miles, their website sucks. But I’m sure pirate sites could pick up on that.

### But hey, this all is just in theory.

I realize that I am proposing [a new standard](https://xkcd.com/927). But it was fun thinking about it. And it sounds vaguely more fun than building a social network, I think?
