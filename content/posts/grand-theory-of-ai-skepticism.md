+++
title = "Grand Theory of AI Skepticism (In UX Research)"
slug = "grand-theory-of-ai-skepticism"
date = 2026-07-11T00:00:00+00:00
description = "Most cynicism about AI in UX research is two years stale. Five questions I run on every confident AI take, including my own."
tags = ["ai", "ux-research"]
+++

Most cynicism about AI in UX research is two years stale.

I spend a lot of time on r/UXResearch and on calls with researchers using Great Question. The same misperceptions come up in both. Confidently, often in upvoted comments, often in the same breath as "I haven't actually tried it lately."

The word that should appear in almost every confident claim about AI in research right now is *yet*. AI synthesis can't create a novel insight yet. AI moderators can't catch what a great human can yet. Synthetic users aren't a substitute for real participants yet. The omission of that one word is what turns a defensible 2026 observation into a 2027 mistake.

A visual example: compare the [2023 AI-generated Will Smith eating spaghetti video](https://en.wikipedia.org/wiki/Will_Smith_Eating_Spaghetti_test) to [what 2025 models produce](https://www.techradar.com/ai-platforms-assistants/chatgpt/will-smith-eating-spaghetti-was-peak-ai-chaos-in-2023-now-it-shows-how-fast-the-tech-has-evolved). In 2023 he is all fingers, bug-eyed, putting his fork through the side of his mouth. Now you could put the output on an iMac screen and nobody would know it wasn't a Hollywood-produced clip.

### Where the cynicism comes from

The skeptics have good reasons, and I want to name them before I argue with anyone.

- People have already been laid off. Telling someone whose role was eliminated last quarter that AI is "just a tool" lands badly, and rightly so.
- The tempo is exhausting. Being told every quarter that the state of the art has moved is its own cognitive load, on top of the actual work.
- The hype is insufferable. LinkedIn is full of confident proclamations from people who haven't sat in a research seat in years. Pattern-matching skepticism toward boosters is a healthy immune response. As an eternal optimist, I'm probably guilty of this too.
- It's about identity as much as employment. A decade spent developing a craft (interviewing, sensemaking, the felt judgment of when a participant is hedging) isn't the kind of thing you take lightly when someone says an LLM can approximate it.

The conclusions can still be wrong. The people holding them don't deserve dismissal, from me or from you.

### The "yet" trap

The failure mode I see most is a 2023 observation frozen into a 2026 categorical claim, with the "yet" deleted.

Hallucination is a good example. When Vectara launched its grounded-summarization leaderboard in November 2023, [GPT-4 made things up in 3% of short summaries and Google's PaLM-Chat in 27%](https://www.vectara.com/blog/cut-the-bull-detecting-hallucinations-in-large-language-models). By 2025 the best models were under 1% (Gemini 2.0 Flash hit 0.7%), and the test had gotten easy enough that Vectara [retired it and built a harder one](https://www.vectara.com/blog/introducing-the-next-generation-of-vectaras-hallucination-leaderboard) using long legal, medical and financial documents. On that version, as of September 2026, the [best model is under 2% and most frontier models land somewhere between 3% and 15%](https://github.com/vectara/hallucination-leaderboard). So the problem hasn't gone away, and it varies a lot by model and by job. That's exactly why "AI is unreliable" has to say *which* AI, configured *how*, on *what* task.

AI moderation was bad eighteen months ago, because the first generation of tools worked off transcripts only and missed tone, hesitation and anything happening on screen. The second generation is multi-modal. The third is being built natively inside research platforms so moderation, recruitment, and synthesis share the same model context. Any take on AI moderation older than 12 months should be assumed stale.

Synthetic users have real limits today. The review everyone cites is [Kuric, Demcak and Krajcovic's 2026 systematic review](https://www.researchsquare.com/article/rs-9057643/v1) of 182 studies (still a preprint). The authors argue the limits are structural, and they might be right. But [their own dataset](https://github.com/synthetic-users-research/synthetic-participants) shows that more than half of those studies tested only GPT-3-era models or the original GPT-4. The limits they document are real for that generation. A categorical "never" needs evidence from the models people are actually using now.

AI in research isn't solved. But a confident dismissal built on 2023 evidence is the mirror image of what the AI hype-bros do: a strong claim about 2026 with no 2026 data behind it.

### Five questions

I run five questions on every confident take, in either direction.

1. **What tool did they actually use?** "AI" isn't a tool. ChatGPT with no document upload is a different product from Claude with a project, from a research platform with retrieval and citation. A claim about "AI" without a named tool is a claim about a vibe.
2. **When did they last use it?** Six months is roughly a model generation, so a take formed 18 months ago is judging something two or three versions old. Most categorical dismissals were formed in 2023-2024 and haven't been re-tested, and the date is almost always missing.
3. **Are they allowed to use the real thing at work?** A huge share of "AI is useless" takes come from people whose IT department gave them a neutered enterprise Copilot that can't connect to anything. They're judging the category based on a deliberately hobbled tool.
4. **What's their background and incentive?** A vendor selling AI tools, a vendor competing with them, a researcher worried about their job, a consultant whose practice depends on the old way of working. Everyone's got an angle, including me. Knowing the angle is how you weight the take. You still have to read it.
5. **Are they reflexively cynical or reflexively bullish?** Some people are professional naysayers; some are professional hype amplifiers. If a person's last ten takes on a topic all went the same direction, the eleventh probably will too.

If three of those five answers are "I don't know," the claim doesn't deserve much weight yet.

### Apply it to me

Now run it on me. I'm the CEO of an AI-native research platform. My livelihood depends on AI in research being more capable than skeptics claim. I've never carried "UX Researcher" as a title.

- *What tool?* Great Question's analysis, retrieval, and moderation tools. The ones I directly shape. I'm not neutral about them. I also use the latest from Claude, ChatGPT and anything else I can get my hands on.
- *When?* Continuously, but in the seat of building, not the seat of being a senior IC researcher. In terms of building I'm building new features and apps constantly.
- *Constrained?* Yes. By what we've decided to build and not build. There are research jobs the platform doesn't yet do well, and I see those daily.
- *Background?* Australian founder, second-time CEO, fifteen years in UXR-adjacent work, never the title of a UX researcher.
- *Reflexively bullish?* Probably, on average. I've spent two years arguing for the upside. Counter-balance accordingly.

So weight my claims against my obvious incentive. I think the framework holds either way. The conclusion that the field's cynicism is mostly wrong should land softer than I've been landing it.

### What "yet" actually costs

Two years ago you could read every AI-in-research take and accurately conclude "this category doesn't work yet." Today that read is wrong on hallucinations for everyday summarization (long, messy documents are still a fair fight), partially wrong on moderation, narrowly wrong on synthetic users for prep work, and still right on synthetic users for validation.

The researchers who'll define good research in 2027 are re-testing their own 2024 takes right now.

Tell me what tool and when you last used it, and we can actually have the argument.

---

*Also read: [The Grand Theory Of Customer Validation](https://neddwyer.com/grand-theory-of-customer-validation/) and [You Have to Touch AI Psychosis](https://neddwyer.com/you-have-to-touch-ai-psychosis/).*
