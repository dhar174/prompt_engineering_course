# Module 1 Knowledge Check Quiz: LLM Internals & Prompt Anatomy

**Duration**: 10 minutes  
**Attempts**: Unlimited  
**Passing Score**: 80%  
**Feedback**: Immediate  

## Instructions

This quiz assesses your understanding of fundamental concepts from Module 1: LLM Internals & Prompt Anatomy. You may retake this quiz as many times as needed for learning. Focus on understanding the concepts rather than memorizing answers.

---

## Question 1: Tokenization Fundamentals (2 points)

**Which of the following statements about tokenization are correct?** (Select all that apply)

- [ ] a) Tokenization converts text into numerical representations for LLM processing
- [ ] b) Each token always represents exactly one word
- [ ] c) Tokenization affects API costs since pricing is often per token
- [ ] d) The same text will always produce the same number of tokens across different models
- [ ] e) Subword tokenization can split words into smaller meaningful units

**Correct Answers**: a, c, e

**Explanation**: Tokenization converts text to numerical tokens (a), affects API costs (c), and uses subword techniques (e). However, tokens don't always equal words (b is false), and different models may tokenize differently (d is false).

---

## Question 2: Context Window Impact (1 point)

**True or False: If your prompt exceeds the model's context window, the model will automatically compress the input to fit.**

- [ ] True
- [ ] False

**Correct Answer**: False

**Explanation**: When input exceeds the context window, the model typically truncates the input (removes text) rather than compressing it. This can result in loss of important information and degraded performance.

---

## Question 3: Temperature Parameter (1 point)

**A prompt engineer wants to generate creative story ideas and is willing to accept some inconsistency. Which temperature setting would be most appropriate?**

- [ ] a) 0.0
- [ ] b) 0.3
- [ ] c) 0.7
- [ ] d) 1.2

**Correct Answer**: c) 0.7

**Explanation**: Higher temperature values (like 0.7) increase creativity and randomness, which is ideal for brainstorming and creative tasks. 0.0 would be too deterministic, 0.3 too conservative, and 1.2 might be too chaotic for coherent ideas.

---

## Question 4: Prompt Role Structure (2 points)

**Match each prompt role with its typical function:**

**Roles:**
1. System prompt
2. User prompt
3. Assistant prompt

**Functions:**
a) Contains the user's question or request
b) Provides context and instructions for the AI's behavior
c) Shows an example of how the AI should respond

**Correct Matches:**
- System prompt → b) Provides context and instructions for the AI's behavior
- User prompt → a) Contains the user's question or request
- Assistant prompt → c) Shows an example of how the AI should respond

---

## Question 5: Output Control Strategies (2 points)

**Which of the following are effective strategies for controlling output length?** (Select all that apply)

- [ ] a) Setting the max_tokens parameter
- [ ] b) Including explicit word limits in the prompt ("Respond in exactly 50 words")
- [ ] c) Using higher temperature values
- [ ] d) Providing examples of desired output length
- [ ] e) Adjusting presence penalty

**Correct Answers**: a, b, d

**Explanation**: 
- max_tokens directly limits token count (a)
- Explicit instructions guide the model (b)
- Examples demonstrate desired length (d)
- Temperature affects creativity, not length (c is incorrect)
- Presence penalty reduces repetition, not length (e is incorrect)

---

## Question 6: Tone and Style Control (1 point)

**Which prompt modification would most effectively change the output from casual to formal tone?**

- [ ] a) Increase temperature to 0.9
- [ ] b) Add "Please respond in a professional, formal tone" to the prompt
- [ ] c) Decrease max_tokens to 50
- [ ] d) Add presence penalty of 0.5

**Correct Answer**: b) Add "Please respond in a professional, formal tone" to the prompt

**Explanation**: Direct instructions about tone and style are the most effective way to control output formality. The other options affect different aspects of generation.

---

## Question 7: Debugging Approach (2 points)

**You notice that your prompt consistently produces outputs that are too verbose and repetitive. What debugging steps should you take?** (Rank in order of priority)

1. Check for repetitive patterns in the prompt itself
2. Adjust decoding parameters (temperature, presence penalty)
3. Revise prompt instructions to be more specific about length
4. Try different example formats
5. Test with different models

**Suggested Order**: 1, 3, 2, 4, 5

**Explanation**: Start with the prompt itself (1), then add specific instructions (3), adjust parameters (2), modify examples (4), and finally test alternatives (5).

---

## Question 8: Divergent vs Convergent Thinking (1 point)

**Which prompt is designed for divergent thinking?**

- [ ] a) "Summarize this article in one sentence"
- [ ] b) "Generate 10 creative uses for a paperclip"
- [ ] c) "What is the capital of France?"
- [ ] d) "Choose the best solution from these three options"

**Correct Answer**: b) "Generate 10 creative uses for a paperclip"

**Explanation**: Divergent thinking involves generating multiple creative ideas or solutions. The other options focus on convergent thinking (narrowing down to one answer).

---

## Question 9: Reading Level Control (1 point)

**True or False: To control reading level, you should only adjust the vocabulary complexity in your prompt.**

- [ ] True
- [ ] False

**Correct Answer**: False

**Explanation**: Reading level control involves multiple factors: vocabulary complexity, sentence length, concept complexity, and explicit instructions about target audience (e.g., "explain to a 5th grader").

---

## Question 10: Uncertainty Calibration (2 points)

**How can you help a model express uncertainty about its responses?** (Select all that apply)

- [ ] a) Ask the model to rate its confidence on a scale
- [ ] b) Request multiple alternative answers
- [ ] c) Use higher temperature settings
- [ ] d) Include phrases like "I'm not sure" in the prompt
- [ ] e) Ask the model to explain what it doesn't know

**Correct Answers**: a, b, e

**Explanation**: Uncertainty calibration involves explicitly asking for confidence ratings (a), alternatives (b), and acknowledgment of limitations (e). Higher temperature doesn't calibrate uncertainty (c), and including uncertainty in prompts doesn't teach the model to express it appropriately (d).

---

## Quiz Summary

**Total Points**: 15  
**Passing Score**: 12/15 (80%)  
**Time Limit**: 10 minutes  

### Learning Objectives Assessed:
- LO.1.1: Define and explain prompt engineering concepts
- LO.1.2: Analyze tokenization and context window constraints
- LO.1.3: Apply role structure and output controls
- LO.1.4: Control tone, style, and reading level
- LO.1.5: Debug prompt failures and calibrate uncertainty

### Study Resources:
- Day 1 lesson materials
- Tokenization playground notebook
- Prompt anatomy template
- Decoding parameters guide

### Next Steps:
After passing this quiz, you're ready to move on to Module 2: Foundational Prompt Patterns & Personas. If you need additional practice, review the specific topics where you lost points and try the quiz again.

---

## Implementation Notes

### For Instructors:
- This quiz uses a mix of question types to assess different learning levels
- Immediate feedback helps with learning retention
- Unlimited attempts encourage mastery learning
- Analytics can identify common misconceptions

### For Students:
- Take time to read explanations for both correct and incorrect answers
- Focus on understanding concepts rather than memorizing answers
- Use this quiz as a learning tool, not just an assessment
- Seek help if you consistently struggle with specific topics

### Technical Implementation:
- Can be implemented in Jupyter notebooks with ipywidgets
- Supports automated grading with detailed feedback
- Accessibility features included for screen readers
- Mobile-friendly design for flexible learning