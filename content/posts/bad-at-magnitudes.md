+++
title = "A billion seconds is 31 years. AI skeptics are making the same mistake."
slug = "bad-at-magnitudes"
date = 2026-07-16T00:00:00+00:00
description = "We're bad at magnitudes, and worse when the magnitude is moving. AI is the latest curve the skeptics are calling too early."
tags = ["ai"]
+++

AI success on open-ended problems jumped from 25% to 76% in eight months. That's the headline number in [Anthropic's recent post](https://www.anthropic.com/institute/recursive-self-improvement). The one I keep coming back to is two paragraphs further down. The time it takes for task length to double has itself dropped, from seven months to four. The curve's going up, and it's steepening as it goes.[^steepening]

Most people are bad at magnitudes, and worse again when the magnitude is moving.

A million seconds is 11 days. A billion is 31 years. Most people hear "millionaire" and "billionaire" as two flavors of the same thing, when a million is about the upper bound of what disciplined wage labor can buy you over a lifetime and a billion is an outside shot for almost everyone. To earn a billion at $1M a year takes 1,000 years. You can't get there by working harder. You get there by taking a bet (founder equity, capital ownership) or by allocating other people's capital (carry on a fund).[^inherited]

Whole industries make the same mistake with technology. They look at one year of data, draw a flat line through it and call the plateau.

Moore's Law has had its obituary written so many times that by 2000 [MIT Technology Review was calling its predicted demise an industry joke](https://www.technologyreview.com/2000/05/01/236362/the-end-of-moores-law/). Chips kept getting denser for another two decades. DNA sequencing is the better comparison for AI, because it moved even faster. The Human Genome Project spent [about $3 billion reading the first human genome](https://www.genome.gov/about-genomics/fact-sheets/DNA-Sequencing-Costs-Data), finishing in 2003. You can get one read today for under $1,000. That's roughly a million-fold drop in 20 years, or about 6% cheaper every month, against around 3% a month for Moore's Law.[^carlson] At pretty much every step, credible people said the next big drop wasn't coming. Most of them were right that it'd slow down eventually and wrong about when.

The Anthropic post says Claude went from reliably finishing 4-minute human tasks in March 2024 to 12-hour tasks in May 2026. That's 180x in a bit over two years, and we've seen jumps like it before:

- Gutenberg's printing press (1440s): a scribe could copy 1 to 3 pages a day. [A single press could produce around 3,600](https://en.wikipedia.org/wiki/Printing_press). Somewhere between 1,000x and 3,600x, depending on how you count.
- Ford's moving assembly line (1913-1914): [Model T chassis assembly went from 12 hours 28 minutes in September 1913 to 93 minutes by April 1914](https://en.wikipedia.org/wiki/Ford_Model_T). 8x in seven months.
- Audio transcription, which every UX researcher reading this has lived through: a 60-minute interview used to take 4 to 6 hours to transcribe verbatim. AI does it in about 10 minutes at 90%+ accuracy. That's 30x in a few years.

Each of those was an order-of-magnitude change in time per unit of output, and the people working inside the old way mostly didn't see it coming. AI's doing the same thing across far more kinds of work at once, and it hasn't stopped.

Maybe it plateaus at 80% and the train stops there. I don't know where the ceiling is, and neither does anyone else. But if your view of AI comes from what a model could do the last time you tried it, you're making a bet on magnitude without realizing you're betting.

Anyone who's been in research long enough has already done this math once, for transcription. Now run it for synthesis.[^recursion]

[^steepening]: Had to look that up. It's a real word.

[^inherited]: Or by inheriting it. But I don't believe the folks saying you can only become a billionaire by exploiting labor, since there are far too many exceptions for that to hold.

[^carlson]: Sequencing's version of Moore's Law is called the Carlson curve, after Rob Carlson, who first plotted it. See [Carlson curve on Wikipedia](https://en.wikipedia.org/wiki/Carlson_curve). The monthly rates are my own back-of-envelope: a million-fold over 240 months, versus chips doubling roughly every two years.

[^recursion]: The bigger version of this argument is in the title of the Anthropic post itself: *When AI builds itself*. If the thing that's compounding can improve itself, the math gets weirder, because the doubling time stops being a fixed number at all. That's where the AI safety conversation lives, and the question there is whether the curve changes shape entirely. As an eternal optimist I think we're still on the steep slope. I'll write more about that another time.

---

*Also read: [Grand Theory of AI Skepticism (In UX Research)](https://neddwyer.com/grand-theory-of-ai-skepticism/).*
