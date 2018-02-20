# An LSTM Recurrent Network for Step Counting

Trained LSTM models for step counting based on annotated smartphone sensor data from the WeAllWork dataset using TensorFlow. The models were built for sighted people (na), blind people with white cane (wc) and guide dog (gd) separately for Leave-One-Out training modality. Three error metric is used to measure the overcount and overcount rate. Details are shown in the report.

### Data Preprocess

Two kinds of files from the dataset are used. The first type is CSV format iPhone sensor data saved in weallwalk/sensor folder, and named as "iPhoneSensors_Tx_IDx_xx_xx.csv" . The second type is XML file containing annotated ground truth data saved in weallwalk/xml folder, and is named as same as the WeAllWork dataset - "Tx_IDx_xx.xml". After saving the two kinds of files in corresponding folders, the code can run in jupyter. 

Preprocess.py converted the data from WeAllWalk into a different set of files. The input path and output path could be changed in line 7 and 9. 


### LSTM model

The values of graph variable may be saved and restored to and from checkpoints in ckpt files in lstm_check folder, which will be automatically created if the saver class is used.

Two ways of splitting training and testing data is used. The first way is to simply mix all data and split it into the training set and testing set. In this way, both the training and the testing data contain records from all participant and all segments. The second way is leaving one person out, which means testing set contains and only contains all records from one participant while the training set contains all other records from the remaining participants.

The lstm_gd_mix file built the lstm network for blind people with a guide dog for mixed data without cross-validation and leave-one-out.

The lstm_wc_leave-one-out file built the lstmnetwork for blind people with a long cane with leave-one-out and cross-validation.

The lstm_na_leave-one-out file built the lstmnetwork for sighted people with leave-one-out and cross-validation.
