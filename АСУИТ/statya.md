# Классификация клеток крови с использованием интерпретируемых признаков формы: Сравнительное исследование SVM-моделей и подходов на основе CNN

## Вступление

## Цель исследования
Существует множество моделей для анализа, подсчёта и классификации клеток крови. К примеру Lou и др. использовали метод опорных векторов на основе спектрального анализа для подсчёта эритроцитов[1](#1). Cruz и др. создали систему, исползующую пороговое значение насыщенности оттенка и связную маркировку для независимого подсчёта эритроцитов, лейкоцитов и тромбоцитов[2](#2). Acharya and Kumar построили систему подсчёта эритроцитов используя разделение вокруг медоида и преобразование Хафа [3](#3). Singhal и Singh классифицировали злокачественные и доброкачественные лейкоциты, используя 256 локальных бинарных признаков [4](#4). Затем они увеличили количество используемых ими признаков до 4096, чтобы улучшить результаты классификации[5](#5). И наоборот, Bhattacharjee и Saini использовали только 8 признаков работы метода k-ближайших соседей для классификации лейкоцитов[6](#6). Kutlu и другие, а также Long' использовали различные сверточные нейронные сети для классификации разных типов лейкоцитов [7](#7),[8](#8). Однако ни один из этих методов не позволяет одновременно подсчитывать количество эритроцитов, тромбоцитов и лейкоцитов.

Популярным методом анализа и классификации изображений является использование сверточных нейронных сетей [9](#9). Эта модель вычислений также очень популярна в анализе медицинских изображений [10](#10),[11](#11). Свёрточные нейронные сети способны самостоятельно определить важные, для решение конкретной задачи, признаки [9](#9). Существует множество различных архитектур для CNN, включая VGGNet[12](#12), Resnet[13](#13) и YOLO[14](#14). Трансферное обучение особенно полезно, когда исследователь располагает набором данных с небольшим количеством наблюдений или экземпляров. При таком подходе заданная архитектура сначала тренируется на наборе данных, которых очень много. Затем предварительно обученная CNN тренируется на задаче, которую исследует аналитик [9](#9).
Один из главных недостатков использования CNN это сложность интерпретации модели и признаков, используемых моделью, вне зависимости от архитектуры. Некоторые исследователи снижают размерность признаков, используемых для классификации, и добивались успеха. Так, например Sahlol и др. использовали трансферное обучение модели VGGNet в сочетаннии со статистически улучшенным алгоритмом Salp Swarm Algorithm(SESSA) для извлечения более полезных признаков для классификации здоровых и злокачественных лейкоцитов [11](#11). В лезультате было отобрано более 1000 признаков из 25088 возможных, которые затем были использованы в модели классификации на базе метода опорных векторов [11](#11). Однако этот подход всё ещё не даёт достаточного представления о важных признаков для определения доброкачественных и злокачественных лейкоцитов. Кроме того, эта система в основном занимается классификацией лейкоцитов и не способна отличить лейкоциты от эритроцитов или тромбоцитов.

Alam и Islam в своей статье [14] (#14) представили различные модели YOLO CNN для одновременного подсчёта эритроцитов, лейкоцитов и тромбоцитов с использованием различных архитектур. Однако, нио дна из этих моделей не предоставляет прямой интерпретации. Более того, есть предположения, что модели, использующие интерпретируемые признаки, способны превзойти CNN[15] (#15).


## Библиографический список

### 1.  
J. Lou, M. Zhou, Q. Li, C. Yuan, H. Liu, An automatic red blood cell counting method based on spectral images. 2016 9th International Congress on Image and Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI), 2016, pp. 1391–1396, https://doi.org/10.1109/CISP-BMEI.2016.7852934.

### 2. 
D. Cruz, C. Jennifer, Valiente, L.C. Castor, C.M.T. Mendoza, B.A. Jay, L.S.C. Jane, P.
T.B. Brian, Determination of blood components (WBCs, RBCs, and Platelets) count
in microscopic images using image processing and analysis. 2017IEEE 9th
International Conference on Humanoid, Nanotechnology, Information Technology,
Communication and Control, Environment and Management (HNICEM), 2017,
pp. 1–7, https://doi.org/10.1109/HNICEM.2017.8269515.ISSN: null

### 3. 
V. Acharya, P. Kumar, Identification and red blood cell automated counting from
blood smear images using computer-aided system, Medical & Biological
Engineering & Computing 56 (3) (2018) 483–489, https://doi.org/10.1007/s11517-017-1708-9

### 4.
V. Singhal, P. Singh, Local Binary Pattern for automatic detection of Acute
Lymphoblastic Leukemia. 2014 Twentieth National Conference on
Communications (NCC), 2014, pp. 1–5, https://doi.org/10.1109/NCC.2014.6811261.

### 5.
V. Singhal, P. Singh, Texture Features for the Detection of Acute Lymphoblastic
Leukemia, 2016, pp. 535–543, https://doi.org/10.1007/978-981-10-0135-2_52.

### 6.
R. Bhattacharjee, L.M. Saini, Robust technique for the detection of Acute
Lymphoblastic Leukemia. 2015 IEEE Power, Communication and Information
Technology Conference (PCITC), 2015, pp. 657–662, https://doi.org/10.1109/PCITC.2015.7438079.

### 7.
H. Kutlu, E. Avci, F. ¨Ozyurt, White blood cells detection and classification based on
regional convolutional neural networks, Med. Hypotheses 135 (2020) 109472,
https://doi.org/10.1016/j.mehy.2019.109472.https://www.sciencedirect.com/science/article/pii/S0306987719310680

### 8. 
F. Long, J.-J. Peng, W. Song, X. Xia, J. Sang, Bloodcaps: a capsule network based
model for the multiclassification of human peripheral blood cells, Comput Methods
Programs Biomed 202 (2021) 105972, https://doi.org/10.1016/j.cmpb.2021.105972.https://www.sciencedirect.com/science/article/pii/S016926072100047X

### 9.
J. Gu, Z. Wang, J. Kuen, L. Ma, A. Shahroudy, B. Shuai, T. Liu, X. Wang, G. Wang,
J. Cai, T. Chen, Recent advances in convolutional neural networks, Pattern
Recognit 77 (2018) 354–377, https://doi.org/10.1016/j.patcog.2017.10.013.

### 10.
A. Esteva, K. Chou, S. Yeung, N. Naik, A. Madani, A. Mottaghi, Y. Liu, E. Topol, J. Dean, R. Socher, Deep learning-enabled medical computer vision, npj Digital Medicine 4 (1) (2021) 1–9, https://doi.org/10.1038/s41746-020-00376-2.
Bandiera_abtest: a Cc_license_type: cc_by Cg_type: Nature Research Journals
Number: 1 Primary_atype: Reviews Publisher: Nature Publishing Group Subject_
term: Computational science;Health care;Medical research Subject_term_id:
computational-science;health-care;medical-research

### 11. 
A.T. Sahlol, P. Kollmannsberger, A.A. Ewees, Efficient classification of white blood
cell leukemia with improved swarm optimization of deep features, Sci Rep 10 (1)
(2020) 2536, https://doi.org/10.1038/s41598-020-59215-9.Number: 1 Publisher:
Nature Publishing Group

### 12.
K. Simonyan, A. Zisserman, Very deep convolutional networks for large-scale image recognition, arXiv:1409.1556 [cs] (2015).ArXiv: 1409.1556, http://arxiv.org/abs/1409.1556

### 13. 
K. He, X. Zhang, S. Ren, J. Sun, Deep Residual Learning for Image Recognition. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), IEEE, Las Vegas, NV, USA, 2016, pp. 770–778, https://doi.org/10.1109/CVPR.2016.90.
http://ieeexplore.ieee.org/document/7780459/

### 14.
M.M. Alam, M.T. Islam, Machine learning approach of automatic identification and counting of blood cells, Healthc Technol Lett 6 (4) (2019) 103–108, https://doi.org/10.1049/htl.2018.5098.https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6718065/

### 15.
W.F. Lamberti, Classification of Synthetic Aperture Radar Images of Icebergs and Ships Using Random Forests Outperforms Convolutional Neural Networks. 2020 IEEE Radar Conference (RadarConf20), 2020, pp. 1–6, https://doi.org/10.1109/RadarConf2043947.2020.9266369.ISSN: 2375–5318

## Сведения об авторе
Шеретов Марк Алексеевич - магистрант кафедры ИТАС, Пермского национального исследовательского политехнического университета, групы АСУ8-23-1М, г.Пермь, e-mail: mark.sheretov@gmail.com 