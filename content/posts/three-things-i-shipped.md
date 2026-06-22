+++
title = "Three things I shipped last week"
slug = "three-things-i-shipped"
date = 2026-06-21T00:00:00+00:00
description = "A CEO who's actually in the code doesn't just ship code. Last week I shipped a feature to production, ran a product spike into the hardest part of our codebase, and built a go-to-market system. Three different modes of shipping, one week."
tags = ["ai-native"]
+++

I've written about being AI-pilled, and about dragging the whole company through the transformation. This is the part where I show you what it tangibly looks like.

Last week I shipped three differently shaped things that I think capture the breadth of what it means to ship with AI.

## 1. I shipped real code to production

The most boring-sounding one, and the one I'm most pleased with.

We had a settings tab in Great Question that had bugged me for a long time. Too dense, badly organised, hard to read. The kind of thing that never makes the roadmap because it's nobody's emergency. I rebuilt the information architecture so it's actually legible.

While I was in there, I shipped a permission customers have been asking for: the ability to update and customise the sign-out time. A real pain, for them and for me, now solved.

Small stuff, and maybe not the best use of my time on their own merits - but a way for me to learn, walk the walk, and ship real solutions for customers.

## 2. I spiked the hardest part of our codebase

Our scheduler is the best calendar on the market for booking customer research. It's also one of the most complex things we own. Deep integrations, a lot of moving parts.

Frankly it was too complex - with it's calendar & email integrations, timezones, multiple calendar synchs etc - for me to hope to ship meaningful changes to, but I could seek to understand it and propose changes. So I ran a product-led spike: what does this need to become? I pulled together what we already know, what customers actually want, where the state of the art is, and which platforms we might build on instead of Nylas (Cronofy, Cal.com). And I started defining what agent-first scheduling really means.

Now I have a map of a hard problem we're going to have to solve soon, and can have deeper and more meaningful conversations w/ product & engineering on what to do about it.

## 3. I built a go-to-market system

Competitive intelligence. I pulled signals from everywhere they live: support calls, sales tickets, customer conversations, and what competitors are actually putting into the world.

![A competitive intelligence dashboard headed "Know every competitor cold" — live battle cards for the UX research market, with competitor names blurred](/images/posts/three-things-i-shipped/competitive-intel.png)

Then I turned it into something the whole company can use. Battle cards for sales, competitive tensions and opportunities for product, a shared way of thinking about where we sit. Not a one-off deck. A system.

## The point isn't the code

Three things, three registers. Engineering. A product spike. A go-to-market system. One week.

"In the mix" used to mean occasionally opened a PR, or commented on a PRD. Now it means moving across all of it: writing code, exploring the product areas we'll have to tackle next, and building the tooling that makes the business better at competing.

That's what the transformation actually buys you. Not a founder who can code. A founder whose range is no longer bottlenecked by what they can personally build.

---

*Also read: [You Have to Touch AI Psychosis](https://neddwyer.com/you-have-to-touch-ai-psychosis/) and [Inject the AI straight into my veins](https://neddwyer.com/speaker-swap/).*
