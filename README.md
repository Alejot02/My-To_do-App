I created a To-Do app Using Django and HTMX, you'll be able to add, update, filter and delete your tasks without having to reload your page even once!

-----------------------MY EXPERIENCE WITH THIS PROJECT:-----------------------

Note that this is the first project I did on my own. I proactively avoided tutorials, but instead searched through online documentation anytime I had a specific question. The best example was when I wanted to use the information of an object to pre-populate my html form. I remember trying to pre-populate the "date" field using syntax like "{{form.deadline.value}}" without knowing that the input type datetime expects data to arrive in a certain format. Turns out the correct way to do it was by having the "value" of the input be: {{form.deadline.value|date:'Y-m-d\Th:m:s'}}.

Either way, I wanted to share this with you since I loved the process of creating this simple webapp. I loved how even when I "knew" what I wanted to do, I needed to double check a bunch of times that I truly knew what I wanted to do. Let me give you an example.

You'll notice that when you "Check" a task, it's style changes to give you the feel that's been completed, right? There's a line going through the text. I achieved this using this bit of code:

.selector:has(.task-completed) ~ p{ text-decoration: line-through; text-decoration-color:#515050; }

Even though this is how the end product has, I wanted a line through the whole element, not just the paragraph. You have no clue how much I battled trying to get that to work, to just not use it in the final product XD, thank god I came across the "::after" pseudo-element, I don't think I would've achieved it without it. If you want to see what I mean, you can just comment the previous bit of code, and un-comment the below piece of code on your end:

.selector:has(.task-completed)::after{ position: absolute; z-index: 1; left: 38px; height: 2px; background: #4b4c4d; content: ""; width: 551px; top: 1.2rem; display: block; transition: .2s; }

Overall, I know there's a bunch of good practices to learn, and without a doubt I could've spent more time making this more responsive. However, I've been watching tutorials for the past 3 months, and I thought I'd just sit down and create something on my own, and get it to work.

I consider this one of my first steps to landing job as a Software Developer!
