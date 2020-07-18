---
title: Fediverse, or a double-edged sword
date: 2020-05-22T14:55:29+0200
---

For many years my favourite social media site was [Twitter](https://twitter.com). I'm not entirely sure why: was it the character limit on the status updates, or the ease of meeting new people, or maybe something else; either way, it was my favourite. However, for the last three years my social media attention has been split between Twitter and the so-called *fediverse*. I'd like to explain a little about what the *fediverse* is and what's good to know before joining.

### The story up until now

#### What is the fediverse and why?

In April 2017 something interesting rose to fame (at least among tech-interested people) from the dark depths of Github – [Mastodon](https://joinmastodon.org), a piece of software for creating social network sites a bit alike to Twitter. The key difference was that the sites created were not separated "walled gardens" – they could exchange their users' messages with one another.

Thanks to this property, user [@michcio@om.nom.pl](https://om.nom.pl/michcio) could easily chat with [@fiskus@a.nom.pl](https://a.nom.pl/fiskus), and [@Michcioperz@niu.moe](https://niu.moe/@Michcioperz) could join the thread and reply just as well. (You can see from this example that the usernames on fediverse look a bit like email addresses.) The larger social network that came to be was named *the fediverse* by its people (or shorter, just *fedi*), because the act of servers exchanging messages was referred to as federating.

Mastodon caught attention of Twitter's techie lefties with cool features like per-post privacy settings (public or followers-only), as well as per-post *Content Warnings*. Another promise of Mastodon was that of a social network free of Nazis, whatever that meant — and I'll come back to this topic in a moment.

#### Why isn't it called just Mastodon?

The concept of federating mini-twitters was far from new. The underlying protocol — OStatus — was taken from another project started in 2008, StatusNet (now renamed [GNU social](https://gnu.io/social/)). Unlike StatusNet, however, Mastodon looked slick and cool <sup>\[citation needed\]</sup> and wasn't written in PHP.

But soon it turned out that the Ruby on Rails framework used for building Mastodon didn't perform as well as was needed. Admins of larger *instances* (instances is how we refer to fedi servers) could usually afford to get better server hardware, but admins of smaller instances could either write a script that restarted Sidekiq every now and then, or they could jump from Mastodon to another server software: Pleroma.

#### Is there anything other than Mastodon on fedi?

[Pleroma](https://pleroma.social) wasn't free of the cultural heritage of PHP, either. The first part of Pleroma that came to be was the user interface that could be used with StatusNet instead of what was shipped alongside it. It was more interactive than what it replaced: for one, it dynamically polled the server for new messages and didn't need a page reload for every action. 

Later on the developers decided that it would be better to write an own server. They chose Elixir programming language (categorized as a "meme language" by some) for the job. Elixir had rich tooling for highly performant web services. Thanks to this and other project decisions, Pleroma used drastically fewer server resources, cementing its position among people hosting their instances on Raspberry Pi boards.

Since then, more projects have joined the fediverse, among them [Misskey](https://github.com/syuilo/misskey) strong in Japanese motifs, radically minimalistic and radical in general [Honk](https://humungus.tedunangst.com/r/honk). Less twitter-ish solutions appeared as well, such as educational resources sharing system [MoodleNet](https://moodle.net) and WebTorrent-based YouTube competitor [PeerTube](https://joinpeertube.org). The federation protocol was also replaced – badly documented OStatus was retired in favour of [ActivityPub](https://activitypub.rocks), which even received the mantle of a W3C Recommended Standard.

#### So, what's the deal with the Nazis?

As mentioned earlier, the creator of Mastodon expressed his intent to build a network that's safe from Nazis and GamerGaters and such, as he invited lefties and LGBT supporters from Twitter. It was a big deal for many people joining, because they saw moderation on Twitter as too slow and permissive, and thus they felt endangered by this policy of Twitter.

But Mastodon's idea of bottom-up moderation done by users wasn't only tempting for those who found Twitter's moderation lacking, but also for those who found it overreaching. And so from the very beginning *free speech* Mastodon instances appeared, chewing on the image Mastodon's creator was trying to build. It escalated further when American far-right twitter-like platform Gab chose to migrate to Mastodon. I'm not even sure if they're *the* most vicious instance of fedi, but it brought 1 million users in, and with them, an extraordinarily large volume of messages.

As a result, fediverse sprang into a few subgraphs. Drawing the line well is hard, but I think a few general categories come to mind: proponents of absolute free speech, proponents of blocking instances from the first category as well as those inertially federated with them, the Japanese people ([I wish I didn't have to explain](https://en.wikipedia.org/wiki/Legal_status_of_drawn_pornography_depicting_minors)) and finally, small instances attempting to stick to the policy of equal distances (see: [foreign policy of interwar Poland in the years leading up to World War II](https://en.wikipedia.org/wiki/History_of_Poland_%281918%E2%80%931939%29#Foreign_policy_1935%E2%80%9339)).

The second group mentioned grew a habit of announcing who they found ban-worthy. Github repositories were created of receipts and vast explanations of why certain instances were ban-worthy. There even appeared a view that Pleroma is Nazi software, mostly because many instances from the first group ran Pleroma, as it was cheaper. For me it felt a bit ridiculous, especially when Pleroma developed more advanced automatic moderation of inflowing messages than the mechanisms found in Mastodon.

There's also a technical problem to fedi – ActivityPub's design is naive at times, for example, the section of the standard specifying security is marked as non-normative. During transport of messages from source instance to followers' instances the messages receive a irrefutable cryptographic signature. A bad actor following the user could then publish such a followers-only message, and it would be provable that it was really posted by the user.

### Double-edged swords

As you can see, fedi has its problems and sometimes even I wonder if it's worth my time and effort being a part of it.

Usually, however, I conclude that my friends there are worthwhile, but if you'd like to join, you have to understand what problems might come, because they're often related directly to the benefits of fedi:

#### You can (not not) moderate

I think quite a few people came to fedi for capabilities like this: if there's someone attacking you, you can just block them or their whole instance. Dishonor on them, dishonor on their cow.

But this power has an implicit consequence I observed on the instances I've been to (as user and as admin). At some point you *will have to* moderate, will have to mute or block people or instances, because you will eventually run into people whose behaviour is wayyyyyy out of your comfort zone. I mean, unless you're those people, I guess.

#### You can set your own rules on your own instance (and you don't have to agree with anyone, and neither do they)

You can make an instance without any rules (if your country won't take your server or IP address away because of it).

You can make an instance where swearwords are forbidden.

You can make [an instance where the letter E is forbidden](https://oulipo.social) or [an instance where all letters other than E are forbidden](https://dolphin.town).

You just have to take into account that:

1. There exist people who will look at your instance's rules and based on that decide whether they want to let you try and befriend them.

2. There exist people who will never take a single look at your instance's rules and will spam you with offensive messages until you block them (or become one with them).

#### You can make funny bot accounts (and spammers can make less funny spam bots)

Making an account on fedi is ridiculously easy. Hell, making a whole instance is easy. And you can use these accounts for a lot of cool stuff, [bots that write funny things](https://botsin.space/@jouns), [bots that make funny images](https://botsin.space/@dogebot), [bots posting weather reports for random cities](https://botsin.space/@randomweather) — there is a lot of potential for cool stuff.

Unfortunately sometimes (not super often, because fedi is still not popular enough) you'll run into waves of spam. Sooner or later you will get a message from a bot telling you to join the *Don't Marry Movement*, in which there are three main rules. (Side note: writing satire ripoffs of it with friends can be great fun.)

#### You can't easily search all the messages ever (and few people can)

Searching can be useful, but the developers of Mastodon decided that it's a dangerous vector for abuse, so Mastodon only allows a limited kind of search. Still, even if it was unrestricted, you'd still be restricted to the messages that reached your instance. The fedi network is large and distributed, and there's a big chance most of the messages people write that are not directed at you somehow will never reach you.

That means, however, that it's a bit harder for people to dig up the stupid stuff you said 5 years ago. I mean, if you posted it in public, I bet Google knows about it, but followers-only posts are, by nature, more difficult to index by search engines.

I don't know if it's bad or good, it just is. Take note and think about what you publish.

### You didn't manage to scare me off, where do I sign?

First of all, even if mastodon.social has open registration when you're reading this, don't go there. There's too many people on there, destroying some of the benefits of federation, and it's difficult to moderate on this scale.

Two years ago I made a Polish Pleroma instance. I no longer run it ([Rafał](http://kolucki.pl) does), but if you're Polish-speaking and interested in a fedi instance that has "Aggression towards other users is forbidden, regardless of who started it. (...) We insist on maintaining civility" in its rules, you could try <https://a.nom.pl>.

If it really has to be my single user instance, <https://om.nom.pl>, I'm willing to accept a few people, but that's to be discussed with me in private.

Other than that, I loved it on <https://kawen.space>, which is a Pleroma. If you're looking for trustworthy Mastodons, I can recommend <https://nulled.red> and <https://mstdn.io>, because I trust their admins and my good friends are there.

There's a lot of instances for all kinds of people, like <https://catgirl.science> for techie catgirls (although this one requires invites) and <https://writing.exchange> for writers, so you can probably find something for yourself this way as well.

Or maybe you want to try being an admin yourself? There's a very cool guide written by Darius Kazemi at <https://runyourown.social/> which treats about the social aspects of admining a fedi instance. It's generally a good read for things that I forgot to mention here about fedi.


---

See you on fedi

[@michcio@om.nom.pl](https://om.nom.pl/michcio)
