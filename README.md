# Speech Recognition
There are four scripts that can convert audio to text. One of them is written with Google API and the others are written with different sizes of Whisper API. !! I am writing this article based on I gained experience while I was doing this project. 
How to run the scripts and what you need to install before running is explained below.

## Google API

It is one of the APIs used to convert audio files to text. In order to use this API, the “SpeechRecognition” library must be installed. This API cannot understand some audio recordings. 
In voice recordings that it cannot understand, exception error (UnknownValueError) is written instead of text. (Free version used)

## Whisper API

This API is more comprehensive and has a higher accuracy rate than other APIs. This API has five sizes in itself. These are tiny, base, small, medium and large. Multi-language models are available in all sizes. This means that they can be used for more than one language at the same time. In addition, if desired, only an English model is available in other sizes except the large size. In other words, it can only be used for the English language. The advantage of this is that the accuracy rate is higher while the English model converts the English voice recording to text compared to the multi-language model. Coming to the differences between these sizes, the accuracy of the conversion process of each size is higher than the previous one. However, as the accuracy rate increases, the duration of the conversion process also increases. In other words, while the accuracy rate of the tiny model is the lowest, the accuracy rate of the large model is the highest. On the other hand, while the conversion process of the tiny model is the shortest, the conversion process of the large model is the longest.

In the table below, you can look at the number of parameters of the sizes, their approximate speed rates and the VRAM they use.
![image](https://github.com/brkygn7/SpeechRecognition/assets/150448786/8c1d1b77-20ba-4b93-8dd6-e321dcb4083d)

To get more detailed information about [Whisper API](https://github.com/openai/whisper)

## Bleu Score
BLEU is a metric used especially in the field of natural language processing and is designed to evaluate the quality of text translations. BLEU is one of a set of metrics used to evaluate translation quality. BLEU measures the similarity of words in a sentence, not the meaning of the sentence.

## How to Run
- Audio files must be in a folder and there must not be anything else (folder etc.) in that folder except wav files.
- It is sufficient to write the folder path. While you write the path of the folder, it must be written without the "/" at the end.
- When converting audio recordings to text, all punctuation marks will be removed and all letters will be recorded in lowercase.
- When the scripts are finished running, the results will be available in an Excel file in the relevant location.

## What you need to install before running
- pip install --upgrade numba or conda update numba
- pip install pandas
- pip install openpyxl
- pip install -U openai-whisper (for the Whisper API)
- pip install whisper (for the Whisper API)
- pip install SpeechRecognition (for the Google API)
