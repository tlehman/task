# task
Improve your estimation skills by practicing calibrated estimates of the time it takes to complete a task.

What is calibration? It is a way of determining how good an estimator is at putting
[prior probabilities](https://en.wikipedia.org/wiki/Prior_probability) on events.
For example, if Alice the meteorologist says that _"there's a 90% chance of 2cm to 5cm of rain tomorrow"_, and it doesn't rain the
next day, does that make Alice a bad estimator?

Suppose after 100 days, you counted up her weather predictions made with 90% confidence, if about 90 of those
predictions were correct, then Alice is a good estimator, that is an example of being calibrated.

This extends to any uncertain future event we might care about. In software engineering, there is a popular,
but incorrect and self-defeating belief that [software estimates are impossible](https://chrismm.com/blog/project-delays-why-software-estimates/)
and we should just accept we can't know anything about how long a task might take.

I reject this, and I intend to prove it using data.
The missing idea here is the probability and the range of values. The linked article hints at this, but doesn't explore it in any depth.

The `task` tool maintains a SQLite database of tasks, along with their predicted duration and CIs (confidence intervals). Then, as it accumulates
data, it can calculate how well calibrated you are. You can improve your calibration in your domain by using this information as feedback
and adjusting your future predictions. Because you have this feedback, you should gradually learn to make better estimates.

# How to use

Starting a task:

```
$ task start
Description of task: Create endpoint to allow logging off
estimated range of time to completion (90% CI): 20 - 30 minutes
task #3 created at 2018-01-04 12:38:28
```

Ending a task:
```
$ task end
end task #3? (y/N) y
task #3 ended at 2018-01-04 13:03:29 (25 minutes) correct!
For 90% CI you are currently 67% correct (2/3 correct),
consider widening intervals or breaking tasks down to improve this number
```

## Multi-tasking
If you can avoid it, you should. But if you have to, just pass the `id` of the task in as an argument to the `start` and `end` subcommands.

# Habit
Once this is a habit, and you start using the feedback from this tool, you should improve at estimating how long it takes you to complete tasks.
Doing this for smaller tasks is easier, but as you gain experience and become more calibrated, you should be able to start estimating larger tasks.
