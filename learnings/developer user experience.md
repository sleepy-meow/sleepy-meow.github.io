*UX + ways of working*

Most of us understand the value of ux in the products we build. But an often overlooked aspect is how those same principles can be applied to finding optimal ways of working and internal tooling.
# ways of working have a user experience

A tool, a meeting, a handoff, or a process can either make that work easier, or require people to remember unwritten rules, search for information, repeat themselves, and work around obstacles.

The same questions we ask about a user interface apply here: Is it clear what to do next? Can people find what they need? Do they know what happened after taking action? Can they recover from a mistake?

[Usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) provide useful prompts for noticing this friction. A request that disappears without acknowledgment is a visibility problem. A workflow that depends on remembering instructions from a meeting places a burden on memory. A temporary process with no way to revisit it leaves people stuck.

Some useful questions
- *How does this impact the cognitive load of individuals and the team overall, in the long run?*
- *How does this scale? (and does it need to)*
- *What are we actually trying to solve here?*

# example: daily team updates
Suppose we want people to keep up to date what their teammates are working on.

**Option 1: a bot asks “what is everyone working on?” in the team channel each day, with updates collected in a thread.**
The prompt removes the need to remember to post. But responding means pausing work, recalling progress, deciding what matters, and composing an update, even when nothing has changed since yesterday. 

Readers have work to do too. The first person to post sees an empty thread. To learn what others are doing, they need to return as replies arrive and distinguish new information from what they’ve already read. Previous days’ threads become buried among unrelated messages. Following someone’s progress means finding several threads and mentally piecing their updates together.

**Option 2: a dedicated channel, with updates when something changes.**
People can catch up and post in one visit at a convenient time. The continuous history includes everyone’s latest updates, even for the first person checking that morning. There is no need to wait for replies to a new daily thread.

The agreement is that an update remains current until replaced, so unchanged work doesn’t need another report. Discussion stays beneath each post. This reduces duplicate writing, repeat visits, and the effort of piecing together information across daily threads. 

Small things like these add up over time, and we tend to often vastly underestimate the scale of recurring interruptions that affect many people. 
# the cost of interrupted work
*Spending 50% on one project and 50% on another does not add up to 100%.*

On average, 9-23 minutes is lost each time context switching. Our brains cannot actually focus on two things at the same time, but rapidly switch between the two.

![[Pasted image 20260831150953.png|425]]

> [!EXAMPLE] [context switching - how to reduce it and achieve flow state](https://www.taskade.com/blog/reduce-context-switching)

*"some people are just better at multitasking"*
Self-perception of being good at multitasking or getting more done while multitasking is frequently inaccurate. Multitasking is mentally and physically stressful for everyone to the point that multitasking is used in laboratory experiments to study stressful environments.

The distance between contexts also matters. This is why an artist solving a technical issue will expend more energy than a programmer who is already in a technical problem solving mindset.


> [!EXAMPLE] research paper: [The Cost of Interrupted Work: More Speed and Stress](https://ics.uci.edu/~gmark/chi08-mark.pdf)

This is also why it's a good idea to have breaks in between meetings. Running from one meeting to the next without any space in between may feel productive, but whether you're actually present at the beginning and end of the meeting is another question.

# cognitive accessibility
> “No single way of working, from where or when we work to how we communicate, is optimal for all of us. Implementing flexibility at the core of policies and practices can be a game changer for your teams’ efficiency.”

Our brains work in different ways, and what may seem trivial to one person may be very draining for someone else. This isn't a deficiency, just that people have different strengths, and accommodating them increases the amount of divergent thinking, which in turn, leads to more innovation.

(For reasons you may not want for everyone in the room to think the same way, check out this article about [groupthink](https://www.atlassian.com/blog/teamwork/groupthink))

> [!EXAMPLE] [unlocking the power of neurodiversity in game development](https://news.ubisoft.com/en-us/article/4MdbqYqnJ4Mk2PGD5hjdYf/gdc-2023-unlocking-the-power-of-neurodiversity-in-game-development)

> [!EXAMPLE] [Beyond Compliance_A User-Autonomy Framework for Inclusive and Customizable Web Accessibility.pdf](attachment:704d9525-a9b2-4cc3-a82e-32e9fd7eb5bc:Beyond_Compliance_A_User-Autonomy_Framework_for_Inclusive_and_Customizable_Web_Accessibility.pdf)

# understanding UX helps us make better decisions

Understanding UX gives us a better basis for choosing tools and ways of working, and helps us ask better questions before committing to a solution. 

This is where [UX maturity](https://www.nngroup.com/articles/ux-maturity-model/) becomes relevant. An organization can have people who understand these issues, yet make decisions without using their knowledge. Greater maturity means giving that understanding (and evidence from the people doing the work) a consistent role in priorities, design choices, and evaluation.

The principles don’t tell us which option is always best. They help us notice the trade-offs, test our assumptions, and make more informed decisions.


> [!TIP] [Designing the User Experience of Game Development Tools](https://uxofgametools.com/) (the best book ever on this topic, very condensed and practical advice)

> [!TIP] Reid Hoffman - Masters of Scale (the book, not the podcast)


%%
# watch where the effort goes

People get used to inefficient workflows. They may stop noticing the workarounds, assume nothing can change, or blame themselves for finding something difficult. A lack of complaints doesn’t tell us that the experience is good.

Sit with someone while they do the work. Notice where they pause, search, switch tools, repeat information, or ask someone for help. Ask what they are trying to accomplish and why they take those steps.

Then consider the whole workflow. Does the proposed improvement reduce effort overall, or just move it to someone else? A daily update might make a lead’s job easier while requiring twenty people to duplicate information already available elsewhere. Fewer clicks aren’t necessarily better if the remaining steps require more thinking and remembering.

# improve it with the people using it

Start with a specific difficulty and try a small change. That might be a scrappy tool prototype, a clearer handoff, a shorter meeting, or an example added where people regularly get stuck.

Involve the people affected while their input can still change the design. Watch whether the change helps, including what it costs to learn and maintain, then adjust.

The aim is to spend less effort navigating the tools and processes around the work, leaving more attention for the work itself.



Some useful things to ask yourself when improving ways of working/workflows/pipelines:
- *How does this impact the cognitive load of individuals and the team overall, in the long run?*
- *How does this scale? (and does it need to)*
- *What are we actually trying to solve here?*
- 

# useful methods
## 5 whys
To identify the root cause of a problem by asking **why** **5** times.

## user centered design
An iterative approach that involves users throughout the design process, ensuring a product reflects their real needs, goals, and context—not just the design team’s assumptions.

It's basically *a continuous learning cycle*:

1. Learn about users—their goals, context, needs, and difficulties.
2. Design based on that understanding.
3. Test with users and observe what works.
4. Refine the design using what you learned.
5. Repeat as users, needs, and circumstances change.

The goal isn’t to understand users once—it’s to keep replacing assumptions with evidence throughout the product’s life.




==todo: maybe just focus why this matters & leave the details on the original page + links to best practices + choose a few most important points to not make this page way too long==

==todo2: a few concrete examples + explain the reasoning behind them==
- ==that one tool everyone used and it took ages for the first person to complain about it==
- ==daily syncs / updates==
- 

==todo3: explain how the whole ux maturity thing matters==

==how to not get blind to all the wasted time==


# start with the users
> “You’ve got to start with the customer experience and work back toward the technology - not the other way around.” -Steve Jobs
# Defining user experience

User experience refers to how a user interacts with and operates a product, system, or service, including perceptions of utility, ease of use, and efficiency.

![[Pasted image 20260827141054.png|314]]
tools must be 1. useful, 2. usable, and 3. desirable
# reducing the cognitive load
A good rule of thumb is to ask yourself: does this change reduce the cognitive load for the whole group as a whole (in the long run). 



# iterative design
Frequent, small iterations reduce the need for significant course corrections.

analyze the situation → design 1+ focused improvements → evaluate impact on user experience

the goal of one iteration is to learn something out of it.![[Pasted image 20260827141154.png]]

- The typical steps of iterative design in user interfaces:
    1. Create an initial interface design
    2. Present the design to several test users
    3. Note any problems had by the test user
    4. Refine interface to account for/fix the problems
    5. Repeat steps 2-4 until user interface problems are resolved
# learning from mistakes
postmortems, decision logs, etc. help identify repeating patterns over time.

# responsibility
> "the minute you encourage someone to use a piece of technology, you are inherently responsible for it" (reid hoffman, masters of scale)
# common reasons why users didn’t read the manual
- not knowing know it exists
- it doesn’t exist
- it’s difficult to find / navigate to
- it’s hard to understand
- it contains a lot of irrelevant information to the user

# lowering the barrier to contribute
the lower the barrier is to extend a tool, the more people can help improve & customize it

# estimating return on investment
basic version: Time/energy saved each occurrence *x* Number of users *x* Frequency *x* Future benefits
Vs
Development time (including the time that users don’t have the fix) *+* Future maintenance & support time *+* time it takes to adopt & learn 

example: 5 minutes saved *x* 4 times a day *x* 35 users
  = 11.7 hours / day, or 29 days / month, or *350 days / year*

(Other factors like cognitive load and context switching are harder to quantify but relevant)

these calculations often end up looking like this:

![[Pasted image 20260827141326.png|296]]
Caveat: creative work of artists / human cognition can not be reduced to a single number, and oversimplifying any complex topic can have unintended consequences
# the hierarchy of mental loads
- High: cognitive tasks (thinking, remembering)
- Medium: visual processing
- Low: physical actions (clicking, typing)

More interactions are not inherently negative if they lower cognitive load.

# reducing distractions
context switching - around 9-23 minutes (or more) can be lost each time you switch your attention from one topic to another before regaining full focus.

it’s often possible to still “feel” like you’re doing something useful, but in the end get nothing done.

severity depends on the type of distraction (and [contexts you’re switching between](https://ics.uci.edu/~gmark/chi08-mark.pdf)), for example making art → figuring out why a tool doesn’t work is quite high.


# Features vs goals
More features do not always make a better tool, adding more features increases complexity exponentially.

![[Pasted image 20260827141400.png]]
every additional feature needs to be developed & maintained, and istime away from other things

# Finding the right balance
maintaining balance between user, developer, and stakeholder requirements.
![[Pasted image 20260827141415.png]]

# user testing
Testing early and frequently reduces the likelihood of developing unused or irrelevant features.

# “we’re evaluating the tool, not the user”
^ important to say out loud before user testing  
users often blame themselves for not understanding how to use a tool.
# user testing - analogy to code reviews
Without review, user interfaces and documentation can become difficult to understand.

Reviewing ensures clarity for others.

> “if the user can’t find it, it doesn’t exist”

# prototypes
validating early without writing complex code or setting a new workflow into stone.

- paper prototypes
	- [what are wizard of oz prototypes?](https://www.interaction-design.org/literature/topics/wizard-of-oz-prototypes)
	- [using paper prototyping as a tool for participatory design](https://www.paulolyslager.com/paper-prototyping-tool-participatory-design-research/)
- interactive prototypes
	- [protopie](https://www.protopie.io/download)
- vibe coding
	- perfect for building scrappy prototypes just to see whether the idea itself is useful and worth doing properly later

# the importance of watching users work
_**what people say they do vs what they actually do is often quite different**_

metrics and focus groups don’t replace actually sitting down with the users watching them work.

it’s totally normal that during development of a tool we become blind to our own design in some way.

![[Pasted image 20260827141517.png|464]]
this is also totally normal, the reason to sit next to the user when they are testing the tool is to have the chance to ask them to explain why.

# Dogfooding
There's value in getting personally annoyed by annoying workflows.

Skipping this step leaves room for missing big fundamental problems in the design. There’s also often lots of stuff that people won’t mention / don’t realize could be easily fixed or automated entirely.

When replacing existing tools, using older tools provides a baseline for comparison.
# some best practices from the book “100 things designers should know about people”
    
Seeing
    - People believe that are grouped together belong together
    - Use simple shapes + familiar objects for icons
    - Cues that tell people what to do with an object
Remembering
    - Memory takes a lot of mental resources
    - Recognizing is easier than recalling
    - People remember only 4 at once
        - Split items into small chunks of 3-4
    - Repetition = remembering
    - Stress reduces short term memory
    - Context switching destroys memory
    - Visual memory > words (also works for presentations, people remember pictures better)
    - Biased questions mess up recall
Thinking
    - Use bite-sized chunks
    - People learn best from examples
Motivation
    - People tend to take the route of least cognitive effort
    - People will look for shortcuts if the shortcuts are easy
Feel
    - Stories & anecdotes > data
    - Look & feel = indicator of trust
Mistakes
    - People will always make mistakes
    - Stress = more mistakes

# user task flows
High-level task flows reveal dependencies and bottlenecks that may otherwise be too abstract to communicate

# flexibility
_“No single way of working, from where or when we work to how we communicate, is optimal for all of us. Implementing flexibility at the core of policies and practices can be a game changer for your teams’ efficiency.” ([blog post from ubisoft](https://news.ubisoft.com/en-us/article/4MdbqYqnJ4Mk2PGD5hjdYf/gdc-2023-unlocking-the-power-of-neurodiversity-in-game-development))_

# digging for the root cause
Initial feedback may represent symptoms rather than underlying causes.
- 5 whys


# ideas for improving feedback culture
when inviting feedback:
- make sure the feedback won’t get lost
- actually be prepared to listen
- follow up on feedback and explain the why, even if the answer is “we can’t do anything about it atm”
- make collected feedback easy to search/browse for everyone
- ask in advance if people have the bandwidth to give/receive feedback

give some idea of what useful feedback looks like in advance:
- that it often needs iteration to get to the root of the problem
- evaluating the severity (frequency & how many people it affects)

also:
- lower the treshold to share feedback:
	- one click record & share a problematic workflow
	- your own availability

# prioritization
sometimes need to choose to let some fires burn - it’s easy to get caught up with lots of small things and miss the one thing that really matters.

# Enabling people to make informed decisions
a guide that enables people to make informed decisions will often outlive any tool or complex process. a good guide can also complement and reduce the overall complexity needed.

a guide can also be about a generic topic that isn’t explained well enough elsewhere (like this page i guess)

# do one thing really well
a simple tool is easier to maintain

# increasing the level of ux maturity
(todo: maybe this could be its own page, and explain the benefits & applications)

# getting buy-in
We end up adopting inefficient workflows or forget to update them when they stop serving their purpose. In the land of tech art the technology side of things is often easy, it's getting everyone onboard to change the way they're used to working that's the real challenge.

One approach would be to spend months behind the scenes developing a tool or planning a change, and then presenting it to the team as "here you have it, we're going to use this whether you want it or not".

The other approach, which has worked quite well for tech art improvements, is to present ideas as deliberately scrappy looking prototypes. Most of them will be discarded, but when you find something valuable to improve, people will tell you about it. 



# links / resources
ux resources
    [10 usability heuristics for user interface design](https://www.nngroup.com/articles/ten-usability-heuristics/)  
    _useful checklist_

ux + neurodiversity 
    (most of these are just good ux practices anyway)
    [neurodiversity and ux - essential resources for cognitive accessibility](https://stephaniewalter.design/blog/neurodiversity-and-ux-essential-resources-for-cognitive-accessibility/)
    [how to design for neurodiversity - inclusive content ant ux](https://www.interaction-design.org/master-classes/how-to-design-for-neurodiversity-inclusive-content-and-ux)
    [Beyond Compliance_A User-Autonomy Framework for Inclusive and Customizable Web Accessibility.pdf](attachment:704d9525-a9b2-4cc3-a82e-32e9fd7eb5bc:Beyond_Compliance_A_User-Autonomy_Framework_for_Inclusive_and_Customizable_Web_Accessibility.pdf)
    
design methodologies
    [Iterative design](https://en.wikipedia.org/wiki/Iterative_design)
    [User-centered design](https://en.wikipedia.org/wiki/User-centered_design)
    [Participatory design](https://en.wikipedia.org/wiki/Participatory_design)
    
writing user manuals
    [https://www.techsmith.com/blog/user-documentation/](https://www.techsmith.com/blog/user-documentation/)
    [https://refactoringenglish.com/chapters/rules-for-software-tutorials/](https://refactoringenglish.com/chapters/rules-for-software-tutorials/)
    [https://www.youtube.com/watch?v=vtIzMaLkCaM](https://www.youtube.com/watch?v=vtIzMaLkCaM)
    [https://en.wikipedia.org/wiki/Cognitive_dimensions_of_notations](https://en.wikipedia.org/wiki/Cognitive_dimensions_of_notations)
    [manufacturer’s guide to developing consumer product instructions](https://www.cpsc.gov/s3fs-public/pdfs/guide.pdf) (some good instructions / checklists for writing guides)
    [https://teachtogether.tech/en/index.html#](https://teachtogether.tech/en/index.html#)
    
some relevant cognitive biases: [[how to question your own thinking]]

also:
[https://growth.design/psychology](https://growth.design/psychology)