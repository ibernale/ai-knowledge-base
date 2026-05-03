# AI Sources — Curated v1 (2026-04-29)

> A curated catalog of high-signal sources for AI research, news and analysis. This file is loaded into the ingest prompt as a closed-list reference. The model uses these names and URLs as primary search targets and as authority signals.
>
> Filtering principles: editorial output, real research credentials, and stable publication cadence. Pure follower-count fame is excluded; reputation among working AI practitioners is what matters.

---

## TIER 1 — PRIMARY PAPER AGGREGATORS (start here)

These three are the highest-signal entry points for "what's worth reading this week" in AI research. The ingest pipeline should always check them first, in this order, before doing any other search.

| #   | Name                                     | URL                              | What it gives you                                                                                                             |
| --- | ---------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Hugging Face Daily Papers**            | https://huggingface.co/papers    | Top arXiv papers ranked by community upvotes, refreshed daily by AK (akhaliq). The single best filter for "what's hot today". |
| 2   | **alphaXiv (Trending)**                  | https://www.alphaxiv.org/        | arXiv mirror with line-by-line annotations and trending feeds — gives reading-community signal beyond raw upvotes.            |
| 3   | **Papers with Code (Trending)**          | https://paperswithcode.com/      | Trending papers with linked open-source implementations. Strong signal for engineering-relevant work.                         |
| 4   | **Semantic Scholar (Recently Trending)** | https://www.semanticscholar.org/ | Provides citation context, TLDRs and influence scores; useful when validating that a paper actually has traction.             |
| 5   | **arXiv Sanity Lite** (Karpathy)         | https://arxiv-sanity-lite.com/   | Personal-recommendation engine over arXiv preprints; clean interface for category-filtered browsing.                          |

---

## TIER 2 — FRONTIER LAB BLOGS AND RESEARCH PAGES

Direct from the source, no intermediaries. Always treat as authoritative when they post about their own work.

| Lab                    | Blog / News                                           | Research / Publications                                |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------ |
| **Anthropic**          | https://www.anthropic.com/news                        | https://www.anthropic.com/research                     |
| **OpenAI**             | https://openai.com/blog                               | https://openai.com/research                            |
| **Google DeepMind**    | https://deepmind.google/discover/blog                 | https://deepmind.google/research/publications          |
| **Google Research**    | https://research.google/blog/                         | https://research.google/pubs/                          |
| **Meta AI (FAIR)**     | https://ai.meta.com/blog/                             | https://ai.meta.com/research/                          |
| **Mistral AI**         | https://mistral.ai/news/                              | —                                                      |
| **xAI**                | https://x.ai/blog                                     | —                                                      |
| **Cohere**             | https://cohere.com/blog                               | https://cohere.com/research                            |
| **Microsoft Research** | https://www.microsoft.com/en-us/research/blog/        | https://www.microsoft.com/en-us/research/publications/ |
| **NVIDIA Research**    | https://blogs.nvidia.com/blog/category/deep-learning/ | https://research.nvidia.com/publications               |
| **Apple ML Research**  | https://machinelearning.apple.com/                    | https://machinelearning.apple.com/research             |
| **Allen AI (AI2)**     | https://allenai.org/blog                              | https://allenai.org/papers                             |
| **Hugging Face Blog**  | https://huggingface.co/blog                           | —                                                      |
| **DeepSeek**           | https://api-docs.deepseek.com/news                    | https://github.com/deepseek-ai                          |
| **Qwen / Alibaba DAMO**| https://qwenlm.github.io/blog/                        | —                                                      |
| **Moonshot AI / Kimi** | https://kimi.moonshot.cn/                             | —                                                      |
| **01.AI / Yi**         | https://01.ai/                                        | —                                                      |
| **Zhipu AI / GLM**     | https://www.zhipuai.cn/en/                            | https://github.com/THUDM                                |
| **Baichuan**           | https://www.baichuan-ai.com/                          | —                                                      |
| **Scale AI Research**  | https://scale.com/research                            | —                                                      |
| **Mosaic / Databricks**| https://www.databricks.com/blog/category/generative-ai | —                                                     |
| **Together AI**        | https://www.together.ai/blog                          | —                                                      |
| **Inflection AI**      | https://inflection.ai/news                            | —                                                      |

---

## TIER 3 — UNIVERSITY AI LABS (BLOGS AND PUBLICATIONS)

| Institution | Source | URL |
|---|---|---|
| Stanford HAI | Blog and AI Index | https://hai.stanford.edu/news |
| Stanford CRFM | Blog | https://crfm.stanford.edu/ |
| MIT CSAIL | News | https://www.csail.mit.edu/news |
| MIT Sloan (Digital Economy) | Initiative on the Digital Economy | https://ide.mit.edu/insights/ |
| UC Berkeley BAIR | Blog | https://bair.berkeley.edu/blog/ |
| Carnegie Mellon LTI | News | https://www.lti.cs.cmu.edu/news-and-events |
| Princeton CITP | Center for IT Policy | https://citp.princeton.edu/ |
| NYU Center for Data Science | News | https://nyudatascience.medium.com/ |
| Oxford Internet Institute | News | https://www.oii.ox.ac.uk/news-events/ |
| ETH Zurich AI Center | News | https://ai.ethz.ch/news-and-events.html |
| University of Washington | Allen School blog | https://news.cs.washington.edu/ |
| Cambridge | Computer Lab + Centre for AI in Medicine | https://www.cst.cam.ac.uk/research |
| EPFL | News and Research | https://www.epfl.ch/research/about/ |
| MILA (Quebec AI Institute) | Publications | https://mila.quebec/en/publications/ |
| Vector Institute (Toronto) | News | https://vectorinstitute.ai/news/ |
| University of Toronto | DCS news | https://web.cs.toronto.edu/news |
| Johns Hopkins CLSP | News | https://www.clsp.jhu.edu/news/ |
| Cornell CIS / Cornell Tech | News | https://www.cs.cornell.edu/news |
| USC Information Sciences Institute | News | https://www.isi.edu/news/ |
| KAIST AI | News (English) | https://gsai.kaist.ac.kr/news/ |
| Tsinghua AI | News (English) | https://ai.tsinghua.edu.cn/en/News/News.htm |
| Hong Kong U | CSE News | https://www.cse.cuhk.edu.hk/news/ |
| National University of Singapore | Computing news | https://www.comp.nus.edu.sg/news/ |
| Yale | CS news | https://cpsc.yale.edu/news |
| Columbia | CS news | https://www.cs.columbia.edu/news/ |
| UPenn | CIS news | https://www.cis.upenn.edu/news/ |
| Imperial College London | Computing news | https://www.imperial.ac.uk/computing/news/ |
| TU Munich | Informatics news | https://www.cs.cit.tum.de/en/cit/news/ |
| University of Edinburgh | Informatics news | https://informatics.ed.ac.uk/news |

---

## TIER 4 — TOP 50 INDIVIDUALS (X / BLOGS / SUBSTACKS — INTEGRATED)

The ingest pipeline searches by author name to surface their writing across whatever channels they currently use. A single entry per person captures all their main outputs. Primary editorial channel is listed first; X handle is informational only (X content is not scraped — see "X / Twitter Note" at the end of this file).

The list is organised by category. Order within category is alphabetical, not ranked.

### 4a. Frontier-lab and senior researcher voices (core signal)

| # | Name | Primary writing | X handle |
|---|---|---|---|
| 1 | **Andrej Karpathy** (ex-OpenAI, ex-Tesla, Eureka Labs) | https://karpathy.github.io/ • https://github.com/karpathy | @karpathy |
| 2 | **Yann LeCun** (Meta Chief AI Scientist, NYU) | https://yann.lecun.com/ | @ylecun |
| 3 | **Geoffrey Hinton** (U. Toronto) | https://www.cs.toronto.edu/~hinton/ | @geoffreyhinton |
| 4 | **Demis Hassabis** (Google DeepMind CEO) | DeepMind blog (above) | @demishassabis |
| 5 | **Yoshua Bengio** (MILA) | https://yoshuabengio.org/ | — |
| 6 | **Fei-Fei Li** (Stanford HAI, World Labs) | https://hai.stanford.edu/people/fei-fei-li | @drfeifei |
| 7 | **Jeff Dean** (Google DeepMind & Google Research) | Google Research blog (above) | @jeffdean |
| 8 | **Oriol Vinyals** (Google DeepMind, Gemini lead) | DeepMind blog (above) | @oriolvinyalsml |
| 9 | **Ilya Sutskever** (SSI, ex-OpenAI) | https://ssi.inc/ | @ilyasut |
| 10 | **Andrew Ng** (DeepLearning.AI, Stanford) | https://www.deeplearning.ai/the-batch/ | @AndrewYNg |
| 11 | **Ian Goodfellow** (DeepMind) | DeepMind blog (above) | @goodfellow_ian |
| 12 | **François Chollet** (Keras, ARC Prize) | https://fchollet.com/ | @fchollet |
| 13 | **Lilian Weng** (ex-OpenAI, applied research) | https://lilianweng.github.io/ | @lilianweng |
| 14 | **Chris Olah** (Anthropic, interpretability) | https://colah.github.io/ • https://transformer-circuits.pub/ | @ch402 |
| 15 | **Jack Clark** (Anthropic, AI policy) | https://importai.substack.com/ • https://jack-clark.net/ | @jackclarkSF |
| — | **Pieter Abbeel** (UC Berkeley, Covariant) | https://people.eecs.berkeley.edu/~pabbeel/ | @pabbeel |
| — | **Sergey Levine** (UC Berkeley, robotics + RL) | https://people.eecs.berkeley.edu/~svlevine/ | @svlevine |
| — | **Stuart Russell** (UC Berkeley, AI safety) | https://people.eecs.berkeley.edu/~russell/ | — |
| — | **Christopher Manning** (Stanford NLP) | https://nlp.stanford.edu/~manning/ | @chrmanning |
| — | **Percy Liang** (Stanford CRFM) | https://cs.stanford.edu/~pliang/ | @percyliang |
| — | **Christopher Ré** (Stanford CRFM, Together AI) | https://cs.stanford.edu/~chrismre/ | @HazyResearch |
| — | **Sam Altman** (OpenAI CEO) | https://blog.samaltman.com/ | @sama |
| — | **Dario Amodei** (Anthropic CEO) | https://www.darioamodei.com/ | — |
| — | **Greg Brockman** (OpenAI President) | https://gregbrockman.com/ | @gdb |
| — | **John Schulman** (Anthropic, ex-OpenAI co-founder) | https://joschu.net/ | @johnschulman2 |
| — | **Mira Murati** (Thinking Machines Lab) | https://thinkingmachines.ai/ | @miramurati |
| — | **Mustafa Suleyman** (Microsoft AI, ex-DeepMind) | — | @mustafasuleyman |
| — | **Aravind Srinivas** (Perplexity CEO) | — | @AravSrinivas |
| — | **Aidan Gomez** (Cohere CEO) | https://aidangomez.ca/ | @aidangomezzz |
| — | **Noam Shazeer** (Google, ex-Character AI) | — | @noamshazeer |
| — | **Jason Wei** (Anthropic, ex-OpenAI) | https://www.jasonwei.net/ | @_jasonwei |
| — | **Yi Tay** (Reka, ex-Google Brain) | https://www.yitay.net/ | @YiTayML |
| — | **Thomas Wolf** (Hugging Face co-founder) | https://thomwolf.io/ | @Thom_Wolf |
| — | **Clément Delangue** (Hugging Face CEO) | — | @ClementDelangue |
| — | **Shane Legg** (DeepMind co-founder, Chief AGI Scientist) | — | — |
| — | **Max Tegmark** (MIT, Future of Life Institute) | https://space.mit.edu/home/tegmark/ | @tegmark |
| — | **Nick Bostrom** (Macrostrategy Research) | https://nickbostrom.com/ | @nickbostrom |
| — | **Dawn Song** (UC Berkeley) | https://dawnsong.io/ | @dawnsongtweets |
| — | **Tatsunori Hashimoto** (Stanford) | https://thashim.github.io/ | @tatsu_hashimoto |
| — | **Yejin Choi** (UW, Stanford) | https://yejinchoi.com/ | @YejinChoinka |
| — | **Ed Chi** (Google DeepMind) | https://research.google/people/106214/ | — |
| — | **Aleksander Mądry** (MIT, OpenAI) | https://madry-lab.ml/ | — |

### 4b. Independent researchers, educators and writers (technical depth)

| # | Name | Primary writing | X handle |
|---|---|---|---|
| 16 | **Sebastian Raschka** | https://magazine.sebastianraschka.com/ — *Ahead of AI* | @rasbt |
| 17 | **Chip Huyen** | https://huyenchip.com/blog/ | @chipro |
| 18 | **Simon Willison** | https://simonwillison.net/ | @simonw |
| 19 | **Jay Alammar** | https://jalammar.github.io/ | @JayAlammar |
| 20 | **Eugene Yan** | https://eugeneyan.com/writing/ | @eugeneyan |
| 21 | **Nathan Lambert** | https://www.interconnects.ai/ | @natolambert |
| 22 | **Jeremy Howard** (fast.ai, answer.ai) | https://www.fast.ai/blog | @jeremyphoward |
| 23 | **Christopher Manning** (Stanford NLP) | https://nlp.stanford.edu/~manning/ | @chrmanning |
| 24 | **Sebastian Ruder** | https://www.ruder.io/ — *NLP News* | @seb_ruder |
| 25 | **Eliezer Yudkowsky** (MIRI, AI safety) | https://www.lesswrong.com/users/eliezer_yudkowsky | @ESYudkowsky |
| 26 | **Gary Marcus** | https://garymarcus.substack.com/ | @GaryMarcus |
| 27 | **Cameron Wolfe** (Deep Learning Focus) | https://cameronrwolfe.substack.com/ | @cwolferesearch |
| 28 | **Tim Dettmers** | https://timdettmers.com/ | @Tim_Dettmers |
| 29 | **Janelle Shane** (AI Weirdness) | https://www.aiweirdness.com/ | @JanelleCShane |
| 30 | **Christoph Molnar** (interpretable ML) | https://christophm.github.io/ | — |

### 4c. Industry analysts, builders and operators

| # | Name | Primary writing | X handle |
|---|---|---|---|
| 31 | **Ethan Mollick** (Wharton) | https://www.oneusefulthing.org/ | @emollick |
| 32 | **Benedict Evans** | https://www.ben-evans.com/ | @benedictevans |
| 33 | **Ben Thompson** (Stratechery) | https://stratechery.com/ | @benthompson |
| 34 | **Azeem Azhar** (Exponential View) | https://www.exponentialview.co/ | @azeem |
| 35 | **Nathan Benaich** (State of AI Report) | https://nathanbenaich.substack.com/ | @nathanbenaich |
| 36 | **Swyx (Shawn Wang)** (Latent Space) | https://www.latent.space/ | @swyx |
| 37 | **Alessio Fanelli** (Latent Space co-host) | https://www.latent.space/ | @FanaHOVA |
| 38 | **Dwarkesh Patel** (Dwarkesh Podcast) | https://www.dwarkeshpatel.com/ | @dwarkesh_sp |
| 39 | **Hamel Husain** (LLM eval, fine-tuning) | https://hamel.dev/ | @HamelHusain |
| 40 | **Jeremy Nixon** | — | @jeremynixon |
| 41 | **Rohit Krishnan** | https://www.strangeloopcanon.com/ | @krishnanrohit |
| 42 | **Dean W. Ball** (Hyperdimensional, AI policy) | https://www.hyperdimensional.co/ | @deanwball |

### 4d. AI safety, alignment and policy

| # | Name | Primary writing | X handle |
|---|---|---|---|
| 43 | **Paul Christiano** (US AI Safety Institute) | https://paulfchristiano.com/ai/ • https://ai-alignment.com/ | — |
| 44 | **Dan Hendrycks** (CAIS) | https://newsletter.safe.ai/ | @DanHendrycks |
| 45 | **Holden Karnofsky** (Anthropic) | https://www.cold-takes.com/ | @holdenkarnofsky |
| 46 | **Ajeya Cotra** (Open Philanthropy) | https://www.planned-obsolescence.org/ | — |
| 47 | **Helen Toner** (CSET, Georgetown) | https://www.helentoner.com/ | @hlntnr |
| 48 | **Kate Crawford** (USC, Microsoft Research) | https://katecrawford.net/ | @katecrawford |
| 49 | **Timnit Gebru** (DAIR) | https://www.dair-institute.org/ | @timnitgebru |
| 50 | **Erik Brynjolfsson** (Stanford Digital Economy Lab) | https://digitaleconomy.stanford.edu/ | @erikbryn |

### 4e. Builders, framework authors, developer-experience leads (engineering depth)

| # | Name | Primary writing | X handle |
|---|---|---|---|
| 51 | **Phil Schmid** (Hugging Face / Google) | https://www.philschmid.de/blog | @_philschmid |
| 52 | **Charlie Marsh** (Astral — Ruff/uv) | https://crmarsh.com/ | @charliermarsh |
| 53 | **Harrison Chase** (LangChain CEO) | https://blog.langchain.com/author/harrison-chase/ | @hwchase17 |
| 54 | **Greg Kamradt** | https://www.greggkamradt.com/ | @GregKamradt |
| 55 | **Logan Markewich** (LlamaIndex) | https://logan-markewich.medium.com/ | @LoganMarkewich |
| 56 | **Geoffrey Litt** (Ink & Switch, local-first) | https://www.geoffreylitt.com/ | @geoffreylitt |
| 57 | **Jason Liu** (Instructor) | https://jxnl.co/writing/ | @jxnlco |
| 58 | **Will Larson** | https://lethain.com/ | @lethain |
| 59 | **Erik Bernhardsson** (Modal) | https://erikbern.com/ | @bernhardsson |
| 60 | **Patrick McKenzie (patio11)** | https://www.kalzumeus.com/ | @patio11 |
| 61 | **Eli Bendersky** | https://eli.thegreenplace.net/ | — |
| 62 | **Riley Goodside** (Scale AI, prompt eng) | https://x.com/goodside | @goodside |
| 63 | **Yoav Goldberg** (Bar-Ilan, AI2) | https://www.cs.biu.ac.il/~yogo/ | — |
| 64 | **Sara Hooker** (Cohere For AI) | https://www.sarahooker.me/ | @sarahookr |
| 65 | **Ross Wightman** (timm, Hugging Face) | https://github.com/rwightman | @wightmanr |
| 66 | **Aleksa Gordić** | https://gordicaleksa.com/ | @gordic_aleksa |
| 67 | **Lex Sokolin** (autonomous finance + AI) | https://thefintechblueprint.com/ | @LexSokolin |
| 68 | **Stas Bekman** (training infra) | https://github.com/stas00 | — |

---

## TIER 5 — TOP 50 BLOGS, NEWSLETTERS AND PUBLICATIONS

Editorial outlets with stable cadence. The ingest pipeline checks for new posts in this list; "weekly digest" newsletters (#1–10) are primary entry points.

### 5a. Weekly/daily digests (best signal-aggregators)

| # | Publication | URL | Cadence |
|---|---|---|---|
| 1 | **Import AI** (Jack Clark) | https://importai.substack.com/ | Weekly |
| 2 | **The Batch** (Andrew Ng / DeepLearning.AI) | https://www.deeplearning.ai/the-batch/ | Weekly |
| 3 | **Last Week in AI** (Andrey Kurenkov et al.) | https://lastweekin.ai/ | Weekly |
| 4 | **AI News (Smol AI)** | https://news.smol.ai/ | Daily |
| 5 | **Latent Space** (Swyx & Alessio) | https://www.latent.space/ | Weekly + podcast |
| 6 | **Interconnects** (Nathan Lambert) | https://www.interconnects.ai/ | Weekly |
| 7 | **Ahead of AI** (Sebastian Raschka) | https://magazine.sebastianraschka.com/ | Bi-weekly |
| 8 | **One Useful Thing** (Ethan Mollick) | https://www.oneusefulthing.org/ | Weekly |
| 9 | **Davis Summarizes Papers** (Davis Blalock) | https://dblalock.substack.com/ | Weekly |
| 10 | **Data Machina** | https://datamachina.substack.com/ | Weekly |

### 5b. Long-form analysis and commentary

| # | Publication | URL |
|---|---|---|
| 11 | **Stratechery** (Ben Thompson) | https://stratechery.com/ |
| 12 | **Exponential View** (Azeem Azhar) | https://www.exponentialview.co/ |
| 13 | **The Algorithmic Bridge** (Alberto Romero) | https://www.thealgorithmicbridge.com/ |
| 14 | **AI Snake Oil** (Narayanan & Kapoor, Princeton) | https://www.aisnakeoil.com/ |
| 15 | **Hyperdimensional** (Dean W. Ball) | https://www.hyperdimensional.co/ |
| 16 | **Marginalia / Cold Takes** (Holden Karnofsky) | https://www.cold-takes.com/ |
| 17 | **Asterisk Magazine** (long-form rationalist tech) | https://asteriskmag.com/ |
| 18 | **Construction Physics + Astral Codex Ten** (cross-pollination) | https://www.astralcodexten.com/ |
| 19 | **Alignment Forum** | https://www.alignmentforum.org/ |
| 20 | **LessWrong (curated)** | https://www.lesswrong.com/ |

### 5c. Technical / engineering blogs

| # | Publication | URL |
|---|---|---|
| 21 | **Distill** (legacy archive but foundational) | https://distill.pub/ |
| 22 | **Transformer Circuits Thread** (Anthropic) | https://transformer-circuits.pub/ |
| 23 | **Andrew Ng's blog (Stanford)** | https://www.andrewng.org/ |
| 24 | **Berkeley BAIR Blog** | https://bair.berkeley.edu/blog/ |
| 25 | **Stanford AI Lab Blog** | https://ai.stanford.edu/blog/ |
| 26 | **CMU Machine Learning Blog** | https://blog.ml.cmu.edu/ |
| 27 | **Off the Convex Path** (Sanjeev Arora et al.) | https://www.offconvex.org/ |
| 28 | **The Gradient** | https://thegradient.pub/ |
| 29 | **Towards Data Science** (high-quality posts only) | https://towardsdatascience.com/ |
| 30 | **Eugene Yan's writing** | https://eugeneyan.com/writing/ |
| 31 | **Hamel Husain's blog** | https://hamel.dev/ |
| 32 | **Lil'Log** (Lilian Weng) | https://lilianweng.github.io/ |
| 33 | **Karpathy's blog** | https://karpathy.github.io/ |
| 34 | **Jay Alammar — Visualizing ML** | https://jalammar.github.io/ |
| 35 | **Sebastian Ruder — NLP News** | https://www.ruder.io/ |

### 5d. AI policy and governance

| # | Publication | URL |
|---|---|---|
| 36 | **CSET Newsletter** (Georgetown) | https://cset.georgetown.edu/publications/ |
| 37 | **Stanford HAI Policy Briefs** | https://hai.stanford.edu/research/policy |
| 38 | **AI Safety Newsletter** (CAIS) | https://newsletter.safe.ai/ |
| 39 | **GovAI** (Oxford) | https://www.governance.ai/ |
| 40 | **Anthropic Policy** | https://www.anthropic.com/policy |
| — | **METR (Model Evaluation & Threat Research)** | https://metr.org/ |
| — | **Apollo Research** | https://www.apolloresearch.ai/research |
| — | **Redwood Research** | https://www.redwoodresearch.org/ |
| — | **FAR AI** | https://far.ai/ |
| — | **AI Now Institute** | https://ainowinstitute.org/publications |
| — | **Future of Privacy Forum** | https://fpf.org/blog/ |
| — | **Carnegie Endowment AI** | https://carnegieendowment.org/topic/2068 |
| — | **RAND AI policy** | https://www.rand.org/research/topics/artificial-intelligence.html |
| — | **Brookings — AI** | https://www.brookings.edu/topic/artificial-intelligence/ |
| — | **Atlantic Council — Cyber & Tech** | https://www.atlanticcouncil.org/programs/scowcroft-center-for-strategy-and-security/cyber-statecraft-initiative/ |

### 5e. Investor / industry intelligence

| # | Publication | URL |
|---|---|---|
| 41 | **State of AI Report** (Nathan Benaich, annual) | https://www.stateof.ai/ |
| 42 | **Air Street Press** (Nathan Benaich) | https://press.airstreet.com/ |
| 43 | **a16z AI Newsletter** | https://a16z.com/ai/ |
| 44 | **Sequoia Capital — AI Notes** | https://www.sequoiacap.com/ |
| 45 | **Big Technology** (Alex Kantrowitz) | https://www.bigtechnology.com/ |
| 46 | **The Information — AI section** | https://www.theinformation.com/ |
| 47 | **MIT Technology Review — AI** | https://www.technologyreview.com/topic/artificial-intelligence/ |
| 48 | **Wired — AI** | https://www.wired.com/tag/artificial-intelligence/ |
| 49 | **Semafor Tech** | https://www.semafor.com/vertical/technology |
| 50 | **AI Index Report** (Stanford HAI, annual) | https://aiindex.stanford.edu/ |

### 5e-bis. Top VC funds with AI thesis (publish substantive theses, not just deal news)

The model should sweep these for new long-form thesis posts (market maps, technical deep-dives, infrastructure breakdowns) — not portfolio-company press releases.

| # | Fund | URL |
|---|---|---|
| — | **Andreessen Horowitz (a16z)** — AI | https://a16z.com/ai/ |
| — | **a16z Future** | https://future.com/ |
| — | **Sequoia Capital** | https://www.sequoiacap.com/perspectives/ |
| — | **Khosla Ventures** | https://www.khoslaventures.com/blog/ |
| — | **Founders Fund** | https://foundersfund.com/ |
| — | **Index Ventures** | https://www.indexventures.com/perspectives/ |
| — | **Accel** | https://www.accel.com/noteworthy |
| — | **Lux Capital** (deep-tech / AI infra) | https://www.luxcapital.com/news |
| — | **General Catalyst** | https://www.generalcatalyst.com/perspectives/ |
| — | **Greylock** (Reid Hoffman, Saam Motamedi) | https://greylock.com/perspectives/ |
| — | **Kleiner Perkins** | https://www.kleinerperkins.com/perspectives/ |
| — | **Bessemer Venture Partners** (State of the Cloud, Roadmaps) | https://www.bvp.com/atlas |
| — | **Conviction** (Sarah Guo) | https://www.conviction.com/perspectives |
| — | **Menlo Ventures** | https://menlovc.com/perspective/ |
| — | **Air Street Capital** (Nathan Benaich) | https://press.airstreet.com/ |
| — | **Battery Ventures** | https://www.battery.com/blog/ |
| — | **CRV** | https://www.crv.com/perspectives |
| — | **NEA** | https://www.nea.com/perspectives |
| — | **Insight Partners** | https://www.insightpartners.com/ideas/ |
| — | **IVP** | https://www.ivp.com/insights/ |
| — | **Coatue** | https://www.coatue.com/insights |
| — | **Tiger Global** | https://www.tigerglobal.com/ |
| — | **SoftBank Vision Fund** | https://visionfund.com/news |
| — | **Initialized Capital** (Garry Tan) | https://initialized.com/perspectives |
| — | **Madrona Ventures** (Seattle AI) | https://www.madrona.com/category/perspectives/ |
| — | **Felicis** | https://www.felicis.com/insights |
| — | **8VC** | https://8vc.com/research |
| — | **First Round Capital** | https://review.firstround.com/ |

---

## TIER 6 — ACADEMIC AND PREPRINT VENUES

These are the corpora the ingest pipeline mines for new papers. Always check published_date against the search window. During an active conference accepted-papers window, the conference page is a primary source.

### Preprint servers

| Venue | URL | Notes |
|---|---|---|
| **arXiv cs.LG** | https://arxiv.org/list/cs.LG/recent | Core ML category |
| **arXiv cs.CL** | https://arxiv.org/list/cs.CL/recent | NLP |
| **arXiv cs.AI** | https://arxiv.org/list/cs.AI/recent | General AI |
| **arXiv cs.CV** | https://arxiv.org/list/cs.CV/recent | Computer Vision |
| **arXiv cs.RO** | https://arxiv.org/list/cs.RO/recent | Robotics |
| **arXiv stat.ML** | https://arxiv.org/list/stat.ML/recent | Statistical ML |
| **OpenReview** | https://openreview.net/ | Conference review platform — pre-publication signal |
| **Semantic Scholar** | https://www.semanticscholar.org/ | Citation context, TLDRs, influence scores |

### Top-tier ML / AI conferences (general)

| Venue | URL | Notes |
|---|---|---|
| **NeurIPS** | https://neurips.cc/ | December — flagship ML conference |
| **ICML** | https://icml.cc/ | July — top ML conference |
| **ICLR** | https://iclr.cc/ | Spring — open-review process |
| **AAAI** | https://aaai.org/conference/aaai/ | February — broad AI |
| **IJCAI** | https://www.ijcai.org/ | August — international AI |
| **AISTATS** | https://aistats.org/ | Statistical AI |
| **UAI** | https://www.auai.org/ | Uncertainty in AI |

### NLP and language models

| Venue | URL | Notes |
|---|---|---|
| **ACL Anthology** | https://aclanthology.org/ | NLP venue archive (ACL, EMNLP, NAACL, EACL, COLING, TACL) |
| **ACL** | https://www.aclweb.org/portal/ | Association for Computational Linguistics |
| **EMNLP** | https://2025.emnlp.org/ | Empirical Methods in NLP |
| **NAACL** | https://2025.naacl.org/ | North American chapter ACL |
| **COLM** | https://colmweb.org/ | Conference on Language Modeling — newer, LLM-focused |

### Computer vision and multimodal

| Venue | URL | Notes |
|---|---|---|
| **CVPR** | https://cvpr.thecvf.com/ | June — top vision conference |
| **ECCV** | https://eccv.ecva.net/ | Biennial European vision |
| **ICCV** | https://iccv.thecvf.com/ | Biennial international vision |
| **SIGGRAPH** | https://s2025.siggraph.org/ | Graphics + generative content |

### Robotics, RL, embodied AI

| Venue | URL | Notes |
|---|---|---|
| **RSS** (Robotics: Science and Systems) | https://roboticsconference.org/ | Robotics flagship |
| **CoRL** (Conference on Robot Learning) | https://www.corl.org/ | Robot learning |
| **ICRA** | https://www.icra2025.org/ | International Conference on Robotics and Automation |

### AI ethics, fairness, accountability

| Venue | URL | Notes |
|---|---|---|
| **FAccT** (Fairness, Accountability, Transparency) | https://facctconference.org/ | ACM venue, AI ethics flagship |
| **AIES** (AI, Ethics & Society) | https://www.aies-conference.com/ | AAAI/ACM joint conference |
| **EAAMO** (Equity & Access in Algorithms, Mechanisms, Optimization) | https://eaamo.org/ | Algorithmic equity |

### Knowledge discovery and applied ML

| Venue | URL | Notes |
|---|---|---|
| **KDD** | https://kdd.org/ | Knowledge Discovery and Data Mining |
| **WWW (The Web Conf)** | https://www.thewebconf.org/ | Web / search / IR |
| **RecSys** | https://recsys.acm.org/ | Recommender systems |
| **SIGIR** | https://sigir.org/ | Information retrieval |

---

## TIER 7 — CONSULTANCY AND INSTITUTIONAL REPORTS (when AI-focused)

Lower frequency than blogs/papers but high signal when published.

- McKinsey QuantumBlack: https://www.mckinsey.com/quantumblack
- BCG Henderson Institute / GenAI: https://www.bcg.com/x/center-for-digital-government
- Deloitte Insights — AI: https://www.deloitte.com/global/en/services/consulting/research.html
- Gartner Hype Cycle (when refreshed): https://www.gartner.com/en/research/methodologies/gartner-hype-cycle
- Stanford AI Index (annual): https://aiindex.stanford.edu/
- WEF AI Reports: https://www.weforum.org/topics/artificial-intelligence/
- OECD AI Observatory: https://oecd.ai/

---

## X / Twitter — Operational Note

The 50 individuals in **Tier 4** all maintain editorial output beyond X (blog, Substack, papers, talks). The ingest pipeline does **not** scrape X directly because:
1. X's API is not freely accessible at viable cost (200 USD/month minimum for read access).
2. X's terms of service restrict systematic storage of tweets outside the platform.
3. Most genuinely important things any of these people post on X get covered within 24-72 hours by digests in Tier 5a (Import AI, AI News, Last Week in AI, Latent Space).

The pipeline therefore uses Tier 4 names as **author signals** — when searching, the model boosts results that mention these names, and follows their primary blog/Substack/research URLs directly. X handles are kept here for human reference (e.g. for the user to follow these accounts manually) but are not used as crawl targets.

---

## How this file plugs into the ingest

The script reads `sources.md` at startup. The ingest prompt is updated to:
1. Treat Tier 1 (paper aggregators) as the first stop on every run.
2. Treat Tier 2 (frontier labs) as authoritative for their own announcements.
3. Use Tier 3 + Tier 6 for primary academic crawl.
4. Use Tier 4 names as author-priority signals when ranking arXiv candidates.
5. Use Tier 5a (digests) as a reflector of what got tractioned in the last 24-72h.
6. Treat Tier 5b–5e as primary sources for analysis and policy items.
7. Treat Tier 7 as low-frequency, high-priority-when-present.
