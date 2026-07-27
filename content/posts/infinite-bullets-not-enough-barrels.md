+++
title = "Infinite Bullets, Not Enough Barrels"
slug = "infinite-bullets-not-enough-barrels"
date = 2026-07-27T00:00:00+00:00
description = "AI made the bullets infinite. Which means the only scarce thing left is barrels — the people who take a problem all the way from conception to shipped."
tags = ["ai-native", "founders"]
image = "/images/posts/infinite-bullets-not-enough-barrels/agency-pyramid.png"
+++

I think I might have superintelligence. I wasn't born with it, I didn't learn it or get bitten by a radioactive spider. It's the large language models. Though the impact is smaller, and more boring than I expected, it's a more useful version that I use every day.

The models give us the ability to hold a far bigger context window than any human could - thankfully for some - and to pull in far more data about the world than we could ever read, and to reason over all of it, decide, and then take action.

By that definition it already exists, and it sits on my laptop. It's junior and uneven, and it burns money like nothing else I run. But when I point it at the right problem it does something no one on my team can do, which is take a whole job from "here's a vague problem" to "it's shipped" without needing me in the loop for a single step in between.

That's the part people keep getting backwards. They assume this makes human judgment cheap. It does the opposite: it makes that one specific kind of human input worth more than ever.

### Bypass permissions

When I build product, the tool I use has a dial on it. At the low end it does nothing without asking. Every edit, every command, it stops and waits for me to approve. At the high end there's a mode called bypass permissions. You turn it on and it stops asking. It finds the problem, works out the cause, researches the fix, makes the change, and tells you afterward. "I found this, here's what caused it, I fixed it, just keeping you in the loop."

I don't use it for everything. It eats tokens. It's the wrong setting for anything delicate or irreversible, or anything I don't understand well enough to catch it going wrong. But when the problem is well shaped and the blast radius is contained, and I trust the direction, I turn it on and get out of the way. And it absolutely rips. It closes a loop in twenty minutes that would have been a week of me being the bottleneck between "the code works" and "customers have it."

I wrote a while back about [why a non-engineer CEO ships features himself](https://neddwyer.com/why-im-in-the-codebase/). This is the tool version of that. The whole point of being in the codebase was to feel every brake between the code working and the customer having it. Bypass permissions is what it feels like when you take your foot off most of those brakes at once.

### The pyramid

Someone shared a diagram with me that I haven't been able to stop thinking about. It maps five levels of how completely you solve a problem, from least helpful at the bottom to most helpful at the top, and it lines them up against those same tool modes.

![Agent mode as a proxy for problem-solving completeness. A five-level pyramid mapping how completely you solve a problem, from "there is a problem" at the base to "I identified it, fixed it, just keeping you in the loop" at the top, lined up against Claude Code's permission modes: Manual, Accept Edits, Plan, Auto, Bypass Permissions.](/images/posts/infinite-bullets-not-enough-barrels/agency-pyramid.png)

*Pyramid adapted from a diagram doing the rounds on X. If it's yours, tell me and I'll credit you.*

1. **"There is a problem."** Then you walk away and leave someone else to deal with it.
2. **"There is a problem, and I found some causes."**
3. **"Here is the problem, here are some possible causes, here are some possible solutions."**
4. **"Here is the problem, here is what I think caused it, here are the options, and here is the one I think we should pick."**
5. **"I found a problem, worked out what caused it, researched the fix, and fixed it. Just keeping you in the loop."**

The uncomfortable thing about the pyramid is that the bottom three levels feel like work but aren't the valuable part. Naming a problem is easy. Listing some causes is easy. Even laying out a few options without committing to one is easy, and it looks responsible, and it's mostly a way of handing the actual decision to someone else.

The value is concentrated at four and five. The recommendation. The done. Everything below that is a coordination cost you're passing to another human.

I want to be honest about the exception, because there is one. Sometimes staying at level two or three is the right call. When the real blocker is a human problem, a political one, an org one, something you haven't yet decided is worth building a system or an agent to solve, then flagging it and stopping is fine. Not everything earns automation yet. But that should be a deliberate choice, not the ceiling of what you're capable of.

### Bullets and barrels

Keith Rabois has a [framework I keep coming back to](https://www.conordewey.com/blog/barrels-and-ammunition), from his [*How to Operate*](https://tyastunggal.com/p/how-to-operate) talk. He says most great people in a company are ammunition, and what you're actually short of is barrels. A barrel is someone who can take an idea from conception all the way to shipped and bring people with them. Ammunition is everyone who executes inside a frame someone else built. His punchline is that the velocity of your company is set by the number of barrels you have, because you can only fire through the barrels you own.

I'm going to call the ammunition bullets, because it's about to change form.

For the last decade the ammunition was still people. Even your executors were humans you had to find, hire, onboard, and hold on to. And humans, with love, are fickle. They take sick days. They disagree. Sometimes they don't want to do the thing. Sometimes they're not capable of the thing and neither of you finds out until it's late. So even the "abundant" resource was expensive and unreliable and slow.

That's the part that just broke. The bullets are now [agents](https://theevolveproject.substack.com/p/barrels-and-ammunition-in-the-age). They're effectively infinite. They don't get tired, don't quit, don't need to be talked into it, and don't go quiet on a Friday. The thing that was scarce and unreliable for the entire history of building companies is suddenly cheap and endless.

Which means the whole constraint collapses onto the barrel. When bullets are infinite, the only thing that matters is how many barrels you have and how good they are. A barrel now is a person with agency plus the systems they build to aim and fire all that ammunition. Nothing else is the bottleneck anymore.

### So be a barrel

Put the two frames on top of each other and the personal instruction is obvious.

The pyramid says the value is at the top, at recommend and at done. Rabois says the scarce resource is the barrel, the person who takes a thing all the way. Superintelligence says the bullets to do it are now infinite and sitting right there. So the only question worth asking yourself is: am I operating at the bottom of that pyramid or the top, and how do I move up?

If you're the person who spots the problem and walks away, you've made yourself the cheapest input in the system, right when that input went to zero. If you're the person who takes it from conception to shipped, and builds the scaffolding so the agents can do the middle, you're the thing everything else is now waiting on.

This isn't a corporate skill. It's the oldest founder lesson there is. Nobody is coming to hand you the interesting work. You move up the stack by taking ownership of an outcome end to end and refusing to hand off the decision.

The bullets are free now. Be the barrel.
