# BARTViBa

# HOW TO

* The current best model is aligned_bartpho model, the checkpoint is stored at: https://drive.google.com/drive/folders/10M4l95A7ImxfSPtV8JzAWNm5ytrUwOgC?usp=sharing 
* This repository has already embedded the checkpoint in the folder "pretrained". 
* First: Start VNCoreNLP server at:
    >vncorenlp -Xmx2g GraphTranslation/vncorenlp/VnCoreNLP-1.1.1.jar -p 9000 -a "wseg,pos,ner,parse"
* Then:  Start api server port 8000:
    >python app.py
* The model type that we run: BART_CHUNK

If you want to run the files in the Kriem_vi folder, which contains all the Vietnamese text files, you can run the sendtextfile.py file and input the approriate Kriem_vi file name in the "file_name_vi" variable on line 16.
