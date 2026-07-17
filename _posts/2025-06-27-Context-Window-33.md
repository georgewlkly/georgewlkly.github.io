---
layout: post
title: Context Window 33
category: newsletter
tags: ["Artificial Intelligence", Newsletter, Publishing]
---
It's been a really significant week for legal developments: while the newsletter has more of a copyright focus than usual, the courtroom updates are balanced with some really interesting technical developments from Creative Commons, Anthropic and others (skip down if you're less interested in the legalities). It points to the fact that, however long a road to a settled legal and licensing position, there are immediate practical uses for AI in publishing.

There were separate rulings in Bartz v. Anthropic and Kadrey v. Meta that the use of copyrighted material for AI training is, in certain circumstances, Fair Use. Regarding training, [Judge William Alsup described the author position as "no different than it would be if they complained that training schoolchildren to write well would result in an explosion of competing works. This is not the kind of competitive or creative displacement that concerns the Copyright Act"][1]. However, despite that apparent similarity, the rulings differed in important aspects and there is enough nuance for both sides of the issue to claim positive aspects from them. There's [an excellent side-by-side comparison of the judgements here][2].

While finding that the ultimate use of copyrighted material may be Fair Use, [Bartz v. Anthropic also suggested that the initial collection of books for training represented copyright infringement][3], and there will be a trial to assess damages for this, which could be considerable. If what this establishes is a precedent that training is Fair Use but that material should be legally obtained, commercial and practical arguments for both publishers and developers point strongly towards [a collective licensing model of the sort being pursued by PLS, CLA and ALCS][4].

Intrinsic to these debates is the question of whether AI training is transformative, and whether the replication of verbatim sections of books is an aberrant behaviour or a common issue. In that context, new research showed a Meta model reproducing over 40% of the text of the first Harry Potter, but highly inconsistent results across different models and books. There's [a great explainer here][5].

Meanwhile, [a completely new author lawsuit was filed against Microsoft][6].

In a parallel development, [photo library Getty dropped some aspects of its UK litigation against Stability AI][7], though litigation continues on other aspects, and in the US. But it emphasises the importance for plaintiffs of pursuing precise, winnable arguments rather than broad claims.

Meanwhile, taking a different approach to content and rights, [Creative Commons announced a new project, CC Signals, to allow publishers to communicate their preferences on how data is reused by AI developers][8]. This feels more aspirational than necessarily enforceable, but for Open Access publishers in particular, it's an interesting development.

Changing gear, on a super practical level, the in-built AI functions within Google Workspace are getting more and more useful. There's [a great and very practical set of examples of AI functions in spreadsheets here][9].

[Anthropic released new features allowing users to create AI-powered apps ("interactive artefacts") using Claude][10]. For tasks that require structured interaction, like workflows, data analysis or working with content, this would offer publishers simple creation and greater control of user experience. I could see this being really useful for creating simple internal apps for publishers, as well as reader-facing experiences.

This kind of app is particularly interesting to me having read [this piece by ProPublica's Ben Werdmuller arguing that AI features should be developed further down the stack, in models, browsers or operating systems][11]: "Publisher websites and apps are not destinations in themselves and no amount of AI will make them so... My proposal is this: you should consider what's actually the most useful experience for the user, rather than what furthers your own interests, and make a bet on that, instead."

Finally, not specifically related to publishing, but for general interest, games have often been one of the ways that we understand progress with AI: think of [Garry Kasparov's chess matches against IBM Deep Blue in the late nineties][12], or [Go champion Lee Sedol losing to AlphaGo in 2016][13]. Chess and Go are interesting use cases because while they are highly complex, the moves available each turn are clearly bounded by rules. So I was really interested to read a series of articles on using LLMs to play [the classic boardgame Diplomacy][14], which has a significantly more complex set of interactions based on negotiation and deceit (it was famously the favourite game of public figures, including JFK and Henry Kissinger). [AI media company Every pitted a series of LLMs against one another, finding that they displayed some of the worst of human behaviour][15]. And they also wrote [a detailed guide to how they achieved it][16].

This was originally published in my email newsletter. [To receive weekly updates on how AI is affecting the publishing industry, sign up here][17]. 

[1]:	https://fingfx.thomsonreuters.com/gfx/legaldocs/jnvwbgqlzpw/ANTHROPIC%20fair%20use.pdf
[2]:	https://chatgptiseatingtheworld.com/2025/06/26/12026/
[3]:	https://medium.com/@matthewsag/anthropics-multi-billion-dollar-loss-in-bartz-v-anthropic-is-really-a-win-for-ai-751ca6cfa1e8
[4]:	https://www.pls.org.uk/news-events-policy/news/pls-and-alcs-agree-to-development-of-pioneering-cla-generative-ai-licence/
[5]:	https://arstechnica.com/features/2025/06/study-metas-llama-3-1-can-recall-42-percent-of-the-first-harry-potter-book/
[6]:	https://www.reuters.com/sustainability/boards-policy-regulation/microsoft-sued-by-authors-over-use-books-ai-training-2025-06-25/
[7]:	https://techcrunch.com/2025/06/25/getty-drops-key-copyright-claims-against-stability-ai-but-uk-lawsuit-continues/
[8]:	https://creativecommons.org/2025/06/25/introducing-cc-signals-a-new-social-contract-for-the-age-of-ai/
[9]:	https://workspaceupdates.googleblog.com/2025/06/generate-data-with-gemini-in-google-sheets.html
[10]:	https://www.anthropic.com/news/claude-powered-artifacts
[11]:	https://werd.io/ai-wont-live-on-publisher-sites/
[12]:	https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov
[13]:	https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol
[14]:	https://en.wikipedia.org/wiki/Diplomacy_(game)
[15]:	https://every.to/p/diplomacy
[16]:	https://every.to/p/how-we-made-ai-diplomacy-work
[17]:	https://www.georgewalkley.com/newsletter/
