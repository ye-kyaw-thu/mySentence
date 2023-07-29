# mySentence
Corpus and models for Burmese (Myanmar language) Sentence Segmentation

[README file in Myanmar language](): 

- [Introduction](#Introduction)
- [License Information](#License-Information)
- [Version Information](#Version-Information)
- [Corpus Development](#Corpus-Development)
  - [Corpus Information](#Corpus-Information)
  - [Word Segmentation](#Word-Segmentation)
  - [Corpus Annotation](#Corpus-Annotation)
  - [Data Preparation](#Data-Preparation)
- Experiments
  - [JIIST Experiments](./ver1.0/jiist-experiments)
  - [CITA Experiments](./ver1.0/cita-experiments)
- [Contributors](#Contributors)
- [Publications](#Publications)
  - [Citations](#Citations)
  - [Workshop Presentation](#Workshop-Presentation)

## Introduction

Sentence segmentation can be defined as the task of dividing text into sentences. These sentences are independent units consisting of grammatically linked words. In formal Burmese (Myanmar language), sentences are grammatically structured and typically end with the "။" pote-ma symbol. However, informal language, which is more commonly used in daily conversations due to its natural flow, does not always follow predefined rules for ending sentences, making it challenging for machines to identify sentence boundaries. Applications rooted in conversation, such as Automatic Speech Recognition (ASR), Speech Synthesis or Text-to-Speech (TTS), and chatbots, need to determine the end of sentences to optimize their performance. In this corpus, we have tagged each token of the sentences and paragraphs from start to finish.

## License Information
Creative Commons Attribution-NonCommercial-Share Alike 4.0 International (CC BY-NC-SA 4.0) License.  
[[Detail Information]](https://creativecommons.org/licenses/by-nc-sa/4.0/)  

## Version Information
**Version 1.0 Release Date:** 30 July 2023  

## Corpus Development

### Corpus Information
The resources used to collect Burmese sentences and paragraphs for constructing the 'mySentence Corpus' for sentence segmentation are as follows:  

| Data Resources | sentence  | paragraph  |
|---|-: |-: |
| [myPOS ver3.0](https://github.com/ye-kyaw-thu/myPOS) | 40,191 | 2,917 |
| [Covid-19 Q&A](https://www3.nhk.or.jp/nhkworld/my/news/qa/coronavirus/) | 1,000 | 1,350 |
| [Shared By Louis Augustine Page](www.facebook.com/sharedbylouisaugustine) | 547 | 1,885 |
| [Maung Zi's Tales Page](www.facebook.com/MaungZiTales) | 2,516 | 581 |
| [Wikipedia](https://my.wikipedia.org/wiki/%E1%80%97%E1%80%9F%E1%80%AD%E1%80%AF%E1%80%85%E1%80%AC%E1%80%99%E1%80%BB%E1%80%80%E1%80%BA%E1%80%94%E1%80%BE%E1%80%AC) | 2,780 | 1,060 |
| Others | 93 | 672 |
| **Total** | **47,127** | **8,465** |

### Word Segmentation

In the Myanmar language, spaces are used only to segment phrases for easier reading. There are no clear rules for using spaces in the Myanmar language.
<br /> <br />
We used the [myWord](https://github.com/ye-kyaw-thu/myWord/) word segmentation tool to segment our manually collected data into words. Afterward, we manually reviewed the word segmentation results. The segmentation rules we applied were proposed by Ye Kyaw Thu et al. in the [myPOS](https://github.com/ye-kyaw-thu/myPOS) corpus.

### Corpus Annotation

After word segmentation, we annotated the sequences of words in the corpus, tagging each token within a sentence with one of four tags: B (Begin), O (Other), N (Next), and E (End). <br />
<br />
If a sequence contains more than two 'E' tags, it is considered a paragraph.
<br />
The tagged example of a Burmese sentence, (I get bored.), is shown below: <br />
Untagged sentence: ကျွန်တော် ပျင်း လာ ပြီ <br />
Tagged sentence : ကျွန်တော်/B ပျင်း/N လာ/N ပြီ/E <br />
<br />
The tagged example of a Burmese paragraph, (I am sorry. I like drama films more.), is shown below:  
Untagged paragraph: တောင်းပန် ပါ တယ် ကျွန်တော် က အချစ် ကား ပို ကြိုက် တယ် <br />
Tagged paragraph: တောင်းပန်/B ပါ/N တယ်/E ကျွန်တော်/B က/O အချစ်/O ကား/N ပို/N ကြိုက်/N တယ်/E <br />

### Dataset Preparation

We prepared two types of data: one containing only sentences and the other containing both sentences and paragraphs. We then split both datasets into training, development, and test data as follows:  

```
$ wc ./data/data-sent/sent_tagged/*
    4712    63622  1046667 test.tagged
   40000   543541  8955710 train.tagged
    2414    32315   531166 valid.tagged
   47126   639478 10533543 total
   
$ wc ./data/data-sent+para/sent+para_tagged/*
    5512    96632  1573446 test.tagged
   47002   834243 13612719 train.tagged
    3079    61782  1001138 valid.tagged
   55593   992657 16187303 total
```

### Dataset format example

```
$ head -5 ./data/data-sent/sent_tagged/train.tagged 
ဘာ/B ရယ်/O လို့/O တိတိကျကျ/O ထောက်မပြ/O နိုင်/O ပေမဲ့/O ပြဿနာ/O တစ်/O ခု/O ခု/O ရှိ/O တယ်/N နဲ့/N တူ/N တယ်/E
လူ့/B အဖွဲ့အစည်း/O က/O ရှပ်ထွေး/O လာ/O တာ/O နဲ့/O အမျှ/O အရင်/O က/O မ/O ရှိ/O ခဲ့/O တဲ့/O လူမှုရေး/O ပြဿနာ/O တွေ/O ဖြစ်ပေါ်/N လာ/N ခဲ့/N တယ်/E
အခု/B အလုပ်/O လုပ်/N နေ/N ပါ/N တယ်/E
ကြည့်/B ရေစာ/O တွေ/O က/O အဲဒီ/O တစ်/O ခု/O နဲ့/N မ/N တူ/N ဘူး/E
ဘူမိ/B ရုပ်သွင်/O ပညာ/O သည်/O ကုန်းမြေသဏ္ဌာန်/O များ/O ကို/O လေ့လာ/O သော/N ပညာရပ်/N ဖြစ်/N သည်/E
```

We also prepared data in the CRF format for experiments using the CRF++ and NCRF++ models.  

```
$ wc ./data/data-sent/sent_data_crf_format/*
   68334   127244  1051379 test.col
  583541  1087082  8995710 train.col
   34729    64630   533580 valid.col
  686604  1278956 10580669 total

$ wc ./data/data-sent+para/sent+para_data_crf_format/*
  102144   193264  1578958 test.col
  881245  1668486 13659721 train.col
   64861   123564  1004217 valid.col
 1048250  1985314 16242896 total
```

### CRF format example  

```
$ head -5 ./data/data-sent/sent_data_crf_format/train.col 
ဘာ B
ရယ် O
လို့ O
တိတိကျကျ O
ထောက်မပြ O
```

We prepared data in a parallel format for the neural machine translation approach.  

```
$ wc ./data/data-sent/sent_parallel/*
    4712    63622   919423 test.my
    4712    63622   919423 test.tg
   40000   543541  7868628 train.my
   40000   543541  1087082 train.tg
    2414    32315   466536 valid.my
    2414    32315    64630 valid.tg
   89540  1215334 10406299 total

$ wc ./data/data-sent+para/sent+para_parallel/*
    5512    96632  1380183 test.my
    5512    96632   193264 test.tg
   47002   834243 11944271 train.my
   47002   834243  1668486 train.tg
    3079    61782   877576 valid.my
    3079    61782   123564 valid.tg
  111186  1985314 16187344 total
```

```
$ head -2 ./data/data-sent/sent_parallel/train.my
ဘာ ရယ် လို့ တိတိကျကျ ထောက်မပြ နိုင် ပေမဲ့ ပြဿနာ တစ် ခု ခု ရှိ တယ် နဲ့ တူ တယ်
လူ့ အဖွဲ့အစည်း က ရှပ်ထွေး လာ တာ နဲ့ အမျှ အရင် က မ ရှိ ခဲ့ တဲ့ လူမှုရေး ပြဿနာ တွေ ဖြစ်ပေါ် လာ ခဲ့ တယ်

$ head -2 ./data/data-sent/sent_parallel/train.tg
B O O O O O O O O O O O N N N E
B O O O O O O O O O O O O O O O O N N N E
```

## Contributors
- [Ye Kyaw Thu](https://sites.google.com/site/yekyawthunlp/) (National Electronics and Computer Technology Center: NECTEC, Pathumthani, Thailand)
- [Thura Aung](https://sites.google.com/view/thura-aung/) (Language Understanding Laboratary: LU Lab., Myanmar)

## Publications
### Citations
If you wish to use the mySentence models or sentence segmentation data in your research, we would appreciate it if you could cite the following reference:
<!-- If you wish to use the mySentence models or sentence segmentation data in your research, we would appreciate it if you could cite the following two references:  -->

<!-- - Thura Aung, Ye Kyaw Thu, Zar Zar Hlaing, "mySentence: Sentence Segmentation for Myanmar language using Neural Machine Translation Approach" -->  

- Ye Kyaw Thu, Thura Aung, Thepchai Supnithi, "Neural Sequence Labeling based Sentence Segmentation for Myanmar Language"

### Workshop Presentation

Thura Aung, Ye Kyaw Thu, Zar Zar Hlaing, "mySentence: Sentence Segmentation for Myanmar language using Neural Machine Translation Methods", the 4th joint Workshop on NLP/AI R&D, November 5, 2022 at Chiang Mai, Thailand. [[workshop_link]](https://isai-nlp-aiot2022.aiat.or.th/workshop-on-nlp-ai-rd/)  

