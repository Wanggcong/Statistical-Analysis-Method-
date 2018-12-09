#include<iostream>
#include<iomanip>
using namespace std;
int main(){
	double a=16989.31278129,b=8059.72578743,c=9705.11321773,d=6730.40809095,e=17331.53343805;
	double bzc=1.96*11366.681011506962;
	cout<<"标准差乘1.96的结果为："<<fixed<<setprecision(8)<<bzc<<endl;
	cout<<"第一个预测人的置信区间为：["<<a-bzc<<","<<a+bzc<<"]"<<endl;
	cout<<"第二个预测人的置信区间为：["<<b-bzc<<","<<b+bzc<<"]"<<endl;
	cout<<"第三个预测人的置信区间为：["<<c-bzc<<","<<c+bzc<<"]"<<endl;
	cout<<"第四个预测人的置信区间为：["<<d-bzc<<","<<d+bzc<<"]"<<endl;
	cout<<"第五个预测人的置信区间为：["<<e-bzc<<","<<e+bzc<<"]"<<endl;
} 
