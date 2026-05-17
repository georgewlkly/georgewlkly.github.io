---
layout: post
title: Context Window 25
tags: ["Artificial Intelligence", Newsletter, Publishing]
---
There's a lot to unpack this week, including a couple of quite contrarian views on the environmental impact of AI and on the use of copyrighted material as training data. But I'm starting with something that's both exciting and very practical...

OpenAI is rolling out an update to ChatGPT's web search capabilities to include online shopping results and personalised recommendations. With around a billion users, this has the potential to disrupt existing retail channels: perhaps not like TikTok Shop in its ability to drive bestsellers, but more like Google Shopping's impact across a long tail of titles. ([OpenAI expressed interest this week in buying the Chrome browser with its 60%+ market share if Google is forced to divest it][1], which would accelerate that impact). For publishers wanting their books to be visible, there are two immediate action points. First, [products are discovered by a search crawler, OAI-SearchBot, and you need to ensure that robots.txt on your website allows access to this][2]. To my mind, OpenAI have implemented this quite thoughtfully: OAI-SearchBot only crawls for product information, not model training, so it would be possible to opt your website out of its other training bots, but still make titles visible. Secondly, referral URLs from OpenAI include the UTM parameter utm\_source=chatgpt.com so this can be tracked in Google Analytics. Forward this paragraph to whoever looks after your website and analytics. The second action point: at the same link, OpenAI has opened up a waitlist for suppliers to provide product feeds directly to ChatGPT—if your website has D2C sales, you should sign up today to be notified when this is available.

Earlier this year, researcher Andy Masley published a deeply researched 9,000 word blog post on the environmental impact of individual ChatGPT usage (or similar models). Last week, he published [a concise version that presents updated findings and puts the environmental impact in perspective][3]. This doesn't address data centres/infrastructure, but it gives useful context on individual choices. While he doesn't include publishing in his comparisons, the uncomfortable truth is that any reasonable individual level of LLM use probably doesn't signify against the impact of one traditional publishing cycle.

Anthony Finkelstein, president of my alma mater City, has [a provocative take on AI training and Fair Use, highlighting that copyright is a balance between creators, consumers and society, and arguing that many human creators overestimate their originality and underestimate the proximity of their work to others][4]. His view is fundamentally critical of Meta's business ethics but supportive of the underlying AI development they've undertaken (with 150 papers in LibGen, he cannot be accused of being a disinterested observer, though as a senior academic he can potentially be more relaxed about the impact than an early career researcher or more general writer).

[YouGov has new data on what people think AI is good at][5]: for publishers, it's instructive that 39% are positive about AI writing on academic topics, 35% positive on AI creative writing, and 50% positive on ability to summarise complex topics. There are also insights on AI in other areas of life that map to non-fiction publishing. It's interesting to compare that research with [recent figures from HBR on the top AI use cases in 2025][6].

After the recent story about LLM outputs in a medical textbook, researchers have found [over 700 journal articles that contained telltale signs of AI, phrases such as "as of my last knowledge update" or "as an AI language model"][7]. In some cases the response to this has been to remove the offending text but not to revisit the article itself, which seems ethically dubious. As an industry, we need to do better than this.

In terms of lessons from outside the industry, I was really interested to read a LinkedIn post from Walmart executive Jose Chapa, whom many of you might know from his time on the Amazon EU Kindle team, about Walmart's [new AI tool, Trend-to-Product, which collects fashion trend data, creates ideas and mood boards for the apparel design team to refine and sign off, and then generates a spec for the manufacturer][8]. The key metric is that it reduces the production timeline by up to 18 weeks, while retaining human control. It's an impressive looking solution for trend-driven products: it's interesting to think about what an equivalent for books/content commissioning would look like.

Finally, huge congratulations to my colleagues at Burleigh Dodds Science Publishing, [winners of the inaugural PLS AI Award at this week's Independent Publishing Awards][9]. (Disclosure: I am on the board of Burleigh Dodds, work with the IPG on AI training, and played no role in either submission or judging of that category).

This was originally published in my email newsletter. [To receive weekly updates on how AI is affecting the publishing industry, sign up here][10]. 

[1]:	https://www.theverge.com/news/653882/openai-chrome-google-us-judge
[2]:	https://openai.com/chatgpt/search-product-discovery/
[3]:	https://andymasley.substack.com/p/a-cheat-sheet-for-conversations-about
[4]:	https://profserious.substack.com/p/fair-use
[5]:	https://bsky.app/profile/petemarcus.bsky.social/post/3lnxfn5g6js2j
[6]:	https://bsky.app/profile/georgewalkley.com/post/3lnxjslu5c22o
[7]:	https://www.nature.com/articles/d41586-025-01180-2
[8]:	https://corporate.walmart.com/news/2025/04/09/in-an-ever-changing-environment-walmart-uses-genai-to-create-cool-for-customers
[9]:	https://www.independentpublishersguild.com/IPG/IPG/Events/IPA/2025%20Winners.aspx?hkey=0a94bca0-7bc2-471a-ae0e-5977d407ef28
[10]:	https://www.georgewalkley.com/newsletter/
