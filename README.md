# GENERATIVE-TEXT-MODEL

COMPANY : CODTECH IT SOLUTIONS

NAME : LEONA MENDES

INTERN ID : CT04DR1252

DOMAIN NAME : ARTIFICIAL INTELLIGENCE

DURATION : 4 WEEKS 

MENTOR : NEELA SANTOSH


# TASK 4 — GENERATIVE-TEXT-MODEL

The fourth task was focused on generative text modeling, where the main aim was to build a system that can automatically generate meaningful and coherent text based on any topic the user provides. For this task, you implemented a text generator using the popular GPT-2 model from the Hugging Face Transformers library. GPT-2 is a large pre-trained language model designed by OpenAI, known for its ability to understand language patterns and produce fluent and human-like sentences. Your script begins by importing the necessary tools from the transformers package, specifically the pipeline function and the set_seed utility. The pipeline function makes it incredibly simple to load a pre-trained model and set up a fully working text generation system in just one line of code. By specifying "text-generation" as the task and "gpt2" as the model, the pipeline initializes GPT-2 and loads all its learned language capabilities so that it can generate high-quality outputs without needing additional training.

After loading the model, your program takes an input prompt from the user. This prompt acts as the seed idea or starting sentence for the AI to build upon. Because GPT-2 generates text by predicting one word at a time based on the previous words, the initial prompt influences the flow, tone, and meaning of the generated paragraph. Next, the script sets a random seed using set_seed(42) to ensure that the output remains consistent every time the code is run with the same prompt. This is important because generative models often produce slightly different results on each run. Setting the seed ensures reproducibility, especially useful when experimenting or demonstrating how the model behaves.

The core generation step happens inside the generator() function call. Here, you specify parameters that control how the text is produced. The max_length=150 parameter ensures that the generated text remains within a reasonable size, making it similar to a small paragraph. The num_return_sequences=1 tells the model to produce only one output rather than multiple variations. You also used temperature=0.8, a value that balances creativity and coherence. Lower temperatures make outputs more predictable and factual, while higher temperatures increase randomness. A temperature of 0.8 helps produce text that is imaginative without becoming nonsensical. Additionally, top_p=0.9 enables nucleus sampling, a technique that restricts the model's predictions to the most probable next words, ensuring more natural and logical sentence flow.

Once the text is generated, the script prints the result clearly on the screen under the label “Generated Text.” The user sees the extended paragraph created by GPT-2 based entirely on their chosen topic. This task demonstrates how generative AI models can be applied to a wide range of practical scenarios. For instance, such systems can be used for creative writing, idea generation, storytelling, content drafting, developing chatbots, generating product descriptions, academic assistance, and even brainstorming new concepts. Industries like marketing, entertainment, journalism, and education frequently use text generation tools to automate writing tasks and speed up content creation. Through this task, you not only explored how GPT-2 works but also gained hands-on experience in using powerful language models to create dynamic, coherent text with very minimal effort.

# OUTPUT 

