---
layout: post
title: Context Window 97
category: newsletter
tags: ["Artificial Intelligence", Newsletter, Publishing]
---
Much of the publishing industry has been at Frankfurt this week, with lots of AI conversations and fewer tangible announcements. Elsewhere, BBC director-general Matt Brittin, a former tech executive, commented that the corporation should be ["a bit more Elvis—a little less conversation, a little more action"][1], a diagnosis that could apply to some other parts of the media landscape. With that in mind, the newsletter highlights four practical things you could do this week: building an app, developing hardware, using a new provenance tool from Google or testing Claude's new Google Workspace plugin.

[The best thing I read this week was a piece by author Robin Sloan on vibe coding the exact app he wanted][2]. There's so much that's great here: the tone, the guardrails, the approach—starting with a written spec created by hand, not AI, and asking for a plan. Most importantly, any of you could take this approach and a month of a premium LLM subscription and try it for minimal cost and boundless learning.

Of course, this is about building something for yourself, not a corporate tool. Anything that touches corporate systems or personal data, to name just two risk categories, will likely need a more deliberative approach. But for individual tasks this is an extraordinary opportunity, a "phase change" to use Robin's term. Go try it.

As a secondary thing I have a lot of sympathy for Robin's framing of the landscape:

> ["The AI industry's immediate future has more to do with exotic finance and gnarly politics than the underlying technology. I'm not invested in that future; most days, I think a minor bust would be a good thing. But, that underlying technology, in its development and flourishing this past year — yes, really that recently — is profound."][3]

In recent weeks I've written a lot about personal agents and Meta's Muse: [building on growing buzz about Muse, Meta open-sourced the code to develop hardware gadgets that work with it][4]. This is a hobbyist play more than an enterprise approach—Meta explicitly calls it a "side project"—but it will be interesting to see what ideas and uses it inspires: if you're looking for an early use case for a vibe-coded app, this could be a great learning project.

Related to personal tools, [Paul Ford wrote about building search tools with AI, in part because he lacks confidence in Google results][5]. It's about the utility of AI for reviewing and querying hundreds of information sources a day—something I suspect many publishers and information workers will empathise with (I certainly do)—but also about the need to build tools to replace the web we've lost.

An interesting bibliographic development highlighted on [the ebooks.com Book Tech newsletter][6] this week (worth subscribing if you don't already): [the Canadian ISBN Agency now requires a declaration that works were created by humans or with *de minimis* AI assistance. AI-generated works are not eligible for Canadian ISBNs][7].

This is a new layer in a stack of practical questions for AI-generated work: is it copyrightable, is it identifiable with an ISBN, does it comply with retailer policies, and how will readers react? Of course, other national ISBN agencies may take different approaches—a national library, as in the Canadian example, can gatekeep to an extent a commercial entity like Bowker or Nielsen might not—and many self-published authors don't assign ISBNs at all, especially if they're really only working within KDP. I suspect that, outside Canada, this is most interesting as a precedent and challenge for other bibliographic providers.

On the wider question of provenance, [OpenAI announced its approach to labelling AI content to comply with the EU AI Act][8]. Like Anthropic, it is relying on a statistical watermark based on word choices. But the approach is quite different to its rival, which turned on watermarking globally. OpenAI will only apply it within the EU, with global API customers able to opt in if they choose. Access to tools to detect the watermark will initially be for expert researchers only. So for publishers and other professional users investigating the provenance of text, this is unlikely to provide short-term utility.

Much more practically, [Google rolled out global access to its SynthID tool for detecting AI images, video and audio][9]. This identifies synthetic content created by Google, OpenAI and other platforms. I didn't see Adobe on the list, which has pushed a metadata-based approach, C2PA. But that omission aside, this would be a really useful and practical check, for example when publishers commission marketing materials from agencies and freelancers.

For anyone using Google Workspace, [Claude for Google Workspace is now available in beta, integrating with Google Docs, Sheets and Slides][10]. The most significant aspect is that the in-app plugin has access to the same data connectors as the user's Claude account—so, for example, if I'm working on a customer proposal, I can query a third-party data source such as a CRM or meeting notes without switching applications. This brings the Claude/Workspace experience to parity with Microsoft. The documentation also discusses creating templates as Claude skills to automate the production of routine documents. This kind of productivity improvement isn't the most eye-catching use of AI, but it could be a consistent time-saver, and it's where I'll be experimenting for the next couple of weeks.

According to investor and Y Combinator founder Paul Graham, Amazon's decision to block third-party AI agents from its platform is ["the first opportunity I've seen since Amazon was founded for a startup to create an Amazon competitor."][11] The conventional wisdom here is that logistics and shipping still give Amazon a significant competitive moat in most categories, but digital or on-demand publishing—with global identifiers, standardised products, existing logistics networks and limited physical inventory—looks close to the ideal category for agent-driven commerce. Most Amazon alternatives aren't well optimised for it. If I were Ingram or Gardners, I'd be all over this.

Finally, not purely an AI story, but it's amazing to me that no-one in the book trade press had, at the time of publishing this newsletter, covered [the announcement reported in the financial and information media since Tuesday that Informa is planning to separate its academic publishing business Taylor & Francis][12]. T&F is approaching $1 billion in revenue, with considerable AI licensing activity and partnerships with other publishers. [James Butcher breaks the announcement down here for Journalology subscribers][13]. The second- and third-order effects of a spin-out or sale could be huge.

[1]:	https://www.theguardian.com/media/2026/oct/07/bbc-boss-matt-brittin-criticism-job-cuts-junior-staff
[2]:	https://www.robinsloan.com/lab/ask-for-what-you-want/
[3]:	https://www.robinsloan.com/lab/ask-for-what-you-want/
[4]:	https://gadgets.muse.ai/
[5]:	https://mailchi.mp/aboard/zkd26k8jzm-10349447
[6]:	https://mailchi.mp/ebooks.com/book-tech-brief-k9na8ui74v-9305587
[7]:	https://www.canada.ca/en/library-archives/services/publishers/isbn/about.html
[8]:	https://openai.com/index/eu-text-provenance/
[9]:	https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/
[10]:	https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
[11]:	https://www.businessinsider.com/paul-graham-amazon-ai-agent-ban-rival-2026-10
[12]:	https://www.ft.com/content/0c8c0122-cc24-4ea5-bc7f-09bfc95d3dd1
[13]:	https://newsletter.journalology.com/p/separation-taylor-and-francis-to