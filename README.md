# Aplicação de Fluxo Óptico

Em visão computacional, o método Lucas Kanade é um método diferencial amplamente usado para estimativa de fluxo óptico, desenvolvido por Bruce D. Lucas e Takeo Kanade. O método assume que o fluxo é essencialmente constante em uma vizinhança local do pixel em questão e resolve as equações básicas de fluxo óptico para todos os pixels dessa vizinhança, pelo critério dos mínimos quadrados.

## Ambiente

Para trabalhar com o vídeo, utilizaremos o OpenCV.
Primeiro, criaremos um objeto VideoCapture e leremos o primeiro quadro.

## Cálculo do fluxo óptico nos frames que seguem

Cada quadro de leitura deve ser convertido para o formato de escala de cinza.
O cálculo real será realizado por **cv2.calcOpticalFlowPyrLK()**
Você pode encontrar mais informações sobre esta função na documentação do opencv disponível [aqui](https://docs.opencv.org/2.4/modules/video/doc/motion_analysis_and_object_tracking.html)

## Artigo medium

Além das referências, elaborei um artigo no medium.

[Rastreamento por Fluxo Óptico com OpenCV](https://medium.com/@toni_esteves/rastreamento-por-fluxo-%C3%B3ptico-com-opencv-aa6302630f7c)


![alt text](https://s4.gifyu.com/images/ezgif.com-optimize-3.gif)

## Referências

* https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

* http://www.diva-portal.org/smash/get/diva2:273847/FULLTEXT01.pdf

* https://www.researchgate.net/publication/320908264_A_Review_On_Particle_Image_Velocimetry_And_Optical_Flow_Methods_In_Riverine_Environment

* https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html

* https://en.wikipedia.org/wiki/Optical_flow

* http://www.lps.usp.br/hae/projform/2010_gabriel_ramires/fluxo_optico.html

* https://sandipanweb.wordpress.com/2018/02/25/implementing-lucas-kanade-optical-flow-algorithm-in-python/
