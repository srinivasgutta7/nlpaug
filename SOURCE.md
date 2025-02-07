Source
======

Pre-trained Model File
----------------------
*  [word2vec](https://code.google.com/archive/p/word2vec/) (Google): Tomas Mikolov, Kai Chen, Greg Corrado and Jeffrey Dean released [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)
*  [GloVe](https://nlp.stanford.edu/projects/glove/) (Standford): Jeffrey Pennington, Richard Socher, and Christopher D. Manning released [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf)
*  [fastText](https://fasttext.cc/docs/en/english-vectors.html) (Facebook): Tomas Mikolov, Edouard Grave, Piotr Bojanowski, Christian Puhrsch and Armand Joulin released [Advances in Pre-Training Distributed Word Representations](https://arxiv.org/pdf/1712.09405.pdf)
*  [BERT](https://github.com/google-research/bert) (Google): Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova released [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805). Used [Hugging Face](https://huggingface.co/) [PyTorch version](https://github.com/huggingface/pytorch-transformers/blob/master/README.md).
*  [GPT2](https://github.com/openai/gpt-2) (OpenAI): Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei and Ilya Sutskever released [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Used [Hugging Face](https://huggingface.co/) [PyTorch version](https://github.com/huggingface/pytorch-transformers/blob/master/README.md).
*  [XLNet](https://github.com/zihangdai/xlnet) (Google/CMU): Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov, Quoc V. Le released [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237). Used [Hugging Face](https://huggingface.co/) [PyTorch version](https://github.com/huggingface/pytorch-transformers/blob/master/README.md).

Raw Data Source
---------------
*   data/Yamaha-V50-Rock-Beat-120bpm.wav, [source](https://freewavesamples.com/yamaha-v50-rock-beat-120-bpm)
*   model/spelling_en.txt, [source](https://github.com/ybisk/charNMT-noise)

Research Reference
------------------
Some of the above augmenters are inspired by the following research papers. However, it does not always follow original implementation due to different reasons. If original implementation is needed, please refer to original source code.

*   Y. Belinkov and Y. Bisk. [Synthetic and Natural Noise Both Break Neural Machine Translation](https://arxiv.org/pdf/1711.02173.pdf). 2017
*   J. Ebrahimi, A. Rao, D. Lowd and D. Dou. [HotFlip: White-Box Adversarial Examples for Text Classification](https://arxiv.org/pdf/1712.06751.pdf). 2018
*   J. Ebrahimi, D. Lowd and Dou. [On Adversarial Examples for Character-Level Neural Machine Translation](https://arxiv.org/pdf/1806.09030.pdf). 2018
*   D. Pruthi, B. Dhingra and Z. C. Lipton. [Combating Adversarial Misspellings with Robust Word Recognition](https://arxiv.org/pdf/1905.11268.pdf). 2019
*   T. Niu and M. Bansal. [Adversarial Over-Sensitivity and Over-Stability Strategies for Dialogue Models](https://arxiv.org/pdf/1809.02079.pdf). 2018
*   P. Minervini and S. Riedel. [Adversarially Regularising Neural NLI Models to Integrate Logical Background Knowledge](https://arxiv.org/pdf/1808.08609.pdf). 2018
*   X. Zhang, J. Zhao and Y. LeCun. [Character-level Convolutional Networks for Text Classification](https://arxiv.org/pdf/1509.01626.pdf). 2015
*   S. Kobayashi and C. Coulombe. [Text Data Augmentation Made Simple By Leveraging NLP Cloud APIs](https://arxiv.org/ftp/arxiv/papers/1812/1812.04718.pdf). 2018
*   Q. Xie, Z. Dai, E Hovy, M. T. Luong and Q. V. Le. [Unsupervised Data Augmentation](https://arxiv.org/pdf/1904.12848.pdf). 2019
*   W. Y. Wang and D. Yang. [That’s So Annoying!!!: A Lexical and Frame-Semantic Embedding Based Data Augmentation Approach to Automatic Categorization of Annoying Behaviors using #petpeeve Tweets](https://aclweb.org/anthology/D15-1306). 2015
*   S. Kobayashi. [Contextual Augmentation: Data Augmentation by Words with Paradigmatic Relation](https://arxiv.org/pdf/1805.06201.pdf). 2018
*   D. S. Park, W. Chan, Y. Zhang, C. C. Chiu, B. Zoph, E. D. Cubuk and Q. V. Le. [SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/pdf/1904.08779.pdf). 2019
*   R. Jia and P. Liang. [Adversarial Examples for Evaluating Reading Comprehension Systems](https://arxiv.org/pdf/1707.07328.pdf). 2017
*   Y. Belinkov and Y. Bisk. [Synthetic and Natural Noise Both Break Neural Machine Translation](https://arxiv.org/pdf/1711.02173.pdf). 2018
*   M. Alzantot, Y. Sharma, A. Elgohary, B. Ho, M. B. Srivastava and K. Chang. [Generating Natural Language Adversarial Examples](https://arxiv.org/pdf/1804.07998.pdf). 2018
*   T. Niu and M. Bansal. [Adversarial Over-Sensitivity and Over-Stability Strategies for Dialogue Models](https://arxiv.org/pdf/1809.02079.pdf). 2018
*   Z. Xie, S. I. Wang, J. Li, D. Levy, A. Nie, D. Jurafsky and A. Y. Ng. [Data Noising as Smoothing in Natural Network Language Models](https://arxiv.org/pdf/1703.02573.pdf). 2017