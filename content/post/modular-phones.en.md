---
title: "My nuclear take on modular phone design"
date: "2021-02-23"
---

For some time now I've been exploring alternative approaches to smartphones.

In February 2020 I wrote a little bit about Nokia 800 Tough, which was a modern attempt at a feature phone with smartphone-ish features, but turned out to be not very great and useful, although pretty well built, which I think could be useful for attending protests _cough cough_ I mean, taking long walks across Warsaw. The full review is over here: [Lessons learnt from dual phone wielding]({{< ref "./dual-wielding" >}}).

I wasn't so brave that I would preorder a Braveheart series PinePhone right after deciding that the Nokia was too meh for me. I did, however, buy one in late 2020, and it's an okay phone with terrible power management (the battery doesn't last a whole day under my usage pattern) and subpar user experience. I'm not ready to give up on it yet, there is a still a number of ways how it can overcome those problems, and I'm willing to give it time.

Unfortunately, after 3.5 years the battery in my Motorola Moto G5S is so dead that I manage to drain it completely during breakfast after a night of charging, and sometimes it discharges from 30% to 0% in a matter of seconds. That called for a radical solution. While two of the phones I bought since the G5S weren't up to the task, I've also found a Nexus 4 in my drawer. I bought it at some point to toy with Ubuntu Touch and postmarketOS, because it's one of the reference devices for all weird mobile operating systems through the fact that it used to be supported by AOSP. The one I have is slightly damaged: there is a strip of the screen that doesn't record touch, roughly covering the middle row of the keyboard. I'm managing to deal with it: on LineageOS you can tell the system to accept 180 degree rotation, so I just turn the phone upside down when I need the keyboard.

I think one of my biggest surprises about a 2012 phone like Nexus 4 is that while it's definitely slower than the G5S, and the lack of LTE modem renders it pretty bad at tethering, it's still a very good phone. Which leads me to wonder how I could address its shortcomings. And of course the best way to address a thing's shortcomings is to throw it into the trash can and take a fresh sheet of paper and reinvent the wheel.

### _The wheel (19xx)_

I think what I most need from a smartphone could be divided into two categories. One is for things that smartphones inherited from feature phones, while the other is more about the features that they evolved themselves.

#### Feature phone features

When I was in primary school, nobody in my class had any kind of phone. I lived in a small village of population 700, and because my flat was even in the school building, and we had a landline phone, there was no need to give me a phone to keep control of me. But giving me one for school trips was still useful, so I had a Siemens ME75. Back then all the phone had good battery life that was counted in days, not hours.

I still managed to be ahead of the times by buying data packages from my mobile operator. My operator was virtual, so they offered pretty big packages considering the era. At some point the offer was 250 MB per 10 PLN (roughly $2.50). Think of all the Wikipedia reading I could do in Opera Mini on that amount! Or news website reading! If I was lucky, I could tell my friends in the back of the coach bus on the school trip that the Polish soccer team scored a goal roughly at the same time the driver of the bus heard it on the radio.

#### Smartphone exclusives

At this point, my smartphone is basically a pocket computer for me. I can spend annoying amounts of time patching my scripts through SSH. Sometimes I download things with youtube-dl in Termux. I guess I am expecting it to let me execute arbitrary Linux programs (and that's part of the reason I can't imagine myself switching to an iPhone as daily driver).

I've also grown pretty comfortable with typing on touch keyboards. I will still get up from my bed and sit at the computer if I need to type something longer (such as this piece), but I think touch keyboards are an okay tradeoff for being able to use the device with just one hand, on the go or something like that.

All the mid-end phones these days have massive photo cameras, GPS sensors and NFC modules. I think we can agree that these are pretty cool things, and while I haven't seen anyone initiate a file transfer over NFC, paying with a phone that's emulating a credit card definitely caught on at my faculty canteen. I don't think I would give any of these up.

### _The wheel (2021)_

My idea here is to actually recognize feature phones and smartphones as separate types of beings and embrace those differences. But since I want the best of both worlds, shouldn't I just get one feature phone and one smartphone? As you may know, I tried that already with the Nokia and the G5S, and it didn't work well. But what if those devices were actually meant to be used together?

Get ready to laugh at the next paragraph where I will describe my allegedly ideal solution.

I think I'd like to have a small (and I mean Siemens ME75 small, not Nokia 800 Tough small) feature phone that would let me answer phone calls, send and receive texts, maybe listen to music and do some basic GPS stuff, but most importantly, **provide its LTE data connection in the form of an Ethernet plug/socket**. This Ethernet could then be consumed by a laptop in areas with no WiFi, or by the second device, which would be shaped after a current-era smartphone, but which wouldn't itself have the radio modules that the actual-phone device already has, because they can just be shared.

I'm not yet convinced how to split the modules up, but I think this could have a good impact on battery life of the smartphone, because you could actually turn it off completely when you don't need it, and boot it up only when you want to do some internet crimes (the word "crimes" used here in a rather innocent internet way). I'm pretty sure we can get it to boot up fast enough to make it feel instant enough.

It still doesn't solve the part where you're not receiving notifications from smart apps while the device is off. So maybe we need to put some notification functionality on the actual-phone part. The notifications are usually abstracted away to either Apple or Google cloud these days, so maybe we could pull off a further abstraction and have the actual-phone tell you what notifications you have pending (and receive them over one low-power-consuming idle TCP socket or something), and then you could turn the phone on and consume their full content.

It's all just a shower thought in the end, but I think it's interesting to consider this.
