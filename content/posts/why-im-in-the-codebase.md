+++
title = "Why I'm in the Codebase"
slug = "why-im-in-the-codebase"
date = 2026-06-21T00:00:00+00:00
description = "I'm a non-engineer CEO and I've started shipping features myself. Not to relive my twenties or step on the team, but to feel every brake between 'the code works' and 'customers have it,' then write each one down with a fix."
tags = ["ai-native", "founders"]
image = "/images/posts/why-im-in-the-codebase/codebase-diff-header.png"
+++

![A code diff changing a hard-coded two-hour session timeout to a configurable, account-controlled one](/images/posts/why-im-in-the-codebase/codebase-diff-header.png)

Last week I shipped my first feature.

It's a small one. For about five years, Great Question logged everyone out after two hours, no matter what. A hard-coded number an engineer dropped into a pentest fix back in 2021 that nobody ever went back and questioned. Security teams had asked for a tight limit, so we gave everyone the tight limit, and then everyone got logged out mid-session and blamed us for it. It drove our customers up the wall, and it drove me up the wall every time it bounced me out of my own product.

I'd developed [schlep blindness](https://paulgraham.com/schlep.html).

Now you can set it yourself. Thirty minutes if you're paranoid, up to 30 days if you're not. The administrator gets the dial, which means when someone gets logged out too aggressively they can take it up with their own admin instead of us. And it drops you back where you were, so you're not hunting for your place every time. It's live in our account today. I've got it set to 24 hours and I keep wanting to push it to a week.

I'm not telling you this because the feature is impressive. It isn't. I'm telling you because of what happened next, which was nothing. The code works. It's deployed. Customers could be using it tomorrow. But it's still not enabled in every account, it's not in the changelog, nobody's announced it, and I didn't actually know what to do next. That gap, between "the code works" and "customers have it," is the whole reason I'm in the codebase at all.

I wasn't only learning how to build the feature. I was learning all the bottlenecks it takes to get something from a customer's problem into a customer's hands.

So here's the experiment. I've started building and shipping features myself. Not because I miss being an engineer, and not to step on the team. I'm doing it to feel every one of those brakes myself, then write each down with a fix next to it. The session timeout already taught me one: we have no fast path from "merged" to "announced." Flag flip, changelog, support article, the heads-up to customer success. All manual, all living in different people's heads. Every one of those is a tax on how fast any of us can ship, and I couldn't feel the tax until I tried to pay it myself.

## How it actually got built

The honest version, because the honest version is the useful one.

It started as a paper cut. I'd get logged out, swear at the screen, and move on. Then one day I didn't move on. My rule on this stuff is see a snake, kill a snake. Don't walk past it, and don't keep poking it once it's dead. So I went spelunking. Dug through our logs, old Linear tickets, Fathom calls, trying to work out how big this actually was and whether anyone but me cared. The story I'd always been told was that the two-hour limit was a SOC 2 thing, a HIPAA thing, a we-have-to thing. It wasn't. That's not how SOC 2 works. It was a number from 2021 wearing a compliance costume.

Then I built it. Mocked it up first, then had Claude do most of the actual writing. The part I'm proudest of isn't the code. It's that I knew Tim would eventually look at this, and Tim cares deeply about anything that touches governance. So I ran the whole thing back and forth through Codex playing Tim, told it to make the work unimpeachable, and let it tear my own pull request apart before a human ever saw it. Then a human did. Yuri reviewed it for real, asked for a couple of changes, and we merged.

AI got me about 90% of the way there. I think 98% is coming. But this was a security feature. Timeouts, logins, session handling. That last stretch is exactly where I shouldn't be the one vibing it. I did it. I probably wouldn't do it again. Some of that 2% is judgment a model doesn't have yet, and some of it's just process I had to learn from scratch: how feature flags work, that a pull request reviews itself zero percent of the time, that if you don't tag a specific human and ask them to look, nobody looks.

<!-- canon-callback: [You Have to Touch AI Psychosis](https://neddwyer.com/you-have-to-touch-ai-psychosis/) — this post is the lived receipt for that essay's "ship a vibe-coded thing and triage what it costs you" prescription; the guardrails below ARE "keep the velocity, drop the religion" in practice. Placement: inline aside in this paragraph. -->
I wrote a while back that you have to [touch AI psychosis](https://neddwyer.com/you-have-to-touch-ai-psychosis/) to get any good at this. You go too far in, watch it not quite work, and drag yourself back one step with the receipts to show for it. This is me collecting receipts. The thing you learn from collecting them is exactly where the model stops being trustworthy, which is the only thing that lets you build sane rules about where it gets to run.

## The guardrails

So I gave myself rules, and I think of the work in three tiers.

**Big systems. Spike, don't ship.** Scheduling, highlight reels, the load-bearing stuff. I'm not going to vibe-code a new scheduler; someone would rightly yell at me. But I can spike it, build the mocks, work out how it should go, and hand it to someone who can actually carry it. I'm doing exactly that with scheduling right now, jamming with one of our engineers who's already poked holes in my version. Good. That's the point of a spike.

**Sensitive systems. Engineer in the loop from the start.** Migrations, security, billing, anything cross-cutting, anything touching customer data. The session timeout was arguably one of these, which is part of why I won't make a habit of it. I can start these and get them part of the way, but an experienced engineer is paired in from the beginning, not parachuted in at the end to clean up.

**Contained features. I take them end-to-end.** Mostly front-end, low blast radius, no migrations. The thing I'm working on now is making text you copy out of Ask AI keep its formatting, because a customer complained about it yesterday. Even these go through the same review, the same adversarial model pass, and the same manual QA as anyone else's work.

And a couple of rules I hold myself to regardless: one spike and one ship in flight at a time, never more. Everything in Linear, including the follow-ups. And done means done. Flag at 100% or reverted, in the changelog, ticket closed. Not "the code works."

## Where I face-planted

You should know how this went wrong, because both ways are obvious in hindsight and worth you not repeating.

For the first week I wasn't using worktrees, so I had three features running at once in the same corner of the codebase, quietly overwriting each other. I deleted my own work more than once. And my pull requests were far too big for anyone to review. A wall of changes nobody could reasonably sign off on. Both fixable. Both the kind of thing you only really learn by doing it badly first.

## Why this isn't about me

Here's the actual point. If I can prove out a safe path, you can walk it too.

Picture customer success going in and fixing the paper cut a customer complained about that morning, instead of filing it and waiting a quarter. Picture support closing the loop on a small bug themselves. Picture design shipping the polish they've been asking someone else to do for months. All of it inside guardrails, everyone knowing exactly what they're cleared to touch and what they're not. That's the thing I'm actually trying to build. The features are just how I find the potholes first.

So review me like you'd review anyone. I'm going to get things wrong, and I want to hear it when I do. Loudly, early, the same way you'd tell any other engineer their PR is a mess. The login bug took five years to fix because it was nobody's job. Most of our best work is sitting in that same pile, waiting for someone to decide it's theirs.

*New posts land weekly. [Subscribe at clubned.co](https://clubned.co) and they'll come to you.*

<!-- canon-callback: [Inject the AI straight into my veins](https://neddwyer.com/speaker-swap/) — same AI-native series; speaker-swap was about borrowing someone else's AI DNA by watching them work, this is Ned becoming that person inside his own team. Placement: "Also read" footer. -->
*Also read: [Inject the AI straight into my veins](https://neddwyer.com/speaker-swap/), on bringing AI-pilled builders into your team to watch them work, and sending your own people out to do the same.*
