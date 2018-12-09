/*age,sex,bmi,children,smoker,region,charges*/

/*1*/
PROC IMPORT DATAFILE='/folders/myfolders/data.csv' REPLACE
	DBMS=CSV
	OUT=data0;
	GETNAMES=YES;
RUN;

proc reg data=data0;
model charges=age bmi children/cli alpha=0.05;


/*2a*/
PROC IMPORT DATAFILE='/folders/myfolders/data.csv' REPLACE
	DBMS=CSV
	OUT=data0;
	GETNAMES=YES;
RUN;

proc anova data=data0;
class sex;
model charges=sex;
means sex/alpha=0.05;
run;

/*2b*/
PROC IMPORT DATAFILE='/folders/myfolders/data.csv' REPLACE
	DBMS=CSV
	OUT=data0;
	GETNAMES=YES;
RUN;

proc glm data=data0 alpha=0.05;
class sex smoker;
model charges=sex|smoker;
means sex|smoker /snk;
run;