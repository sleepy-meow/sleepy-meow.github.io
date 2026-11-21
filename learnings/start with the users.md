*a collection of bite sized tech art learnings*

> “You’ve got to start with the customer experience and work back toward the technology - not the other way around.” -Steve Jobs

> [!SUCCESS] Defining user experience
> User experience refers to how a user interacts with and operates a product, system, or service, including perceptions of utility, ease of use, and efficiency.
> ![[Pasted image 20260827141054.png|314]]


> [!SUCCESS] reducing the cognitive load
> A good rule of thumb is to ask yourself: does this change reduce the cognitive load for the whole group as a whole (in the long run). 

> [!SUCCESS] iterative design
> Frequent, small iterations reduce the need for significant course corrections.
> 
> analyze the situation → design 1+ focused improvements → evaluate impact on user experience
> 
> the goal of one iteration is to learn something out of it.![[Pasted image 20260827141154.png]]
> 
> The typical steps of iterative design in user interfaces:
 >    1. Create an initial interface design
 >    2. Present the design to several test users
 >    3. Note any problems had by the test user
 >    4. Refine interface to account for/fix the problems
>     1. Repeat steps 2-4 until user interface problems are resolved

> [!SUCCESS]  learning from mistakes
> postmortems, decision logs, etc. help identify repeating patterns over time.

> "the minute you encourage someone to use a piece of technology, you are inherently responsible for it" (reid hoffman, masters of scale)

> [!SUCCESS] common reasons why users didn’t read the manual
> - not knowing know it exists
> - it doesn’t exist
> - it’s difficult to find / navigate to
> - it’s hard to understand
> - it contains a lot of irrelevant information to the user

> [!SUCCESS]  lowering the barrier to contribute
> the lower the barrier is to extend a tool, the more people can help improve & customize it

> [!SUCCESS]  estimating return on investment
> basic version: Time/energy saved each occurrence *x* Number of users *x* Frequency *x* Future benefits
> Vs
> Development time (including the time that users don’t have the fix) *+* Future maintenance & support time *+* time it takes to adopt & learn 
> 
> example: 5 minutes saved *x* 4 times a day *x* 35 users
>   = 11.7 hours / day, or 29 days / month, or *350 days / year*
> 
> (Other factors like cognitive load and context switching are harder to quantify but relevant)
> 
> these calculations often end up looking like this:
> 
>  ![[Pasted image 20260827141326.png|296]]
> Caveat: creative work of artists / human cognition can not be reduced to a single number, and oversimplifying any complex topic can have unintended consequences

> [!SUCCESS] the hierarchy of mental loads
> - High: cognitive tasks (thinking, remembering)
> - Medium: visual processing
> - Low: physical actions (clicking, typing)
> 
> More interactions are not inherently negative if they lower cognitive load.

> [!SUCCESS] reducing distractions
> context switching - around 9-23 minutes (or more) can be lost each time you switch your attention from one topic to another before regaining full focus.
> 
> it’s often possible to still “feel” like you’re doing something useful, but in the end get nothing done.
> 
> severity depends on the type of distraction (and [contexts you’re switching between](https://ics.uci.edu/~gmark/chi08-mark.pdf)), for example making art → figuring out why a tool doesn’t work is quite high.


> [!SUCCESS] Features vs goals
> More features do not always make a better tool, adding more features increases complexity exponentially.
> 
> ![[Pasted image 20260827141400.png]]
> every additional feature needs to be developed & maintained, and istime away from other things

> [!SUCCESS] Finding the right balance
> maintaining balance between user, developer, and stakeholder requirements.
> ![[Pasted image 20260827141415.png]]

> [!SUCCESS] user testing
> Testing early and frequently reduces the likelihood of developing unused or irrelevant features.

> [!SUCCESS] “we’re evaluating the tool, not the user”
> ^ important to say out loud before user testing  
> users often blame themselves for not understanding how to use a tool.

> [!SUCCESS] user testing & analogy to code reviews
> Without review, user interfaces and documentation can become difficult to understand.
> 
> Reviewing ensures clarity for others.

> “if the user can’t find it, it doesn’t exist”

> [!SUCCESS] prototypes
> validating early without writing complex code or setting a new workflow into stone.
> 
> - paper prototypes
	> - [what are wizard of oz prototypes?](https://www.interaction-design.org/literature/topics/wizard-of-oz-prototypes)
	> - [using paper prototyping as a tool for participatory design](https://www.paulolyslager.com/paper-prototyping-tool-participatory-design-research/)
> - interactive prototypes
> 	- [protopie](https://www.protopie.io/download)
> - vibe coding
> 	- great for building scrappy prototypes simply to answer the question "would this idea be useful?"

> [!SUCCESS] the importance of watching users work
> _**what people say they do vs what they actually do is often quite different**_
> 
> metrics and focus groups don’t replace actually sitting down with the users watching them work.
> 
> it’s totally normal that during development of a tool we become blind to our own design in some way.
> 
> ![[Pasted image 20260827141517.png|464]]
> this is also totally normal, the reason to sit next to the user when they are testing the tool is to have the chance to ask them to explain why.

> [!SUCCESS] Dogfooding
> There's value in getting personally annoyed by annoying workflows.
> 
> Skipping this step leaves room for missing big fundamental problems in the design. There’s also often lots of stuff that people won’t mention / don’t realize could be easily fixed or automated entirely.
> 
> When replacing existing tools, using older tools provides a baseline for comparison.

> _“No single way of working, from where or when we work to how we communicate, is optimal for all of us. Implementing flexibility at the core of policies and practices can be a game changer for your teams’ efficiency.” ([blog post from ubisoft](https://news.ubisoft.com/en-us/article/4MdbqYqnJ4Mk2PGD5hjdYf/gdc-2023-unlocking-the-power-of-neurodiversity-in-game-development))_

> [!SUCCESS] digging for the root cause
> Initial feedback may represent symptoms rather than underlying causes.
> - 5 whys

> [!SUCCESS] prioritization
> sometimes need to choose to let some fires burn - it’s easy to get caught up with lots of small things and miss the one thing that really matters.

> [!SUCCESS] Enabling people to make informed decisions
> a guide that enables people to make informed decisions will often outlive any tool or complex process. a good guide can also complement and reduce the overall complexity needed.
> 
> a guide can also be about a generic topic that isn’t explained well enough elsewhere (like this page i guess)

> [!SUCCESS] do one thing really well
> a simple tool is easier to maintain


> [!SUCCESS] getting buy-in
> We end up adopting inefficient workflows or forget to update them when they stop serving their purpose. In the land of tech art the technology side of things is often easy, it's getting everyone onboard to change the way they're used to working that's the real challenge.
>
> One approach would be to spend months behind the scenes developing a tool or planning a change, and then presenting it to the team as "here you have it, we're going to use this whether you want it or not".
> 
> The other approach, which has worked quite well for tech art improvements, is to present ideas as deliberately scrappy looking prototypes. Most of them will be discarded, but when you find something valuable to improve, people will tell you about it. 

### Resources
> [!TIP] Reid Hoffman - Masters of Scale

> [!TIP]  Designing the User Experience of Game Development Tools - David Lightbown. (A practical approach to observing how people work, understanding their goals, and testing improvements to their tools.)

> [!EXAMPLE] [10 usability heuristics for user interface design](https://www.nngroup.com/articles/ten-usability-heuristics/)  

> [!EXAMPLE] [https://growth.design/psychology](https://growth.design/psychology)
