*small snippets of tech art learnings*

Main sources:
> [!TIP] [Designing the User Experience of Game Development Tools](https://uxofgametools.com/) (the best book ever on this topic, very condensed and practical advice)

> [!TIP] Reid Hoffman - Masters of Scale (the book, not the podcast)

> “You’ve got to start with the customer experience and work back toward the technology - not the other way around.” -Steve Jobs


# Defining user experience

User experience refers to how a user interacts with and operates a product, system, or service, including perceptions of utility, ease of use, and efficiency.

![[Pasted image 20260827141054.png|314]]
tools must be 1. useful, 2. usable, and 3. desirable

# start with the users

Developing tools without first understanding their users can result in incorrect assumptions about needs and workflows.

When individuals contribute features based on differing assumptions, the resulting tool may become complex and difficult to learn.

# designing for flow state

_“The flow state is an optimal state of intrinsic motivation, where the person is fully immersed in what they are doing.“
_“The flow state amplifies performance, accelerates learning, and heightens creativity.”__

**Conditions:**
- knowing what to do
- knowing how to do it
- knowing how well you are doing
- knowing where to go (navigation)
- room for risk (it’s ok fail & experiment)
- confidence in skills & challenges
- freedom from distractions

![[Pasted image 20260827141138.png|315]]



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

## common reasons why users didn’t read the manual

- not knowing know it exists
- it doesn’t exist
- it’s difficult to find / navigate to
- it’s hard to understand
- it contains a lot of irrelevant information to the user

# lowering the barrier to help improve things

the lower the barrier is to extend a tool, the more people can help improve & customize it

# **estimating return on investment**

- basic version
    - Time/energy saved each occurrence
    - Number of users
    - Frequency
    - Future benefits
    Vs
    - Development time (including the time that users don’t have the fix)
    - Future maintenance & support time
- example:
    5 minutes saved
    4 times a day
    35 users
    = 11.7 hours / day
    = 29 days / month
    = 350 days / year

(Other factors like cognitive load and context switching are harder to quantify but relevant)

these calculations often end up looking like this:

![[Pasted image 20260827141326.png|296]]

*_creative work of artists / human cognition can not be reduced to a single number, and oversimplifying any complex topic can have unintended consequences (adding disclaimers, context, and a clear suggestion of what to do with this information can help)._
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

tool developers might also blame themselves for users not understanding how to use a tool, but it’s totally normal for ux issues to come up (in the end ux is more about understanding the users & validating designs, than anything else)

# user testing - analogy to code reviews

Without review, user interfaces and documentation can become difficult to understand.

Reviewing ensures clarity for others.

> “if the user can’t find it, it doesn’t exist”

# paper prototypes

validating early without writing complex code

paper prototype, using the wizard of oz technique

[what are wizard of oz prototypes?](https://www.interaction-design.org/literature/topics/wizard-of-oz-prototypes)

[using paper prototyping as a tool for participatory design](https://www.paulolyslager.com/paper-prototyping-tool-participatory-design-research/)

# interactive prototypes

for example: [protopie](https://www.protopie.io/download)

# _the importance of watching users work_

_**what people say they do vs what they actually do is often quite different**_

metrics and focus groups don’t replace actually sitting down with the users watching them work

it’s totally normal that during development of a tool we become blind to our own design in some way.

![[Pasted image 20260827141517.png|464]]
this is also totally normal, the reason to sit next to the user when they are testing the tool is to have the chance to ask them to explain why.

# Dogfooding (using internally developed tools)

skipping this step leaves room for missing big fundamental problems in the design. there’s also lots of stuff that users won’t mention / don’t realize could be fixed with 3 lines of code or just automated entirely.

_(how nice the programmer created assets look visually is also not relevant, but it’s important for it to be a real asset made from start to finish.)_

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
    - Visual memory > words
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
High-level task flows reveal dependencies and bottlenecks in asset creation and iteration.

# flexibility
_“No single way of working, from where or when we work to how we communicate, is optimal for all of us. Implementing flexibility at the core of policies and practices can be a game changer for your teams’ efficiency.” ([blog post from ubisoft](https://news.ubisoft.com/en-us/article/4MdbqYqnJ4Mk2PGD5hjdYf/gdc-2023-unlocking-the-power-of-neurodiversity-in-game-development))_

# user feedback
Initial feedback may represent symptoms rather than underlying causes.

## ideas for improving feedback culture
when inviting feedback:
- making sure the feedback won’t get lost
- actually being prepared to listen & trying to understand
- following up on the feedback - even if the answer is “we can’t do anything about it atm” or some kind of explanation
- collecting feedback & issue tickets easy to search/browse for everyone
- asking if people actually have the bandwidth to give/receive feedback

sharing some ballpark idea of what useful feedback looks like in advance:
- iteration on the feedback needed, to confirm it’s actually correct
- evaluating the severity (frequency & how many users does it affect)

also:
- making it as easy as possible to share feedback: one click record & share a problematic workflow could help & is very easy to make

# prioritization
sometimes need to choose to let some fires burn - it’s easy to get caught up with lots of small things and miss the one thing that really matters.

# Enabling people to make informed decisions
a guide that enables people to make informed decisions will often outlive any tool. a good guide can complement a tool and reduce the overall complexity needed.

a guide can also be about a generic topic that isn’t explained well enough elsewhere (like this page i guess)

# do one thing really well
a simple tool is easier to maintain

[wiios law](https://en.wikipedia.org/wiki/Wiio%27s_laws): "Communication usually fails, except by accident” - applies to user interfaces and guides, most of it is about understanding what the users need and making sure that the designs we create actually make sense to the users

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
    
some relevant cognitive biases
[https://en.wikipedia.org/wiki/Curse_of_knowledge](https://en.wikipedia.org/wiki/Curse_of_knowledge)
_“…occurs when a person who has specialized knowledge assumes that others share in that knowledge.”_

[https://en.wikipedia.org/wiki/Default_effect](https://en.wikipedia.org/wiki/Default_effect)
_“the tendency to to generally accept the default option”_
    
[https://en.wikipedia.org/wiki/Information_overload](https://en.wikipedia.org/wiki/Information_overload)
_“the difficulty in understanding an issue and effectively making decisions when one has too much information about it, and is generally associated with the excessive quantity of daily information.”_
    
[https://en.wikipedia.org/wiki/Response_bias](https://en.wikipedia.org/wiki/Response_bias) (for surveys)
_“general term for a wide range of tendencies for participants to respond inaccurately or falsely to questions, and can have a large impact on the validity of questionnaires or surveys.”_

also:
[https://growth.design/psychology](https://growth.design/psychology)