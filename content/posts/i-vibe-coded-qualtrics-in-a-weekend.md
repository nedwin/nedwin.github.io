+++
title = "I Vibe Coded Qualtrics in a Weekend"
slug = "i-vibe-coded-qualtrics-in-a-weekend"
date = 2026-05-27T00:00:00+00:00
description = "What the SaaS-pocalypse gets right, what it gets wrong, and a rubric for deciding what to build, buy, or partner on."
tags = ["ai-native", "saas"]
image = "/images/posts/i-vibe-coded-qualtrics-in-a-weekend/header.png"
+++

![A vibe-coded survey builder dissolving into the code that generated it](/images/posts/i-vibe-coded-qualtrics-in-a-weekend/header.png)

I had a few hours free on Sunday, so I decided to vibe code Qualtrics. Surveys, branching logic, response collection, a dashboard. The lot. By the end of the afternoon I had something that genuinely worked.

It was incredible. And it was a little terrifying, at least in part because I run a software company that sells, among other things, surveys.

Every founder I know has done a version of this lately. You sit down on a weekend, point an LLM at a category you know cold, and watch a year of someone's roadmap appear in front of you in a few hours. Then you sit back and ask the obvious question: if I can do this, what stops everyone from doing this? And if everyone can do this, what exactly am I selling? What is my moat?

People are calling it the SaaS-pocalypse.

## The case for the apocalypse

The macro version of this fear is real, and the markets have already voted. In early 2026 something like $285 billion got wiped off software stocks in a week, and by some counts close to $2 trillion has come off the sector since. The [iShares software ETF had its worst stretch since 2008](https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html). [Forrester wrote a blog literally titled "SaaS As We Know It Is Dead."](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/) The logic is simple and a bit scary: if AI agents do the work of ten people, you stop paying for ten seats. Per-seat SaaS, the most reliable business model of the last fifteen years, suddenly looks fragile.

And it isn't just the seat math. It's the build math too. [Retool's 2026 Build vs. Buy report](https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software) found that 35% of enterprises have already replaced at least one SaaS tool with something they built themselves, and 78% expect to build more this year. Sixty percent of them did it outside any IT oversight. Every renewal now comes with a new line in the conversation: *could we just build this?*

I'm not going to tell you that's all hype. I felt it on that Sunday. The barrier to a working V1 of almost anything has basically gone to zero.

## We're watching it happen to us

Here's the part that makes this personal rather than theoretical.

We sell a research platform: a CRM of the people you can talk to, a repository of everything you've ever learned from them, and the tools to run studies in between. And we're now, regularly, watching customers vibe code chunks of exactly that.

A prospect on a recent call put it bluntly to one of our salespeople: *if Claude can do this, why can't we just plug it into our CRM and have it vibe code the whole thing?* Another customer showed up to a session having replaced their Figma prototype with a vibe-coded web app they'd built that morning. These aren't luddites poking at a toy. These are sharp teams at real companies, and the question they're asking is completely reasonable.

So I had the founder's two-stage reaction. Stage one: oh $h1T. Stage two, once I'd actually thought it through: this is going to be awesome. Because the more I sat with it, the more I realized that almost none of these companies should actually build all the things that they're capable of building. 

And being able to articulate *why* turns out to be one of the most useful things I can do for a customer right now.

## Product vs Operations vs Corporate

The clearest way I've found to think about this came out of a conversation with Nicolas Carey and the team at Brex.

Brex has the engineering talent and the cash to build almost anything. So what do they build, and what do they buy? Their answer comes in layers.

![Three stacked layers: product and AI plus infrastructure are Build, corporate software is Buy](/images/posts/i-vibe-coded-qualtrics-in-a-weekend/build-buy-layers.png)

The top layer is their product. The expense management, the corporate card, the actual thing customers pay for. Brex would never outsource that. It would be insane to let someone else build your core product. Of course they build it.

The next layer down is the AI and infrastructure that makes the product genuinely work. Know-your-customer checks, fraud and money-laundering controls, the machinery a card company has to be excellent at. At their scale, they build a lot of that in-house too, because being world-class at it directly determines whether the product is good.

Then there's the bottom layer. The corporate software they run *on*. Their CRM. Their payroll. Their research stack. And here the answer flips. Is Brex going to vibe code Salesforce? Are they going to vibe code their own payroll? Are they going to rebuild a research CRM and repository, given everything else they could point that engineering at? No. Even though they absolutely could. The interesting tell: Brex has tried building pieces of this in the past, and every time they've concluded it wasn't a good fit.

The layers are the whole point. The closer something sits to the thing your customers actually pay you for, the more it makes sense to own it. The further away it sits, the more building it is just a tax you've volunteered to pay.

## Does it make your beer taste better?

I have a shorter way of asking the same question. Does it make your beer taste better?

If you brew beer, the thing your customers taste is the beer. Building a slightly worse version of the accounting software you could buy off the shelf doesn't make the beer taste better. Neither does rebuilding your CRM, or your survey tool, or your research repository. It might feel like progress. It's almost always a detour.

I learned this watching it go wrong. Long before I joined GoDaddy, the company built nearly everything in-house, and at one point that included their own version of Microsoft Word. Was a slightly worse Word ever going to help anybody buy more domains? Of course not. They killed it within a few years and went on to become one of the largest resellers of Microsoft software on earth. Building the thing was the expensive way to learn it didn't make the beer taste better.

None of this is new thinking, by the way. It's just newly urgent. Geoffrey Moore [has been making this argument for twenty years](https://strategictoolkits.com/strategic-concepts/core-and-context-strategic-framework/) with the language of "core versus context." Core is the work that differentiates you in your customers' eyes. Context is everything else you have to do to stay in business. His line is the one to write on the wall: if you do context brilliantly, you don't win. If you do it badly, you get in trouble. 

So do it competently and move on. 

Amazon says the same thing in fewer words when they talk about not spending engineering on "undifferentiated heavy lifting." Vibe coding didn't repeal any of this. It just made the temptation to ignore it a hundred times stronger, because now you *can* build the context, in an afternoon, and it'll even kind of work. ["Maybe it'll work for us"](https://www.youtube.com/watch?v=Po4adxJxqZk).

## The part nobody vibe codes

Here's what my Sunday Qualtrics didn't have, and what every weekend build is quietly missing.

It worked for one person. Me. The moment a second person needs to log in, you need auth, roles, and permissions. The moment a teammate wants to change something, you need code review and a way to ship safely. The moment the server falls over at 11pm, somebody has to be on call. The moment you go on holiday, either you've documented enough that it keeps running or you're answering Slack from the beach. Anyone can plant a tomato. Keeping the garden alive through February is the actual job, and nobody posts about that part.

And that's before anyone asks the trust questions. Want to put real customer data in your weekend build? Then you're signing up for SOC 2, a pen test, GDPR handling, HIPAA controls if you touch anything clinical, PII tagging and retention, SSO, audit logs your own customers can export, vendor security reviews, disaster recovery. 

Open-source survey tools have existed for twenty years. So have open-source CRMs and help desks. Almost no serious company runs them, and not because they couldn't stand one up in an afternoon. The tool was always the cheap part. Vibe coding made the tool free. It didn't make the trust free.

The version I keep coming back to is a question I'd put to anyone tempted: when it breaks, whose neck gets rung? When you need to send a survey to two million people and it falls over, who do you call? When someone wants to change it, who decides if that change ships? When you get hacked, is it the one person who built it on a Sunday, and what happens when they're on vacation? Add it all up and you haven't built a tool. You've started a department. You're now in the business of running survey software, which is a strange business to be in if you sell expense cards, or apartments, or insurance.

## A rubric: build, buy, or partner

So when *should* you build? It's not never. It's a spectrum, and the honest answer depends on a handful of questions you can ask in about thirty seconds.

A quick note on the language. "Build vs buy vs partner" is borrowed from how companies think about acquisitions, which isn't quite what we're talking about here. We're really talking about a vendor relationship and how much of it you want to own. Think of it as a dial that runs from *do it yourself* to *rent it* to *go deep with someone who'll build it with you.*

| Question                                         | Lean **Build**                             | Lean **Buy**                                              | Lean **Partner**                                             |
| ------------------------------------------------ | ------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------ |
| **Does it make your beer taste better?**         | Yes. It's your core, your differentiation. | No. It's context. Necessary, not special.                 | Adjacent to core. Strategic, but not the thing itself.       |
| **Who uses it?**                                 | One person, or a throwaway prototype.      | The whole team, every day.                                | A team, with needs that'll keep evolving.                    |
| **Does it need to be maintained?**               | No. Use it once and bin it.                | Forever. And you don't want to own that.                  | Yes, and you'd rather shape a roadmap than staff one.        |
| **Does it hold sensitive or regulated data?**    | No real data, or only your own.            | Customer PII, PHI, anything a regulator cares about.      | Sensitive, and compliance is part of what you're paying for. |
| **What happens when it breaks?**                 | Nothing. Nobody notices.                   | Someone important is blocked and you need a name to call. | You want a partner on the hook with you.                     |
| **Could building it become its own department?** | No. It's a weekend, not a hire.            | Yes, and that's not the business you're in.               | Yes, so let someone whose business it *is* run it.           |

If most of your answers sit in the left column, by all means, vibe code it. Honestly, go build a single survey if you want one. That's a great use of a Sunday. If they sit in the middle, buy the boring, well-run thing and spend your saved cycles on your actual product. And the right column is the one people forget exists: sometimes the smartest move isn't to build or to buy off the rack, but to find a vendor who'll go deep with you, integrate properly, move with your roadmap, and carry the liability you don't want to own.

Years ago I wrote about [how service providers survive when a platform starts competing with them](https://neddwyer.com/what-the-quickbooks-accounting-community-can-learn-from-godaddy-pro/): the winners niche down and out-serve. I called it the DIY / Do-It-With-Me / Do-It-For-Me spectrum back then, which is really the same dial as build / buy / partner. The instinct holds for your own tooling. Do the small number of things only you can do brilliantly, and let people who live and breathe the rest do the rest.

## So, should you ship the weekend build?

I'm not going to ship my Sunday Qualtrics. It's tempting, and I could absolutely harden it into something real. But it wouldn't make anyone's beer taste better, and I have a finite number of Sundays to spend on the things that do.

I will however use it as a symbol for what is possible, and as inspiration for how we might support significantly more study types at Great Question. But shipping it holus bolus? No.

The SaaS-pocalypse crowd is half right. A lot of thin, undifferentiated, per-seat software is about to have a very bad few years. And to be honest it deserves to. The barrier to building a V1 of it has collapsed, and customers will absolutely build the easy 80%. But the gap between a working V1 and something a whole company can actually rely on, securely, for years, hasn't collapsed at all. If anything it's the last thing standing, and it's exactly where the value is moving.

So before you spend a quarter rebuilding something you could rent, ask the question. Does this make your beer taste better? If the answer is no, you're not saving money by building it. You're paying twice. Once for the build, and again for every hour you spend keeping it alive instead of making the thing your customers actually came for.

---

*Also read: [Emerging infrastructure and the entrepreneurial opportunity](https://neddwyer.com/emerging-infrastructure-and-the-entrepreneurial-opportunity/).*
