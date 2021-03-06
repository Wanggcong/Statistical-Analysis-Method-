DATA hw3;
INFILE '/folders/myfolders/data.csv' DLM = ',' DSD MISSOVER;
INPUT AGE SEX $ BMI CHILDREN SMOKER $ REGION $ CHARGES;
RUN; 

PROC GLM DATA = hw3;
CLASS SEX SMOKER;
MODEL CHARGES = SEX SMOKER SEX * SMOKER;
MEANS SEX SMOKER SEX * SMOKER;
RUN;