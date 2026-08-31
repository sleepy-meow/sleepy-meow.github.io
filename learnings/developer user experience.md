> [!WARNING] this page is wip

*applying pipeline tech art ux learnings*

Most of us understand the value of ux in the products we build. But an often overlooked aspect is how those same principles can be applied to finding optimal ways of working and internal tooling.

> [!TIP] [Designing the User Experience of Game Development Tools](https://uxofgametools.com/) (the best book ever on this topic, very condensed and practical advice)

> [!TIP] Reid Hoffman - Masters of Scale (the book, not the podcast)
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


# getting buy-in
We end up adopting inefficient workflows or forget to update them when they stop serving their purpose. In the land of tech art the technology side of things is often easy, it's getting everyone onboard to change the way they're used to working that's the real challenge.

One approach would be to spend months behind the scenes developing a tool or planning a change, and then presenting it to the team as "here you have it, we're going to use this whether you want it or not".

The other approach, which has worked quite well for tech art improvements, is to present ideas as deliberately scrappy looking prototypes. Most of them will be discarded, but when you find something valuable to improve, people will tell you about it. 

%%
# communication

[wiios law](https://en.wikipedia.org/wiki/Wiio%27s_laws): "Communication usually fails, except by accident” - applies to user interfaces and guides, most of it is about understanding what the users need and making sure that the designs we create actually make sense to the users



By involving the people affected at an early stage, addressing their concerns, explaining the why, 
%%

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