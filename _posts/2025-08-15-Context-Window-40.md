---
layout: post
title: Context Window 40
category: newsletter
tags: ["Artificial Intelligence", Newsletter, Publishing]
---
This edition covers OpenAI's response to GPT-5 feedback with a partial model selector and a 140,000-word context window, Drew Breunig on how long contexts fail and how to fix them, John Willshire's seven key questions for working with AI, MIT Press's survey of 6,000 authors on LLM training, Reddit blocking the Internet Archive's Wayback Machine, Neil Perkin on using AI for scenario planning, and a personal case study on using AI to size and map the UK publishing industry.

ChatGPT 5 is a week old, and already [evolving in response to frankly mixed reviews][1]. At their best, AI tools for publishing are getting more powerful, but also more opaque. The theme this week is making them work on your own terms.
​
[Last week I wrote about LLMs as Swiss Army knives][2], and the issue of GPT-5 choosing a model for the user. [OpenAI has responded to a lot of user feedback on that issue by reintroducing a limited model selector][3]: this gives users the choice of Auto, Fast or Thinking models, along with access to the legacy GPT-4o. For most users, this is a good compromise between simplicity and control.
​
OpenAI also clarified that the context window for GPT-5—that is, the amount of text that the model can consider at once when processing information—is now the equivalent of about 140,000 words, or large enough for processing most complete manuscripts if you cared to, subject to any policy and security considerations.
​
Expanding context windows and the ability to work with more data ("long contexts") have sat behind a lot of the leaps in publishing AI use over the last two years. But it's not just a case of throwing in every piece of data and getting good results. The best things I've read this week are a pair of blog posts by data strategist Drew Breunig. [The first looks at how long context windows fail][4]—when a hallucination, or superfluous content, is part of the context, when the context overwhelms the model, and where parts of the context disagree with each other. [The second post sets out a really clear set of mitigations for those problems][5]. For publishers working with large datasets already, or those that intend to, these are essential reading.
​
[Back in May, I mentioned strategist John Willshire's concept of Cognitive Debt][6], when AI gives a conclusion but the user doesn't fully understand how it got there. In his newsletter this week, John relates this to a model for understanding how people deal with information, and [seven key questions everyone should ask about AI][7]—the full piece unpacks each of these and is a must-read, and I've printed the infographic version for the wall above my desk. The seven questions are: 

1. What data was used
2. How was it collected and refined
3. How was the model trained
4. How is the interface designed
5. What outputs emerge
6. How do you perceive them
7. What are you trying to do?
	​
Late last year, MIT Press consulted 6,000 authors on their views on LLM training, and the results of that survey are discussed in a pair of guest posts on Scholarly Kitchen. [Interestingly most respondents said they were open to working with LLMs][8], albeit with clear parameters and appropriate safeguards. [The second post makes a clear series of recommendations for academic stakeholders, including multi-stakeholder scenario planning, attribution requirements and limited licenses][9] (incidentally, while the stated focus is academic publishing, this advice would be applicable to any kind of publisher).
​
Regular readers will know that access to web content for training is becoming one of the fault lines of the AI world. This week [Reddit announced that it is blocking the Internet Archive's Wayback Machine from indexing Reddit, because AI companies that are prevented from accessing the platform directly are training on data scraped from the Wayback machine][10]. The Internet Archive has a very mixed reputation with publishers, some of whom [successfully sued it for copyright infringement][11], but it's sad to see another sign of the open web giving way to walled gardens.
​
Just in time for anyone inclined to follow that MIT Press advice, [Neil Perkin published a really helpful short guide to using AI for scenario planning and stress testing strategy][12].
​
Finally, I've just done a piece of work sizing the UK publishing industry and plotting companies by location, using AI to help write scripts for data analysis and geolocation, and [I've published a write-up on my website describing how AI was used][13]. I hope it's a useful case study for how AI can support traditional research.

This was originally published in my email newsletter. [To receive weekly updates on how AI is affecting the publishing industry, sign up here][14]. 

[1]:	https://aboard.com/desperately-seeking-software/
[2]:	https://ckarchive.com/b/p9ueh9h29e6n4fm6ggw6kapv02033hrher8pe
[3]:	https://x.com/sama/status/1955438916645130740
[4]:	https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html
[5]:	https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html
[6]:	https://ckarchive.com/b/d0ueh0howx4o0ck4xx64otzp25244clh35pv3
[7]:	https://buttondown.com/artefacts/archive/artefact-251/
[8]:	https://scholarlykitchen.sspnet.org/2025/08/12/guest-post-who-controls-knowledge-in-the-age-of-ai-part-1/
[9]:	https://scholarlykitchen.sspnet.org/2025/08/13/guest-post-who-controls-knowledge-in-the-age-of-ai-part-2-recommendations-for-stakeholders/
[10]:	https://www.theverge.com/news/757538/reddit-internet-archive-wayback-machine-block-limit
[11]:	https://en.wikipedia.org/wiki/Hachette_v._Internet_Archive
[12]:	https://onlydeadfish.substack.com/p/fish-food-656-using-ai-for-simulation
[13]:	https://www.georgewalkley.com/UK-Publishing-Industry-2025/
[14]:	https://www.georgewalkley.com/newsletter/