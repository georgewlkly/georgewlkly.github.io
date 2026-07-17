---
layout: post
title: Context Window 20
category: newsletter
tags: ["Artificial Intelligence", Newsletter, Publishing]
---
This edition covers OpenAI's inline image generation in 4o and the Studio Ghibli controversy that followed, a US court's refusal to halt Anthropic's training on song lyrics and what that means for publisher litigation strategy, a new world map of AI copyright lawsuits, MIT Tech Review on the dangers of total autonomy for AI agents, OUP's AI Discovery Assistant with Silverchair, the worsening impact of AI crawlers on open access infrastructure and Cloudflare's response, and a BookBrunch op-ed on AI in bookselling.

OpenAI has supported image generation for some time through its DALL-E models: in a sign of the more unified product roadmap that the company has been teasing, it released inline image generation within its 4o model—and [I'm really torn about it][2]. On the one hand, it feels like a significant qualitative step, particularly for ideation/concepting, marketing visuals, and prototyping design elements. The ability to effectively edit images with natural language prompts is slightly magical. On the other, the social web has been taken over by [Studio Ghibli-style images generated with the new tool][3], despite Hayao Miyazaki's known opposition to AI. It's all very reminiscent of [OpenAI releasing a synthetic voice that sounded like Scarlet Johansson after the actor turned down a deal with them][4]. The recurring pattern of brushing up against, or outright ignoring, creators' ethical boundaries feels like trolling by product.
​
[A federal judge in California rejected a bid by Universal Music Group and other publishers to prevent Anthropic training its Claude model on lyrics][5], finding that the publishers' case was too broad and failed to demonstrate irreparable harm. It is a similar finding to [Raw Story Media v. OpenAI, which I wrote about in the second issue of this newsletter last year][6]. The broader litigation will go forward, but for publishers, the key issue is that litigation isn't stopping training, but at best delaying licensing deals. At worst, it's running out the clock on government decisions.
​
Meanwhile, if you want to keep track of litigation or have something to hang on your dartboard, there's [a handy map of active publisher versus AI litigation here][7].
​
MIT Tech Review has [a good piece by a team from AI company Hugging Face, arguing for the importance of human-in-the-loop supervision of AI agents][8]. It introduces a helpful framework for understanding levels of agent autonomy and risk. This is a must-read if you're building or commissioning AI agents. The case against 'total control' is clear: AI agents are strong on execution, variable on context, and weaker at triage. Publishing workflows are well suited to agents, from metadata enrichment to sales forecasting. But automation without oversight risks introducing subtle, compounding errors. For publishers, that means starting with assistive agents—not autonomous ones.
​
[Oxford University Press has rolled out an AI Discovery Assistant, working with technology provider Silverchair][9], to provide academic researchers with enhanced search and AI-generated summaries. This kind of AI tool could reshape researcher expectations, raising the bar for discoverability and UX across other academic publishers. That's both a competitive pressure and a potential differentiator.
​
For Open Access publishers and scholarly presses, [this post highlights a growing problem: AI crawlers are degrading access by overwhelming infrastructure][10]. Publishers such as MIT Press have [implemented technical measures to prevent crawling that go beyond simple robots.txt][11], but these have second order effects such as making them inaccessible to resources such as the Internet Archive.
​
In the wider content ecosystem it is a sufficiently serious problem that [infrastructure provider Cloudflare has just introduced a 'honeypot' model to punish AI crawlers that don't respect restrictions][12].
​
Finally this week, [I wrote a short opinion piece for BookBrunch on how AI might be used by booksellers and other retailers][13].

This was originally published in my email newsletter. [To receive weekly updates on how AI is affecting the publishing industry, sign up here][1]. 

[1]:	https://www.georgewalkley.com/newsletter/
[2]:	https://openai.com/index/introducing-4o-image-generation/
[3]:	https://variety.com/2025/digital/news/openai-ceo-chatgpt-studio-ghibli-ai-images-1236349141/
[4]:	https://www.theguardian.com/technology/article/2024/may/20/chatgpt-scarlett-johansson-voice
[5]:	https://www.reuters.com/legal/anthropic-wins-early-round-music-publishers-ai-copyright-case-2025-03-26/
[6]:	https://ckarchive.com/b/0vuwh9ho8wxgkc7mggrmzhv67r555sn
[7]:	https://chatgptiseatingtheworld.com/2025/03/24/world-map-of-all-copyright-lawsuits-v-ai-companies/
[8]:	https://www.technologyreview.com/2025/03/24/1113647/why-handing-over-total-control-to-ai-agents-would-be-a-huge-mistake
[9]:	https://www.silverchair.com/news/silverchairs-ai-lab-oup-ai-discovery-assistant/
[10]:	https://go-to-hellman.blogspot.com/2025/03/ai-bots-are-destroying-open-access.html
[11]:	https://blog.cloudflare.com/declaring-your-aindependence-block-ai-bots-scrapers-and-crawlers-with-a-single-click/
[12]:	https://arstechnica.com/ai/2025/03/cloudflare-turns-ai-against-itself-with-endless-maze-of-irrelevant-facts/
[13]:	https://www.bookbrunch.co.uk/page/free-article/ai-and-bookselling/
