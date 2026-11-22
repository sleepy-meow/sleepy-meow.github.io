Postmortems are a powerful way to learn from mistakes. They are commonly used in lines of work where catastrophic failures have immediate and painful consequences, for example devops being woken up in the middle of the night, or in aviation where failure can lead to a big explosion. 

The biggest benefits do not necessarily come so much from individual reports, but when they accumulate over time it allows seeing repeating patterns.
# short version

- What happened  
- Why did it happen (digging for the root cause)  
- How did you fix it?  
- Was it a permanent fix or a temporary one
- How can we detect this earlier in the future if it happens again  
- How can we prevent this from ever happening again


# long version

- leadup
	- list sequence of events that led to the incident
- fault
	- describe how the change was implemented didn't work as expected. if possible, include relevant data visualizations
- impact
	- describe how internal and external users were impacted during the incident. include how many support cases were raised
- detection
	- report when the team detected the incident and how they knew it was happening. describe how the team could've improved the time to detection
- response
	- report who responded to the incident and describe what they did at what times. include any delays or obstacles to responding
- recovery
	- report how the user impact was mitigated and when the incident was deemed resolved. describe how the team could've improved time to mitigation
- timeline
	- detail the incident timeline (using utc) include lead-up events, post-impact event, and any decisions or changes made
- five whys root cause identification
	- run a 5 whys analysis https://en.wikipedia.org/wiki/Five_whys to understand the true causes of the incident
- blameless root cause
	- note the final root cause and describe what needs to change without placing blame to prevent this class of incident recurring
- backlog check
	- review the engineering backlog to find out if there was unplanned work that could've prevented the incident or reduced its impact
- related incidents
	- check if any past incidents could've had the same root cause. note what mitigation was attempted in those incidents and ask why this incident occurred aain
- lessons learned
	- describe what you learned, what went well, and how you can improve
- follow-up tasks
	- list the jira issues created to prevent this class of incident in the future. note who is responsible, when they have to complete the work, and where that work is being tracked.